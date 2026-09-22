package br.edu.operacoes;

public class Principal {

    public static void main(String[] args) {

        // Instanciando as operações
        OperacaoMatematica soma = new Soma();
        OperacaoMatematica divisao = new Divisao();

        try {
            // Chamada ao método calcular() da classe Soma
            double resultadoSoma = soma.calcular(10, 5);
            System.out.println("Resultado da soma: " + resultadoSoma);

            // Chamada ao método calcular() da classe Divisao (caso válido)
            double resultadoDivisao = divisao.calcular(10, 2);
            System.out.println("Resultado da divisão: " + resultadoDivisao);

            // Chamada ao método calcular() da classe Divisao (divisão por zero)
            double resultadoDivisaoInvalida = divisao.calcular(10, 0);
            System.out.println("Resultado da divisão: " + resultadoDivisaoInvalida);

        } catch (DivisaoPorZeroException e) {
            System.out.println("Erro: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Ocorreu um erro inesperado: " + e.getMessage());
        }
    }
}
