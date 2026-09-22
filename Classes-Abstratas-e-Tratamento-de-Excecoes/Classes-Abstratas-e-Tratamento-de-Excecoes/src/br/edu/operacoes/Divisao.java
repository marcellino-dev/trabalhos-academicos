package br.edu.operacoes;

public class Divisao extends OperacaoMatematica {

    // Implementação do método abstrato: divide os dois valores,
    // lançando uma exceção personalizada caso o divisor seja zero
    @Override
    public double calcular(double a, double b) throws Exception {
        if (b == 0) {
            throw new DivisaoPorZeroException();
        }
        return a / b;
    }
}
