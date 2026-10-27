from funcoes_pertinencia import (
    tempo_rapido, tempo_medio, tempo_lento,
    cordialidade_baixa, cordialidade_media, cordialidade_alta,
)

NOTA_EXCELENTE = 9
NOTA_BOA = 7
NOTA_REGULAR = 5
NOTA_RUIM = 2


def avaliar_atendimento(tempo, cordialidade):
    """
    Regras:
    1. rapido E alta   -> EXCELENTE
    2. rapido E media  -> BOA
    3. medio  E alta   -> BOA
    4. medio  E media  -> REGULAR
    5. caso contrario  -> RUIM
    O conectivo E usa MIN e regras de mesma saida sao unidas com MAX.
    """
    t_rapido = tempo_rapido(tempo)
    t_medio = tempo_medio(tempo)
    t_lento = tempo_lento(tempo)

    c_baixa = cordialidade_baixa(cordialidade)
    c_media = cordialidade_media(cordialidade)
    c_alta = cordialidade_alta(cordialidade)

    excelente = min(t_rapido, c_alta)
    boa = max(min(t_rapido, c_media), min(t_medio, c_alta))
    regular = min(t_medio, c_media)
    ruim = max(
        min(t_lento, c_baixa), min(t_lento, c_media), min(t_lento, c_alta),
        min(t_rapido, c_baixa), min(t_medio, c_baixa),
    )

    soma = excelente + boa + regular + ruim
    qualidade_final = (
        excelente * NOTA_EXCELENTE + boa * NOTA_BOA
        + regular * NOTA_REGULAR + ruim * NOTA_RUIM
    ) / max(soma, 0.001)

    return {
        "excelente": excelente,
        "boa": boa,
        "regular": regular,
        "ruim": ruim,
        "qualidade_final": qualidade_final,
    }
