from experta import Fact, Field
from knowledge_base.violence_types import VIOLENCE_TYPES, SEVERITY_LEVEL, REPORT_CONTACT
import streamlit as st

### Fatos de Entrada ###

class TextRelato(Fact):
    text = Field(str, mandatory=True)
    processed = Field(bool, default=False)

class KeywordFact(Fact):
    category = Field(str, mandatory=True)
    keyword = Field(str, mandatory=True)

class ViolenceBehavior(Fact):
    behavior_type = Field(str, mandatory=True)

class ContextFact(Fact):
    location = Field(str, mandatory=True)

class FrequencyFact(Fact):
    value = Field(str, mandatory=True)

class TargetFact(Fact):
    characteristic = Field(str, mandatory=True)

class RelationshipFact(Fact):
    type = Field(str, mandatory=True)

class ImpactFact(Fact):
    type = Field(str, mandatory=True)

### Fatos de Saída ###

class ViolenceClassification(Fact):
    """
    Representa o resultado da classificação de um tipo de violência.
    """
    violence_type = Field(str, mandatory=True)  # Tipo principal de violência
    subtype = Field(str, default="")            # Subtipo (se aplicável)
    explanation = Field(list, default=[])       # Lista de explicações

class AnalysisResult(Fact):
    """
    Armazena o resultado final da análise
    """
    classifications = Field(list, default=[])   # Lista de classificações 
    primary_result = Field(dict, default=None)  # Resultado principal
    multiple_types = Field(bool, default=False) # Indica se foram encontrados múltiplos tipos\

### Fatos de Controle ###

class ProcessingPhase(Fact):
    """Controla a fase de processamento do motor de inferência."""
    phase = Field(str, mandatory=True)  # 'collection', 'analysis'

def print_information(violence_type, subtype=None):
    info = VIOLENCE_TYPES.get(violence_type)
    if not info:
        st.warning("Informações adicionais não disponíveis.")
        return

    title, definition = _get_title_and_definition(info, violence_type, subtype)
    st.markdown(f"### ✅ {title}")
    st.markdown(f"**Definição:** {definition}")

    _print_severity(info)
    _print_contacts(info)
    _print_recommendations(info)

def _get_title_and_definition(info, violence_type, subtype):
    title = violence_type.replace('_', ' ').title()
    if subtype and subtype in info.get('subtipos', {}):
        subtype_info = info['subtipos'][subtype]
        title += f" - {subtype.replace('_', ' ').title()}"
        definition = subtype_info.get('definicao', info.get('definicao', ''))
    else:
        definition = info.get('definicao', '')
    return title, definition

def _print_severity(info):
    severity = info.get('gravidade')
    if severity:
        st.markdown(f"**Gravidade:** {SEVERITY_LEVEL.get(severity, '')}")

def _print_contacts(info):
    contacts = info.get("canais_denuncia", [])
    if contacts:
        st.markdown("**Canais de denúncia:**")
        for contact in contacts:
            contact_info = REPORT_CONTACT.get(contact)
            if contact_info:
                st.markdown(f"- **{contact}**: {contact_info.get('descricao')}")
                if "contato" in contact_info:
                    st.markdown(f"  📧 Contato: `{contact_info['contato']}`")
                st.markdown(f"  📌 Procedimento: {contact_info.get('procedimento')}")

def _print_recommendations(info):
    recommendations = info.get("recomendacoes", [])
    if recommendations:
        st.markdown("**Recomendações:**")
        for r in recommendations:
            st.markdown(f"- {r}")