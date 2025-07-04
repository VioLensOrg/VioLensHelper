from knowledge_base.violence_types import VIOLENCE_TYPES, CRITERION_WEIGHTS
from typing import Dict, List
from knowledge_base.violence_types import CRITERION_WEIGHTS
from typing import Dict, List

CONCEPT_MAPPING = {
    "comportamentos": {
        "interrupcao": {
            "microagressoes": {"interrupcoes_constantes": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "questionamento_capacidade": {
            "microagressoes": {"questionar_julgamento": CRITERION_WEIGHTS["behavior"]["critical"]},
            "discriminacao_genero": {"discriminacao_sutil": CRITERION_WEIGHTS["behavior"]["relevant"]}
        },
        "comentarios_saude_mental": {
            "microagressoes": {"comentarios_saude_mental": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "piadas_estereotipos": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "perseguicao": {
            "perseguicao": CRITERION_WEIGHTS["behavior"]["critical"]
        },
        "vigilancia": {
            "perseguicao": CRITERION_WEIGHTS["behavior"]["critical"]
        },
        "exclusao": {
            "discriminacao_genero": {
                "discriminacao_flagrante": CRITERION_WEIGHTS["behavior"]["critical"],
                "discriminacao_sutil": CRITERION_WEIGHTS["behavior"]["relevant"]
            }
        },
        "ameaca": {
            "abuso_psicologico": CRITERION_WEIGHTS["behavior"]["critical"],
            "perseguicao": CRITERION_WEIGHTS["behavior"]["relevant"]
        },
        "constrangimento": {
            "abuso_psicologico": CRITERION_WEIGHTS["behavior"]["critical"]
        },
        "humilhacao": {
            "abuso_psicologico": CRITERION_WEIGHTS["behavior"]["critical"],
            "assedio_moral_genero": CRITERION_WEIGHTS["behavior"]["relevant"]
        },
        "pressao_tarefas": {
            "assedio_moral_genero": CRITERION_WEIGHTS["behavior"]["critical"]
        },
        "natureza_sexual_nao_consentido": {
            "violencia_sexual": {"assedio_sexual": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "contato_fisico_nao_consentido": {
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "ato_obsceno": {
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "coercao_sexual": {
            "violencia_sexual": {"estupro": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "comentarios_sobre_peso": {
            "gordofobia": {"discriminacao_direta": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "piadas_sobre_peso": {
            "gordofobia": {"discriminacao_direta": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "exclusao_por_peso": {
            "gordofobia": {"discriminacao_estrutural": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "negacao_acessibilidade": {
            "capacitismo": {"barreiras_fisicas": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "infantilizacao": {
            "capacitismo": {"barreiras_atitudinais": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "cyberbullying": {
            "violencia_digital": {"cyberbullying": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "mensagens_ofensivas": {
            "violencia_digital": {"cyberbullying": CRITERION_WEIGHTS["behavior"]["relevant"]}
        },
        "exposicao_conteudo": {
            "violencia_digital": {"exposicao_nao_consentida": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "zombaria_religiao": {
            "discriminacao_religiosa": {"ofensa_direta": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "impedimento_pratica_religiosa": {
            "discriminacao_religiosa": {"discriminacao_institucional": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "discriminacao_origem": {
            "xenofobia": {"xenofobia_internacional": CRITERION_WEIGHTS["behavior"]["critical"]}
        },
        "piada_sotaque": {
            "xenofobia": {"discriminacao_regional": CRITERION_WEIGHTS["behavior"]["critical"]}
        }
    },
    "frequencia": {
        "unica_vez": {
            "violencia_sexual": {
                "estupro": CRITERION_WEIGHTS["frequency"]["single"], 
                "importunacao_sexual": CRITERION_WEIGHTS["frequency"]["single"],
                "assedio_sexual": CRITERION_WEIGHTS["frequency"]["single"]
            },
            "discriminacao_genero": {"discriminacao_flagrante": CRITERION_WEIGHTS["frequency"]["single"]}
        },
        "algumas_vezes": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["frequency"]["few"],
                "estereotipos": CRITERION_WEIGHTS["frequency"]["few"],
                "comentarios_saude_mental": CRITERION_WEIGHTS["frequency"]["few"]
            },
            "violencia_sexual": {"assedio_sexual": CRITERION_WEIGHTS["frequency"]["few"]}
        },
        "repetidamente": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["frequency"]["repeated"],
                "questionar_julgamento": CRITERION_WEIGHTS["frequency"]["repeated"],
                "estereotipos": CRITERION_WEIGHTS["frequency"]["repeated"]
            },
            "perseguicao": CRITERION_WEIGHTS["frequency"]["repeated"],
            "discriminacao_genero": {"discriminacao_sutil": CRITERION_WEIGHTS["frequency"]["repeated"]},
            "abuso_psicologico": CRITERION_WEIGHTS["frequency"]["repeated"],
            "violencia_digital": {"cyberbullying": CRITERION_WEIGHTS["frequency"]["repeated"]}
        },
        "continuamente": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["frequency"]["continuous"],
                "questionar_julgamento": CRITERION_WEIGHTS["frequency"]["continuous"]
            },
            "perseguicao": CRITERION_WEIGHTS["frequency"]["continuous"],
            "discriminacao_genero": {"discriminacao_sutil": CRITERION_WEIGHTS["frequency"]["continuous"]},
            "abuso_psicologico": CRITERION_WEIGHTS["frequency"]["continuous"],
            "assedio_moral_genero": CRITERION_WEIGHTS["frequency"]["continuous"],
            "xenofobia": {"discriminacao_regional": CRITERION_WEIGHTS["frequency"]["continuous"]}
        }
    },
    "contexto": {
        "sala_aula": {
            "microagressoes": {"interrupcoes_constantes": CRITERION_WEIGHTS["context"]["relevant"]},
            "capacitismo": {"barreiras_fisicas": CRITERION_WEIGHTS["context"]["relevant"]}
        },
        "ambiente_administrativo": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["context"]["relevant"],
                "questionar_julgamento": CRITERION_WEIGHTS["context"]["relevant"]
            }
        },
        "local_trabalho": {
            "assedio_moral_genero": CRITERION_WEIGHTS["context"]["critical"],
            "microagressoes": {"questionar_julgamento": CRITERION_WEIGHTS["context"]["relevant"]}
        },
        "espaco_publico_campus": {
            "perseguicao": CRITERION_WEIGHTS["context"]["supporting"],
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["context"]["relevant"]},
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["context"]["supporting"]}
        },
        "ambiente_online": {
            "perseguicao": CRITERION_WEIGHTS["context"]["supporting"],
            "violencia_digital": {
                "cyberbullying": CRITERION_WEIGHTS["context"]["critical"],
                "exposicao_nao_consentida": CRITERION_WEIGHTS["context"]["critical"]
            }
        },
        "redes_sociais": {
            "violencia_digital": {
                "cyberbullying": CRITERION_WEIGHTS["context"]["critical"],
                "exposicao_nao_consentida": CRITERION_WEIGHTS["context"]["critical"]
            }
        },
        "evento_academico": {
            "microagressoes": {"interrupcoes_constantes": CRITERION_WEIGHTS["context"]["relevant"]},
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["context"]["supporting"]}
        },
        "ambiente_social": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["context"]["relevant"]},
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["context"]["supporting"]},
            "gordofobia": {"discriminacao_direta": CRITERION_WEIGHTS["context"]["relevant"]}
        },
        "local_culto_religioso": {
            "discriminacao_religiosa": {
                "ofensa_direta": CRITERION_WEIGHTS["context"]["critical"],
                "discriminacao_institucional": CRITERION_WEIGHTS["context"]["critical"]
            }
        }
    },
    "caracteristicas_alvo": {
        "genero": {
            "microagressoes": {"interrupcoes_constantes": CRITERION_WEIGHTS["target"]["relevant"]},
            "discriminacao_genero": {
                "discriminacao_flagrante": CRITERION_WEIGHTS["target"]["critical"],
                "discriminacao_sutil": CRITERION_WEIGHTS["target"]["critical"]
            },
            "assedio_moral_genero": CRITERION_WEIGHTS["target"]["critical"]
        },
        "orientacao_sexual": {
            "discriminacao_genero": {
                "discriminacao_flagrante": CRITERION_WEIGHTS["target"]["critical"],
                "discriminacao_sutil": CRITERION_WEIGHTS["target"]["critical"]
            }
        },
        "raca_etnia": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["target"]["relevant"],
                "estereotipos": CRITERION_WEIGHTS["target"]["relevant"]
            }
        },
        "condicao_financeira": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["target"]["supporting"]}
        },
        "deficiencia": {
            "microagressoes": {
                "interrupcoes_constantes": CRITERION_WEIGHTS["target"]["relevant"],
                "estereotipos": CRITERION_WEIGHTS["target"]["relevant"]
            },
            "capacitismo": {
                "barreiras_fisicas": CRITERION_WEIGHTS["target"]["critical"],
                "barreiras_atitudinais": CRITERION_WEIGHTS["target"]["critical"]
            }
        },
        "aparencia_fisica": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["target"]["supporting"]},
            "gordofobia": {"discriminacao_direta": CRITERION_WEIGHTS["target"]["critical"]}
        },
        "peso_corporal": {
            "gordofobia": {
                "discriminacao_direta": CRITERION_WEIGHTS["target"]["critical"],
                "discriminacao_estrutural": CRITERION_WEIGHTS["target"]["critical"]
            }
        },
        "origem_regional": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["target"]["supporting"]},
            "xenofobia": {
                "discriminacao_regional": CRITERION_WEIGHTS["target"]["critical"],
                "xenofobia_internacional": CRITERION_WEIGHTS["target"]["relevant"]
            }
        },
        "origem_estrangeira": {
            "xenofobia": {"xenofobia_internacional": CRITERION_WEIGHTS["target"]["critical"]}
        },
        "desempenho_academico": {
            "microagressoes": {"questionar_julgamento": CRITERION_WEIGHTS["target"]["supporting"]}
        },
        "religiao": {
            "discriminacao_religiosa": {
                "ofensa_direta": CRITERION_WEIGHTS["target"]["critical"],
                "discriminacao_institucional": CRITERION_WEIGHTS["target"]["critical"]
            }
        }
    },
    "relacionamento": {
        "relacao_hierarquica": {
            "abuso_psicologico": CRITERION_WEIGHTS["relationship"]["hierarchical"],
            "assedio_moral_genero": CRITERION_WEIGHTS["relationship"]["hierarchical"]
        },
        "colega": {
            "microagressoes": {"questionar_julgamento": CRITERION_WEIGHTS["relationship"]["peer"]}
        },
        "desconhecido": {
            "perseguicao": CRITERION_WEIGHTS["relationship"]["unknown"],
            "violencia_sexual": {"importunacao_sexual": CRITERION_WEIGHTS["relationship"]["unknown"]}
        },
        "ex_relacionamento": {
            "perseguicao": CRITERION_WEIGHTS["relationship"]["ex_partner"]
        }
    },
    "impacto": {
        "constrangimento": {
            "microagressoes": {"estereotipos": CRITERION_WEIGHTS["impact"]["mild"]},
            "violencia_sexual": {
                "assedio_sexual": CRITERION_WEIGHTS["impact"]["moderate"],
                "importunacao_sexual": CRITERION_WEIGHTS["impact"]["moderate"]
            },
            "discriminacao_religiosa": {"ofensa_direta": CRITERION_WEIGHTS["impact"]["moderate"]}
        },
        "impacto_participacao": {
            "microagressoes": {"interrupcoes_constantes": CRITERION_WEIGHTS["impact"]["moderate"]},
            "gordofobia": {"discriminacao_estrutural": CRITERION_WEIGHTS["impact"]["strong"]}
        },
        "danos_emocionais": {
            "microagressoes": {"comentarios_saude_mental": CRITERION_WEIGHTS["impact"]["strong"]},
            "abuso_psicologico": CRITERION_WEIGHTS["impact"]["critical"],
            "assedio_moral_genero": CRITERION_WEIGHTS["impact"]["strong"],
            "violencia_sexual": {"estupro": CRITERION_WEIGHTS["impact"]["critical"]},
            "violencia_digital": {"exposicao_nao_consentida": CRITERION_WEIGHTS["impact"]["critical"]}
        },
        "limitacao_liberdade": {
            "perseguicao": CRITERION_WEIGHTS["impact"]["strong"],
            "capacitismo": {"barreiras_fisicas": CRITERION_WEIGHTS["impact"]["critical"]}
        },
        "prejuizo_desempenho": {
            "microagressoes": {"questionar_julgamento": CRITERION_WEIGHTS["impact"]["moderate"]},
            "discriminacao_genero": {
                "discriminacao_sutil": CRITERION_WEIGHTS["impact"]["strong"],
                "discriminacao_flagrante": CRITERION_WEIGHTS["impact"]["strong"]
            },
            "assedio_moral_genero": CRITERION_WEIGHTS["impact"]["strong"]
        },
        "medo_inseguranca": {
            "perseguicao": CRITERION_WEIGHTS["impact"]["strong"],
            "violencia_sexual": {
                "importunacao_sexual": CRITERION_WEIGHTS["impact"]["strong"],
                "estupro": CRITERION_WEIGHTS["impact"]["critical"]
            },
            "xenofobia": {"xenofobia_internacional": CRITERION_WEIGHTS["impact"]["strong"]}
        },
        "violacao_privacidade": {
            "violencia_sexual": {
                "assedio_sexual": CRITERION_WEIGHTS["impact"]["strong"],
                "importunacao_sexual": CRITERION_WEIGHTS["impact"]["strong"],
                "estupro": CRITERION_WEIGHTS["impact"]["critical"]
            },
            "violencia_digital": {"exposicao_nao_consentida": CRITERION_WEIGHTS["impact"]["critical"]}
        },
        "exposicao_indesejada": {
            "violencia_digital": {"exposicao_nao_consentida": CRITERION_WEIGHTS["impact"]["critical"]}
        },
        "limitacao_acesso": {
            "capacitismo": {"barreiras_fisicas": CRITERION_WEIGHTS["impact"]["critical"]}
        },
        "discriminacao_identidade": {
            "discriminacao_religiosa": {"ofensa_direta": CRITERION_WEIGHTS["impact"]["strong"]},
            "xenofobia": {"xenofobia_internacional": CRITERION_WEIGHTS["impact"]["strong"]}
        }
    }
}

KEYWORD_DESCRIPTIONS = {
    # action_type
    "interrupcao": "Identificada quando há dúvidas explícitas sobre a competência da pessoa baseadas em características pessoais",
    "questionamento_capacidade": "Identificada quando há comentários ou questionamentos sobre a capacidade de alguém.",
    "comentarios_saude_mental": "Identificada quando há comentários ou piadas sobre a saúde mental de alguém.",
    "piadas_estereotipos": "Identificada quando há piadas ou comentários que reforçam estereótipos negativos.",
    "perseguicao": "Identificada quando há comportamentos de vigilância ou perseguição.",
    "exclusao": "Identificada quando há exclusão de alguém de atividades ou grupos.",
    "ameaca": "Identificada quando há ameaças explícitas ou implícitas.",
    "constrangimento": "Identificada quando alguém é colocado em uma situação embaraçosa ou desconfortável.",
    "humilhacao": "Identificada quando alguém é tratado de forma desrespeitosa ou degradante.",
    "pressao_tarefas": "Identificada quando há pressão excessiva para cumprir tarefas ou obrigações.",
    "natureza_sexual_nao_consentido": "Identificada quando há comentários ou comportamentos de natureza sexual sem consentimento.",
    "contato_fisico_nao_consentido": "Identificada quando há contato físico sem consentimento.",
    "ato_obsceno": "Identificada quando há comportamentos ou expressões obscenas.",
    "coercao_sexual": "Identificada quando há coerção para relações sexuais.",
    "comentarios_sobre_peso": "Identificada quando há comentários negativos ou piadas sobre o peso de alguém.",
    "exclusao_por_peso": "Identificada quando alguém é excluído ou discriminado com base no peso.",
    "negacao_acessibilidade": "Identificada quando há barreiras físicas ou atitudinais que impedem o acesso de pessoas com deficiência.",
    "infantilizacao": "Identificada quando alguém é tratado de forma condescendente ou infantilizada.",
    "cyberbullying": "Identificada quando há comportamentos de bullying online.",
    "exposicao_conteudo": "Identificada quando há exposição não consensual de conteúdo pessoal ou íntimo.",
    "zombaria_religiao": "Identificada quando há zombarias ou ofensas relacionadas à religião de alguém.",
    "impedimento_pratica_religiosa": "Identificada quando há impedimentos para a prática religiosa de alguém.",
    "discriminacao_origem": "Identificada quando há discriminação com base na origem de alguém, seja regional ou estrangeira.",
    "piada_sotaque": "Identificada quando há piadas ou comentários negativos sobre o sotaque de alguém.",
    "insulto": "Identificada quando há insultos ou ofensas direcionadas a alguém.",
    "insulto_racial": "Identificada quando há insultos ou ofensas com base na raça ou etnia de alguém.",
    # frequency
    "unica_vez": "Identificada quando o comportamento ocorre uma única vez.",
    "algumas_vezes": "Identificada quando o comportamento ocorre algumas vezes, mas não de forma recorrente.",
    "repetidamente": "Identificada quando o comportamento ocorre de forma repetitiva, mas não contínua.",
    "continuamente": "Identificada quando o comportamento ocorre de forma contínua.",
    # context
    "sala_aula": "Identificada quando o comportamento ocorre em um ambiente de sala de aula.",
    "ambiente_administrativo": "Identificada quando o comportamento ocorre em um ambiente administrativo.",
    "local_trabalho": "Identificada quando o comportamento ocorre em um ambiente de trabalho.",
    "espaco_publico_campus": "Identificada quando o comportamento ocorre em um espaço público dentro do campus.",
    "ambiente_online": "Identificada quando o comportamento ocorre em um ambiente online, como redes sociais ou plataformas digitais.",
    "evento_academico": "Identificada quando o comportamento ocorre durante um evento acadêmico, como palestras ou conferências.",
    "ambiente_social": "Identificada quando o comportamento ocorre em um ambiente social, como festas ou encontros informais.",
    "local_culto_religioso": "Identificada quando o comportamento ocorre em um local de culto religioso.",
    # target
    "genero": "Identificada quando o alvo é baseado no gênero de alguém.",
    "orientacao_sexual": "Identificada quando o alvo é baseado na orientação sexual de alguém.",
    "raca_etnia": "Identificada quando o alvo é baseado na raça ou etnia de alguém.",
    "condicao_financeira": "Identificada quando o alvo é baseado na condição financeira de alguém.",
    "deficiencia": "Identificada quando o alvo é baseado na deficiência de alguém.",
    "aparencia_fisica": "Identificada quando o alvo é baseado na aparência física de alguém.",
    "origem_regional": "Identificada quando o alvo é baseado na origem regional de alguém.",
    "origem_estrangeira": "Identificada quando o alvo é baseado na origem estrangeira de alguém.",
    "desempenho_academico": "Identificada quando o alvo é baseado no desempenho acadêmico de alguém.",
    "religiao": "Identificada quando o alvo é baseado na religião de alguém.",
    # relationship
    "relacao_hierarquica": "Identificada quando o relacionamento é baseado em uma hierarquia de poder.",
    "colega": "Identificada quando o relacionamento é baseado na condição de colega.",
    "desconhecido": "Identificada quando o relacionamento é com alguém desconhecido.",
    "ex_relacionamento": "Identificada quando o relacionamento é com um ex-parceiro ou ex-parceira.",
    # impact
    "constrangimento": "Identificada quando o comportamento causa constrangimento a alguém.",
    "impacto_participacao": "Identificada quando o comportamento impacta a participação de alguém.",
    "danos_emocionais": "Identificada quando o comportamento causa danos emocionais a alguém.",
    "limitacao_liberdade": "Identificada quando o comportamento causa limitação da liberdade de alguém.",
    "prejuizo_desempenho": "Identificada quando o comportamento causa prejuízo no desempenho de alguém.",
    "medo_inseguranca": "Identificada quando o comportamento causa medo ou insegurança em alguém.",
    "violacao_privacidade": "Identificada quando o comportamento causa violação da privacidade de alguém.",
    "limitacao_acesso": "Identificada quando o comportamento causa limitação de acesso a recursos ou oportunidades para alguém.",
    "discriminacao_identidade": "Identificada quando o comportamento causa discriminação com base na identidade de alguém.",
}

def extract_keywords_from_violence_types():
    """
    Extrai palavras-chave do dicionário VIOLENCE_TYPES.
    """
    keywords = {
        "action_type": [],
        "behavior": []  # Para comportamentos específicos
    }
    
    # Extrair palavras-chave de cada tipo de violência
    for vtype, vdata in VIOLENCE_TYPES.items():
        # Extrair do tipo principal
        if "palavras_chave" in vdata:
            keywords["action_type"].extend(vdata["palavras_chave"])
        
        # Extrair dos subtipos
        if "subtipos" in vdata:
            for subtype, subdata in vdata["subtipos"].items():
                if "palavras_chave" in subdata:
                    keywords["action_type"].extend(subdata["palavras_chave"])
                if "comportamentos" in subdata:
                    keywords["behavior"].extend(subdata["comportamentos"])
    
    return keywords

def extract_keywords_from_concept_mapping():
    """
    Extrai palavras-chave do CONCEPT_MAPPING.
    """
    keywords = {
        "action_type": [],
        "frequency": [],
        "context": [],
        "target": [],
        "relationship": [],
        "impact": []
    }
    
    # Mapeamento entre categorias de conceito e campos de formulário
    concept_to_field = {
        "comportamentos": "action_type",
        "frequencia": "frequency",
        "contexto": "context",
        "caracteristicas_alvo": "target",
        "relacionamento": "relationship",
        "impacto": "impact"
    }
    
    # Extrair chaves como palavras-chave
    for concept, mappings in CONCEPT_MAPPING.items():
        field = concept_to_field.get(concept)
        if field and field in keywords:
            keywords[field].extend(mappings.keys())
    
    return keywords

def build_keywords_dictionary():
    """
    Constrói o dicionário simplificado de palavras-chave usando apenas as keywords permitidas.
    """
    keywords = {
        "action_type": [
            "interrupcao", "questionamento_capacidade", "comentarios_saude_mental",
            "piadas_estereotipos", "perseguicao", "exclusao", "ameaca",
            "constrangimento", "humilhacao", "pressao_tarefas",
            "natureza_sexual_nao_consentido", "contato_fisico_nao_consentido",
            "ato_obsceno", "coercao_sexual", "comentarios_sobre_peso",
            "exclusao_por_peso", "negacao_acessibilidade", "infantilizacao",
            "cyberbullying", "exposicao_conteudo", "zombaria_religiao",
            "impedimento_pratica_religiosa", "discriminacao_origem",
            "piada_sotaque", "insulto", "insulto_racial"
        ],
        "frequency": [
            "unica_vez", "algumas_vezes", "repetidamente", "continuamente"
        ],"interrupcao": "Identificada quando há padrão de cortar a fala de alguém de forma repetitiva",
        "context": [
            "sala_aula", "ambiente_administrativo", "local_trabalho",
            "espaco_publico_campus", "ambiente_online", "evento_academico",
            "ambiente_social", "local_culto_religioso"
        ],
        "target": [
            "genero", "orientacao_sexual", "raca_etnia", "condicao_financeira",
            "deficiencia", "aparencia_fisica", "origem_regional", 
            "origem_estrangeira", "desempenho_academico", "religiao"
        ],
        "relationship": [
            "relacao_hierarquica", "colega", "desconhecido", "ex_relacionamento"
        ],
        "impact": [
            "constrangimento", "impacto_participacao", "danos_emocionais",
            "limitacao_liberdade", "prejuizo_desempenho", "medo_inseguranca",
            "violacao_privacidade", "limitacao_acesso", "discriminacao_identidade"
        ]
    }
    
    return keywords

# Construir e exportar o dicionário de palavras-chave
KEYWORDS_DICT = build_keywords_dictionary()