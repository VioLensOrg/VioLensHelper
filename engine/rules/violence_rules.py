from .base_engine import BaseViolenceEngine
from .microaggression_rules import MicroaggressionRulesMixin
from .sexual_violence_rules import SexualViolenceRulesMixin
from .discrimination_rules import DiscriminationRulesMixin
from .harassment_rules import HarassmentRulesMixin
from .digital_violence_rules import DigitalViolenceRulesMixin


class ViolenceRules(
    BaseViolenceEngine,
    MicroaggressionRulesMixin,
    SexualViolenceRulesMixin,
    DiscriminationRulesMixin,
    HarassmentRulesMixin,
    DigitalViolenceRulesMixin
):
    """
    Motor de regras completo para identificação de tipos de violência.
    
    Esta classe combina todas as especializações de regras em um único motor,
    herdando de:
    - BaseViolenceEngine: Infraestrutura básica e métodos comuns
    - MicroaggressionRulesMixin: Regras para microagressões
    - SexualViolenceRulesMixin: Regras para violência sexual
    - DiscriminationRulesMixin: Regras para discriminação
    - HarassmentRulesMixin: Regras para assédio/perseguição
    - DigitalViolenceRulesMixin: Regras para violência digital
    """
    
    def __init__(self):
        super().__init__()