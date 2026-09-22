package br.edu.produto;

public class Produto {

    // Atributos de instância
    String nome;
    double preco;

    // Atributo estático (compartilhado entre todos os objetos)
    static int quantidadeTotal = 0;

    // Construtor padrão (sem parâmetros)
    public Produto() {
        this.nome = "Produto sem nome";
        this.preco = 0.0;
        quantidadeTotal++;
    }

    // Construtor com parâmetros (sobrecarga)
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
        quantidadeTotal++;
    }

    // Método de instância para exibir os dados do produto
    public void exibirDados() {
        System.out.println("Nome: " + nome + " | Preço: R$ " + preco);
    }

    // Método estático para exibir a quantidade total de produtos cadastrados
    public static void exibirQuantidadeTotal() {
        System.out.println("Quantidade total de produtos cadastrados: " + quantidadeTotal);
    }
}