package br.edu.operacoes;

public class DivisaoPorZeroException extends Exception {

    // Construtor com mensagem personalizada
    public DivisaoPorZeroException() {
        super("Não é possível dividir por zero.");
    }
}
