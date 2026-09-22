package br.edu.produto;

public class Principal {

    public static void main(String[] args) {

        // Objeto criado com o construtor padrão
        Produto produto1 = new Produto();

        // Objetos criados com o construtor com parâmetros (sobrecarga)
        Produto produto2 = new Produto("Teclado Mecânico", 250.90);
        Produto produto3 = new Produto("Mouse Gamer", 120.50);

        // Exibindo os dados de cada produto
        produto1.exibirDados();
        produto2.exibirDados();
        produto3.exibirDados();

        // Exibindo a quantidade total de produtos cadastrados (método estático)
        Produto.exibirQuantidadeTotal();
    }
}