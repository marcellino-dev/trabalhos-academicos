package br.edu.operacoes;

public abstract class OperacaoMatematica {

    // Método abstrato: cada subclasse deve implementar sua própria lógica de cálculo
    public abstract double calcular(double a, double b) throws Exception;
}
