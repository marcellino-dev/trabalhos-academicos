import argparse

import matplotlib.pyplot as plt

from graficos import plotar_funcoes_pertinencia, plotar_superficie_qualidade
from regras import avaliar_atendimento

CASOS_TESTE = [
    {"tempo": 8, "cordialidade": 9, "descricao": "Atendimento rápido e muito cordial"},
    {"tempo": 15, "cordialidade": 6, "descricao": "Atendimento médio"},
    {"tempo": 35, "cordialidade": 3, "descricao": "Atendimento demorado e pouco cordial"},
    {"tempo": 12, "cordialidade": 8, "descricao": "Bom atendimento geral"},
]


def testar_sistema():
    print("=== TESTE DO SISTEMA DE LÓGICA NEBULOSA ===\n")

    for i, caso in enumerate(CASOS_TESTE, 1):
        resultado = avaliar_atendimento(caso["tempo"], caso["cordialidade"])

        print(f"Caso {i}: {caso['descricao']}")
        print(f"  Tempo de espera: {caso['tempo']} minutos")
        print(f"  Cordialidade: {caso['cordialidade']}/10")
        print("  Graus de pertinência:")
        print(f"    Excelente: {resultado['excelente']:.2f}")
        print(f"    Boa: {resultado['boa']:.2f}")
        print(f"    Regular: {resultado['regular']:.2f}")
        print(f"    Ruim: {resultado['ruim']:.2f}")
        print(f"  Qualidade final: {resultado['qualidade_final']:.2f}/10\n")


def main():
    parser = argparse.ArgumentParser(description="Avaliação de qualidade de atendimento com lógica nebulosa")
    parser.add_argument("--sem-graficos", action="store_true", help="executa apenas os casos de teste")
    args = parser.parse_args()

    testar_sistema()

    if not args.sem_graficos:
        plotar_funcoes_pertinencia()
        plotar_superficie_qualidade()
        plt.show()


if __name__ == "__main__":
    main()
