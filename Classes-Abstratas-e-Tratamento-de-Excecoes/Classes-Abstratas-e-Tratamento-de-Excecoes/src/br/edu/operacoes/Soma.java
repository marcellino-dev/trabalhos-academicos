package br.edu.operacoes;

public class Soma extends OperacaoMatematica {

    // Implementação do método abstrato: soma os dois valores
    @Override
    public double calcular(double a, double b) throws Exception {
        return a + b;
    }
}
