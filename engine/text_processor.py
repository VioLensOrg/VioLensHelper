import os
from typing import Dict, List, Any

from knowledge_base.keywords_dictionary import KEYWORDS_DICT
from utils.groq_integration import GroqAPI

from engine.facts import (
    TextRelato, KeywordFact, ViolenceBehavior, ContextFact, FrequencyFact,
    TargetFact, RelationshipFact, ImpactFact
)

class TextProcessor:
    """
    Processa texto livre do usuário para extrair fatos e disparar regras.
    """
    def __init__(self, api_key: str = None, 
                 model: str = "meta-llama/llama-4-scout-17b-16e-instruct"):

        self.api_key = api_key if api_key else os.environ.get("GROQ_API_KEY", "")
        self.model = model
        self.groq_api = GroqAPI(api_key=self.api_key, model=self.model)
        self.conversation_context = []

    def create_experta_facts(self, text: str) -> List[Any]:
        print(f"\nAnalisando relato (primeiros 100 caracteres): {text[:100]}{'...' if len(text) > 100 else ''}")
        
        # Lista para armazenar os fatos que serão retornados
        facts = [TextRelato(text=text, processed=True)]
        
        try:
            # Extrair palavras-chave usando o Groq
            prompt = self.groq_api.build_prompt(text, KEYWORDS_DICT)
            response = self.groq_api.send_request(prompt)
            
            if "identified_keywords" in response and response["identified_keywords"]:
                keywords = response["identified_keywords"]
                
                # Mostrar resumo das palavras-chave identificadas
                print(f"Elementos identificados no relato:")
                for category, values in keywords.items():
                    if values:
                        category_name = {
                            "action_type": "Comportamentos",
                            "frequency": "Frequência", 
                            "context": "Local/Contexto",
                            "target": "Características visadas",
                            "relationship": "Relacionamento",
                            "impact": "Impactos"
                        }.get(category, category)
                        print(f"   • {category_name}: {', '.join(values)}")
                
                print(f"\nCriando fatos para o motor de inferência...")
                
                # Converter resposta em fatos Experta
                for category, values in keywords.items():
                    for keyword in values:
                        # Criar fato KeywordFact
                        kw_fact = KeywordFact(category=category, keyword=keyword)
                        facts.append(kw_fact)
                        
                        # Criar fatos específicos correspondentes (sem log detalhado)
                        if category == "action_type":
                            behavior_fact = ViolenceBehavior(behavior_type=keyword)
                            facts.append(behavior_fact)
                        elif category == "context":
                            context_fact = ContextFact(location=keyword)
                            facts.append(context_fact)
                        elif category == "frequency":
                            freq_fact = FrequencyFact(value=keyword)
                            facts.append(freq_fact)
                        elif category == "target":
                            target_fact = TargetFact(characteristic=keyword)
                            facts.append(target_fact)
                        elif category == "relationship":
                            rel_fact = RelationshipFact(type=keyword)
                            facts.append(rel_fact)
                        elif category == "impact":
                            impact_fact = ImpactFact(type=keyword)
                            facts.append(impact_fact)
                
                print(f"{len(facts)} fatos criados para análise")
            else:
                print("Nenhum elemento relevante identificado no texto")
        
        except Exception as e:
            print(f"Erro durante análise: {str(e)}")
        
        return facts

    # Acabamos não usando esse método, mas deixamos aqui para referência futura
    def _process_followup(self, follow_up_text: str, previous_keywords: Dict, missing_fields: List[str]) -> Dict[str, Any]:
        """
        Processa resposta de follow-up para complementar informações.
        """
        self.conversation_context.append({"role": "user", "content": follow_up_text})
        prompt = self.groq_api.build_prompt(follow_up_text, KEYWORDS_DICT, is_follow_up=True, missing_fields=missing_fields)
        response = self.groq_api.send_request(prompt)

        combined_keywords = self._combine_keywords(previous_keywords, response.get("identified_keywords", {}))
        facts = self._extract_facts_from_keywords(combined_keywords)

        missing = response.get("missing_information", [])
        questions = response.get("follow_up_questions", [])
        missing_critical = any(field in missing for field in ["action_type"])

        return {
            "status": "complete" if not missing_critical else "incomplete",
            "identified_keywords": combined_keywords,
            "missing_fields": missing,
            "questions": questions,
            "facts": facts
        }
    