def tempo_rapido(x):
    if x <= 10:
        return 1.0
    if x <= 20:
        return (20 - x) / 10
    return 0.0


def tempo_medio(x):
    if x <= 10:
        return 0.0
    if x <= 20:
        return (x - 10) / 10
    if x <= 30:
        return (30 - x) / 10
    return 0.0


def tempo_lento(x):
    if x <= 25:
        return 0.0
    if x <= 35:
        return (x - 25) / 10
    return 1.0


def cordialidade_baixa(x):
    if x <= 3:
        return 1.0
    if x <= 5:
        return (5 - x) / 2
    return 0.0


def cordialidade_media(x):
    if x <= 3:
        return 0.0
    if x <= 5:
        return (x - 3) / 2
    if x <= 7:
        return (7 - x) / 2
    return 0.0


def cordialidade_alta(x):
    if x <= 6:
        return 0.0
    if x <= 8:
        return (x - 6) / 2
    return 1.0
