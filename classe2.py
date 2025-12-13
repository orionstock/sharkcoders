class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def mostrar_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")


livro1 = Livro("Vingt Mille Lieues Sous Les Mers", "Júlio Verne", 368)
livro2 = Livro("The Great Gatsby", "F. Scott Fitzgerald", 218)
livro3 = Livro("Darkly Dreaming Dexter", "Jeff Lindsay", 288)


class Biblioteca:
    def __init__(self):
        self.colecao = []

    def adicionar_livro(self, livro):
        self.colecao.append(livro)

    def listar_livros(self):
        if not self.colecao:
            print("A biblioteca está vazia.")
        else:
            print("\nLista de Livros na biblioteca")
            for livro in self.colecao:
                livro.mostrar_livro()
                print("\n")

minha_biblioteca = Biblioteca()

minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)

minha_biblioteca.listar_livros()