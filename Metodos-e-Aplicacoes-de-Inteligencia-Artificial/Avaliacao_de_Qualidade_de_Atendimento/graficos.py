import numpy as np
import matplotlib.pyplot as plt

from funcoes_pertinencia import (
    tempo_rapido, tempo_medio, tempo_lento,
    cordialidade_baixa, cordialidade_media, cordialidade_alta,
)
from regras import avaliar_atendimento


def plotar_funcoes_pertinencia():
    tempos = np.linspace(0, 60, 200)
    cordialidades = np.linspace(0, 10, 200)

    fig, (ax_tempo, ax_cord) = plt.subplots(1, 2, figsize=(12, 4.5))

    ax_tempo.plot(tempos, [tempo_rapido(t) for t in tempos], "g-", label="Rápido", linewidth=2)
    ax_tempo.plot(tempos, [tempo_medio(t) for t in tempos], "y-", label="Médio", linewidth=2)
    ax_tempo.plot(tempos, [tempo_lento(t) for t in tempos], "r-", label="Lento", linewidth=2)
    ax_tempo.set(title="Tempo de Espera", xlabel="Minutos", ylabel="Grau de Pertinência")

    ax_cord.plot(cordialidades, [cordialidade_baixa(c) for c in cordialidades], "r-", label="Baixa", linewidth=2)
    ax_cord.plot(cordialidades, [cordialidade_media(c) for c in cordialidades], "y-", label="Média", linewidth=2)
    ax_cord.plot(cordialidades, [cordialidade_alta(c) for c in cordialidades], "g-", label="Alta", linewidth=2)
    ax_cord.set(title="Cordialidade", xlabel="Pontuação (0-10)", ylabel="Grau de Pertinência")

    for ax in (ax_tempo, ax_cord):
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig


def plotar_superficie_qualidade():
    tempos, cordialidades = np.meshgrid(np.linspace(0, 60, 60), np.linspace(0, 10, 60))
    qualidade = np.zeros_like(tempos)

    for i in range(tempos.shape[0]):
        for j in range(tempos.shape[1]):
            qualidade[i, j] = avaliar_atendimento(tempos[i, j], cordialidades[i, j])["qualidade_final"]

    fig, ax = plt.subplots(figsize=(7, 5))
    contorno = ax.contourf(tempos, cordialidades, qualidade, levels=20, cmap="RdYlGn")
    fig.colorbar(contorno, label="Qualidade final (0-10)")
    ax.set(title="Superfície de Qualidade", xlabel="Tempo (min)", ylabel="Cordialidade")
    fig.tight_layout()
    return fig
