# Cria um dicionario de aliases para imprimir no main

KEYWORD_ALIASES = {
    # action_type
    "interrupcao": "Interrupção constante",
    "questionamento_capacidade": "Questionamento de capacidade",
    "comentarios_saude_mental": "Comentários sobre saúde mental",
    "piadas_estereotipos": "Piadas e estereótipos",
    "perseguicao": "Perseguição",
    "exclusao": "Exclusão",
    "ameaca": "Ameaça",
    "constrangimento": "Constrangimento",
    "humilhacao": "Humilhação",
    "pressao_tarefas": "Pressão em tarefas",
    "natureza_sexual_nao_consentido": "Comportamento sexual não consentido",
    "contato_fisico_nao_consentido": "Contato físico não consentido",
    "ato_obsceno": "Ato obsceno",
    "coercao_sexual": "Coerção sexual",
    "comentarios_sobre_peso": "Comentários sobre peso",
    "exclusao_por_peso": "Exclusão por peso",
    "negacao_acessibilidade": "Negação de acessibilidade",
    "infantilizacao": "Infantilização",
    "cyberbullying": "Cyberbullying",
    "exposicao_conteudo": "Exposição de conteúdo",
    "zombaria_religiao": "Zombaria religiosa",
    "impedimento_pratica_religiosa": "Impedimento de prática religiosa",
    "discriminacao_origem": "Discriminação por origem",
    "piada_sotaque": "Piada sobre sotaque",
    "insulto": "Insulto",
    "insulto_racial": "Insulto racial",
    
    # frequency
    "unica_vez": "Uma única vez",
    "algumas_vezes": "Algumas vezes",
    "repetidamente": "Repetidamente",
    "continuamente": "Continuamente",
    
    # context
    "sala_aula": "Sala de aula",
    "ambiente_administrativo": "Ambiente administrativo",
    "local_trabalho": "Local de trabalho",
    "espaco_publico_campus": "Espaço público do campus",
    "ambiente_online": "Ambiente online",
    "evento_academico": "Evento acadêmico",
    "ambiente_social": "Ambiente social",
    "local_culto_religioso": "Local de culto religioso",
    
    # target
    "genero": "Gênero",
    "orientacao_sexual": "Orientação sexual",
    "raca_etnia": "Raça/Etnia",
    "condicao_financeira": "Condição financeira",
    "deficiencia": "Deficiência",
    "aparencia_fisica": "Aparência física",
    "origem_regional": "Origem regional",
    "origem_estrangeira": "Origem estrangeira",
    "desempenho_academico": "Desempenho acadêmico",
    "religiao": "Religião",
    
    # relationship
    "relacao_hierarquica": "Relação hierárquica",
    "colega": "Colega",
    "desconhecido": "Desconhecido",
    "ex_relacionamento": "Ex-relacionamento",
    
    # impact
    "constrangimento": "Constrangimento",
    "impacto_participacao": "Impacto na participação",
    "danos_emocionais": "Danos emocionais",
    "limitacao_liberdade": "Limitação da liberdade",
    "prejuizo_desempenho": "Prejuízo no desempenho",
    "medo_inseguranca": "Medo e/ou insegurança",
    "violacao_privacidade": "Violação da privacidade",
    "limitacao_acesso": "Limitação de acesso",
    "discriminacao_identidade": "Discriminação de identidade",
    
    # aliases para tipos de violência que aparecem nas explicações
    "violencia_sexual": "Violência Sexual",
    "estupro": "Estupro",
    "assedio_sexual": "Assédio Sexual",
    "importunacao_sexual": "Importunação Sexual",
    "perseguicao": "Perseguição",
    "abuso_psicologico": "Abuso Psicológico",
    "microagressoes": "Microagressões",
    "discriminacao_genero": "Discriminação de Gênero",
    "capacitismo": "Capacitismo",
    "xenofobia": "Xenofobia",
    "violencia_digital": "Violência Digital",
    "assedio_moral_genero": "Assédio Moral de Gênero",
    "discriminacao_religiosa": "Discriminação Religiosa",
    
    # aliases para frases comuns nas explicações
    "do tipo": "do tipo",
    "comportamentos de": "comportamentos de",
    "em seu relato": "em seu relato",
    "identificamos": "identificamos",
    "causou": "causou",
    "comportamento": "comportamento",
}

def get_keyword_alias(keyword: str) -> str:
    """
    Retorna o alias amigável para uma palavra-chave.
    Se não houver alias, retorna a palavra-chave formatada.
    """
    if keyword in KEYWORD_ALIASES:
        return KEYWORD_ALIASES[keyword]
    
    # Fallback: formatar a palavra-chave removendo underscores e capitalizando
    return keyword.replace("_", " ").title()

def get_category_alias(category: str) -> str:
    """
    Retorna o alias amigável para uma categoria.
    """
    category_aliases = {
        "action_type": "Comportamento",
        "frequency": "Frequência",
        "context": "Local/Contexto",
        "target": "Característica visada",
        "relationship": "Relacionamento",
        "impact": "Impacto"
    }
    
    return category_aliases.get(category, category.replace("_", " ").title())