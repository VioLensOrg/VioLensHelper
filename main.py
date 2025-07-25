import os
import re
import streamlit as st
from engine.expert_system import ExpertSystem
from knowledge_base.violence_types import VIOLENCE_TYPES
from knowledge_base.keyword_aliases import KEYWORD_ALIASES

def apply_aliases_to_text(text: str) -> str:
    
    result = text
    
    # Ordenar as palavras-chave por tamanho (maiores primeiro) para evitar substituições parciais
    sorted_keywords = sorted(KEYWORD_ALIASES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for keyword, alias in sorted_keywords:
        # Usar boundary para palavras com letras/números, ou posição para caracteres especiais
        if keyword.replace("_", "").isalnum():
            pattern = rf'\b{re.escape(keyword)}\b'
        else:
            pattern = rf'{re.escape(keyword)}'
        result = re.sub(pattern, alias, result, flags=re.IGNORECASE)
    
    return result

@st.cache_resource
def get_expert_system():
    if 'expert_system' not in st.session_state:
        api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
        st.session_state.expert_system = ExpertSystem(api_key=api_key)
    return st.session_state.expert_system

st.set_page_config(
    page_title="Sistema Especialista",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.title("Sistema Especialista de Identificação de Violência")

if 'state' not in st.session_state:
    st.session_state.state = 'initial'
if 'keywords' not in st.session_state:
    st.session_state.keywords = {}
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'missing_fields' not in st.session_state:
    st.session_state.missing_fields = []
if 'partial_facts' not in st.session_state:
    st.session_state.partial_facts = {}
if 'results' not in st.session_state:
    st.session_state.results = []

expert_system = get_expert_system()

if st.session_state.state == 'initial':
    st.subheader("Relate a situação ocorrida")
    
    user_text = st.text_area(
        "Descreva em detalhes o que aconteceu:",
        height=200,
        placeholder="Conte com suas palavras o que aconteceu, incluindo detalhes sobre o comportamento, local, frequência e como isso te afetou..."
    )
    
    if st.button("Analisar"):
        if len(user_text) < 20:
            st.error("Por favor, forneça um relato mais detalhado para análise.")
        else:
            with st.spinner("Analisando seu relato..."):
                result = expert_system.analyze_text(user_text)
                
                st.session_state.results = result["classifications"]
                st.session_state.state = 'result'
                st.rerun()

elif st.session_state.state == 'follow_up':
    st.subheader("Precisamos de mais algumas informações")
    
    if st.session_state.keywords:
        st.write("Com base no seu relato, identificamos:")
        for category, keywords in st.session_state.keywords.items():
            if keywords:
                category_name = category.replace("_", " ").capitalize()
                st.write(f"- **{category_name}**: {', '.join(keywords)}")
    
    st.write("Para uma análise mais precisa, por favor responda:")
    for question in st.session_state.questions:
        st.write(f"- {question}")
    
    follow_up_text = st.text_area(
        "Sua resposta:",
        height=150,
        placeholder="Responda as perguntas acima para continuar a análise..."
    )
    
    if st.button("Continuar análise"):
        if follow_up_text:
            with st.spinner("Processando suas respostas..."):
                # Processar a resposta complementar através do sistema especialista
                combined_text = follow_up_text 
                
                result = expert_system.analyze_text(combined_text)
                
                st.session_state.results = result["classifications"]
                st.session_state.state = 'result'
                st.rerun()
        else:
            st.error("Por favor, responda às perguntas para continuar.")

elif st.session_state.state == 'result':
    st.subheader("Resultados da Análise")
    
    if not st.session_state.results:
        st.info("Nenhum tipo de violência foi identificado com base nas informações fornecidas.")
    else:
        st.success("Identificamos possíveis tipos de violência:")
        
        for r in st.session_state.results:
            vtype = r["violence_type"]
            subtype = r.get("subtype")
            
            if subtype:
                subtype_formatted = subtype.replace("_", " ").capitalize()
                title = f"{subtype_formatted} ({vtype.replace('_', ' ').title()})"
            else:
                title = VIOLENCE_TYPES[vtype]['nome'] if 'nome' in VIOLENCE_TYPES[vtype] else vtype.replace('_', ' ').title()
            
            st.markdown(f"#### {title}")
            with st.expander("Ver detalhes"):
                if subtype and "subtipos" in VIOLENCE_TYPES[vtype] and subtype in VIOLENCE_TYPES[vtype]["subtipos"]:
                    st.write(VIOLENCE_TYPES[vtype]["subtipos"][subtype]["definicao"])
                else:
                    st.write(VIOLENCE_TYPES[vtype]["definicao"])
                
                if "explanation" in r and r["explanation"]:
                    st.subheader("Por que identificamos este tipo:")
                    
                    for i, exp in enumerate(r["explanation"]):
                        if exp.strip():
                            clean_exp = exp.strip()
                            if clean_exp.startswith("- "):
                                clean_exp = clean_exp[2:]
                            
                            # Verificar se é um cabeçalho (como "Como chegamos a esta conclusão:")
                            if clean_exp.endswith(":") and len(clean_exp.split()) <= 6:
                                # É um cabeçalho - formatar como subseção SEM bullet point
                                st.markdown(f"##### {clean_exp}")
                                # Adicionar uma linha em branco para separação visual
                                st.write("")
                            else:
                                # É um item da lista - aplicar aliases e mostrar como bullet point
                                formatted_exp = apply_aliases_to_text(clean_exp)
                                st.write(f"• {formatted_exp}")
                
                if "recomendacoes" in VIOLENCE_TYPES[vtype]:
                    st.subheader("Recomendações:")
                    for rec in VIOLENCE_TYPES[vtype]["recomendacoes"]:
                        st.write(f"• {rec}")


    if st.button("Iniciar Nova Análise"):
        for key in ['state', 'keywords', 'questions', 'missing_fields', 'partial_facts', 'results', 'expert_system']:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state.state = 'initial'
        st.rerun()