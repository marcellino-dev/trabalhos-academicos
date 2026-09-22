package br.edu.catalogo;

public class Livro {

    String titulo;
    String autor;
    int anoPublicacao;

    public Livro(String titulo, String autor, int anoPublicacao) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }

    public void exibirInformacoes() {
        System.out.println("Titulo: " + titulo + " | Autor: " + autor + " | Ano: " + anoPublicacao);
    }
}
