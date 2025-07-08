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

        facts = [TextRelato(text=text, processed=True)]

        try:
            prompt = self.groq_api.build_prompt(text, KEYWORDS_DICT)
            response = self.groq_api.send_request(prompt)

            keywords = self._extract_keywords_from_response(response)
            self._print_keywords_summary(keywords)

            if keywords:
                print(f"\nCriando fatos para o motor de inferência...")
                self._add_keyword_facts(facts, keywords)
                print(f"{len(facts)} fatos criados para análise")
            else:
                print("Nenhum elemento relevante identificado no texto")

        except Exception as e:
            print(f"Erro durante análise: {str(e)}")

        return facts

    def _extract_keywords_from_response(self, response: Dict) -> Dict:
        if "identified_keywords" in response and response["identified_keywords"]:
            return response["identified_keywords"]
        return {}

    def _print_keywords_summary(self, keywords: Dict):
        if not keywords:
            return
        print(f"Elementos identificados no relato:")
        category_names = {
            "action_type": "Comportamentos",
            "frequency": "Frequência",
            "context": "Local/Contexto",
            "target": "Características visadas",
            "relationship": "Relacionamento",
            "impact": "Impactos"
        }
        for category, values in keywords.items():
            if values:
                category_name = category_names.get(category, category)
                print(f"   • {category_name}: {', '.join(values)}")

    def _add_keyword_facts(self, facts: List[Any], keywords: Dict):
        for category, values in keywords.items():
            for keyword in values:
                facts.append(KeywordFact(category=category, keyword=keyword))
                if category == "action_type":
                    facts.append(ViolenceBehavior(behavior_type=keyword))
                elif category == "context":
                    facts.append(ContextFact(location=keyword))
                elif category == "frequency":
                    facts.append(FrequencyFact(value=keyword))
                elif category == "target":
                    facts.append(TargetFact(characteristic=keyword))
                elif category == "relationship":
                    facts.append(RelationshipFact(type=keyword))
                elif category == "impact":
                    facts.append(ImpactFact(type=keyword))

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
    