package br.edu.catalogo;

public class Principal {

    public static void main(String[] args) {

        Livro[] livros = new Livro[5];

        livros[0] = new Livro("Java para Iniciantes", "Carlos Mendes", 2019);
        livros[1] = new Livro("Efetive Java", "Joshua Bloch", 2018);
        livros[2] = new Livro("Clean Code", "Robert Martin", 2008);
        livros[3] = new Livro("Java Concorrente na Pratica", "Brian Goetz", 2006);
        livros[4] = new Livro("O Poder do Habito", "Charles Duhigg", 2012);

        String palavraChave = "Java";

        System.out.println("Livros com '" + palavraChave + "' no titulo:");
        for (Livro livro : livros) {
            if (livro.titulo.contains(palavraChave)) {
                livro.exibirInformacoes();
            }
        }
    }
}
