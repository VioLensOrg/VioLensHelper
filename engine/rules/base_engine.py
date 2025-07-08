import inspect
from experta.engine import KnowledgeEngine
from experta import Fact
from experta.rule import Rule
from experta.deffacts import DefFacts

from ..facts import (
    ViolenceClassification, AnalysisResult, ProcessingPhase
)

from knowledge_base.violence_types import VIOLENCE_TYPES

class BaseViolenceEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.explanations = {}

    @DefFacts()
    def initial_facts(self):
        yield Fact(engine_ready=True)
        yield ProcessingPhase(phase="collection")  # Fase inicial: coleta de fatos

    @Rule(ProcessingPhase(phase="collection"))
    def start_analysis_phase(self):
        """
        Transição da fase de coleta para a fase de análise.
        Esta regra dispara após todos os fatos serem declarados.
        """
        print(" Transitando para fase de análise...")
        # Remover a fase de coleta
        for fact_id in self.get_matching_facts(ProcessingPhase):
            self.retract(fact_id)
        # Declarar a fase de análise
        self.declare(ProcessingPhase(phase="analysis"))

    def create_classification(self, violence_type, subtype=None, explanations=None, facts_used=None, reasoning=None):
        """
        Cria uma classificação de violência com explicações detalhadas.
        """
        subtype = subtype or ""
        if self._classification_exists(violence_type, subtype):
            return

        key = f"{violence_type}_{subtype}" if subtype else violence_type

        if facts_used:
            self._add_detailed_explanations(key, facts_used, violence_type, subtype, reasoning)
        elif explanations:
            self._add_simple_explanations(key, explanations)

        self._declare_classification_fact(violence_type, subtype, key)

    def _classification_exists(self, violence_type, subtype):
        for fact_id in self.get_matching_facts(ViolenceClassification):
            fact = self.facts[fact_id]
            if fact["violence_type"] == violence_type and fact["subtype"] == subtype:
                return True
        return False

    def _add_detailed_explanations(self, key, facts_used, violence_type, subtype, reasoning):
        conclusion = f"{violence_type}" + (f" do tipo {subtype}" if subtype else "")
        detailed_explanations = self.format_detailed_explanation(facts_used, conclusion, reasoning)
        if key not in self.explanations:
            self.explanations[key] = []
        for explanation in detailed_explanations:
            if explanation not in self.explanations[key]:
                self.explanations[key].append(explanation)

    def _add_simple_explanations(self, key, explanations):
        if key not in self.explanations:
            self.explanations[key] = []
        for explanation in explanations:
            if explanation not in self.explanations[key]:
                self.explanations[key].append(explanation)

    def _declare_classification_fact(self, violence_type, subtype, key):
        self.declare(
            ViolenceClassification(
                violence_type=violence_type,
                subtype=subtype,
                explanation=self.explanations.get(key, []).copy()
            )
        )
    
    def run(self, steps=None):
        """
        Executa o motor em modo controlado por fases.
        """
        print("\nIniciando análise com motor de inferência...")

        # Limitar o número máximo de iterações para evitar loops infinitos
        max_iterations = 100
        iteration = 0
        
        # Executar até que não haja mais regras para disparar ou atingir limite
        while self.agenda and iteration < max_iterations:
            super().run(1)  # Executar apenas uma regra por vez
            iteration += 1
            
            # Sair se não houver mais regras para acionar
            if not self.agenda:
                break
        
        self.consolidate_results()

    def consolidate_results(self):
        """
        Consolida os resultados de todas as classificações.
        """
        all_classifications = []
        for fact_id in self.get_matching_facts(ViolenceClassification):
            fact = self.facts[fact_id]
            all_classifications.append({
                "violence_type": fact["violence_type"],
                "subtype": fact["subtype"] or "",
                "explanation": self.get_explanation(fact["violence_type"], fact["subtype"])
            })
        
        if not all_classifications:
            print("Nenhum tipo de violência identificado")
            self.declare(
                AnalysisResult(
                    classifications=[],
                    primary_result={"violence_type": "", "subtype": ""},
                    multiple_types=False
                )
            )
            return
        
        # Reportar múltiplos se houver mais de um
        report_multiple = len(all_classifications) > 1
        
        # Primeiro resultado como principal
        primary_result = all_classifications[0]
        
        self.declare(
            AnalysisResult(
                classifications=all_classifications,
                primary_result=primary_result,
                multiple_types=report_multiple
            )
        )

        print("\nAnálise concluída:")

        if report_multiple:
            print(f"   • {len(all_classifications)} tipos de violência identificados")
            for i, cls in enumerate(all_classifications, 1):
                subtype_text = f" ({cls['subtype']})" if cls['subtype'] else ""
                print(f"   {i}. {cls['violence_type']}{subtype_text}")
        else:
            subtype_text = f" - {primary_result['subtype']}" if primary_result.get('subtype') else ""
            print(f"   • Tipo identificado: {primary_result['violence_type']}{subtype_text}")

        
    def get_explanation(self, violence_type, subtype=None):
        key = f"{violence_type}_{subtype}" if subtype else violence_type
        return self.explanations.get(key, [])
    
    def get_matching_facts(self, fact_type):
        return [fact_id for fact_id, fact in self.facts.items() 
                if isinstance(fact, fact_type)]
    
    def debug_facts(self):
            print(f"\n{len(self.facts)} fatos carregados no motor de inferência")


    def reset(self):
        self.explanations = {}
        
        super().reset()
        print("Motor de regras reiniciado completamente")

    def format_detailed_explanation(self, facts_used, conclusion, reasoning=None):
        """
        Gera uma explicação detalhada em linguagem natural baseada nos fatos que ativaram a regra.
        """
        basic_explanation = [f"Identificado: {conclusion}"]
        detailed_explanation = ["**Como chegamos a esta conclusão:**"]

        # Adiciona cada parte da explicação usando funções auxiliares
        self._append_behavior_explanation(detailed_explanation, facts_used)
        self._append_context_explanation(detailed_explanation, facts_used)
        self._append_frequency_explanation(detailed_explanation, facts_used)
        self._append_target_explanation(detailed_explanation, facts_used)
        self._append_relationship_explanation(detailed_explanation, facts_used)
        self._append_impact_explanation(detailed_explanation, facts_used)

        if reasoning:
            detailed_explanation.append(f"\n**Por que isso é importante:** {reasoning}")

        return basic_explanation + detailed_explanation

    def _append_behavior_explanation(self, explanation_list, facts_used):
        if 'behavior' in facts_used:
            behaviors = facts_used['behavior']
            behavior_text = ", ".join(behaviors) if len(behaviors) > 1 else behaviors[0]
            explanation_list.append(f"- Identificamos em seu relato comportamentos de {behavior_text}")

    def _append_context_explanation(self, explanation_list, facts_used):
        if 'context' in facts_used:
            contexts = facts_used['context']
            context_text = ", ".join(contexts) if len(contexts) > 1 else contexts[0]
            explanation_list.append(f"- O incidente ocorreu em um contexto de {context_text}")

    def _append_frequency_explanation(self, explanation_list, facts_used):
        if 'frequency' in facts_used:
            frequencies = facts_used['frequency']
            freq_text = ", ".join(frequencies) if len(frequencies) > 1 else frequencies[0]
            explanation_list.append(f"- O comportamento ocorre {freq_text}")

    def _append_target_explanation(self, explanation_list, facts_used):
        if 'target' in facts_used:
            targets = facts_used['target']
            target_text = ", ".join(targets) if len(targets) > 1 else targets[0]
            explanation_list.append(f"- O comportamento foi direcionado com base em {target_text}")

    def _append_relationship_explanation(self, explanation_list, facts_used):
        if 'relationship' in facts_used:
            relationships = facts_used['relationship']
            rel_text = ", ".join(relationships) if len(relationships) > 1 else relationships[0]
            explanation_list.append(f"- Existe uma relação de {rel_text} entre as partes envolvidas")

    def _append_impact_explanation(self, explanation_list, facts_used):
        if 'impact' in facts_used:
            impacts = facts_used['impact']
            impact_text = ", ".join(impacts) if len(impacts) > 1 else impacts[0]
            explanation_list.append(f"- O comportamento causou {impact_text}")
