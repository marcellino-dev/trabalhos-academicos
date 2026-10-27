# Avaliação de Qualidade de Atendimento (Lógica Nebulosa)

Disciplina: Fundamentos da Inteligência Artificial
Unidade: U2 - Métodos e Aplicações de Inteligência Artificial
Aula: A3 - Soluções em Inteligência Artificial

Sistema de decisão fuzzy em Python que avalia a qualidade de um atendimento a partir de:

- Tempo de espera (0 a 60 minutos)
- Cordialidade do atendente (0 a 10)

## Como funciona

- Fuzzificação com funções de pertinência triangulares e trapezoidais (3 por variável)
- 5 regras de inferência, com MIN para o conectivo E e MAX para unir regras de mesma saída
- Defuzzificação por média ponderada (excelente = 9, boa = 7, regular = 5, ruim = 2)

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| `funcoes_pertinencia.py` | funções de pertinência de tempo e cordialidade |
| `regras.py` | regras de inferência e defuzzificação (`avaliar_atendimento`) |
| `graficos.py` | gráficos das funções de pertinência e da superfície de qualidade |
| `app.py` | executa os 4 casos de teste e exibe os gráficos |
| `test_atendimento.py` | testes unitários |
| `Avaliacao_de_Qualidade_de_Atendimento.ipynb` | versão para Google Colab |
| `Avaliacao_de_Qualidade_de_Atendimento_Fuzzy.docx` | relatório da aula prática |

## Como executar

```bash
pip install -r requirements.txt
python app.py
python app.py --sem-graficos
python -m unittest -v
```

## Tecnologias

- Python 3
- NumPy
- Matplotlib
