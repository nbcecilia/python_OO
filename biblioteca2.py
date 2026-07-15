class Autor:
   def __init__(self, nome, nacionalidade):
      self.nome = nome
      self.nacionalidade = nacionalidade
   
#ideal é fazer o encapsulamento em todos

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor #relaçao de agregaçao(com a classe autor)

class Biblioteca:
    def __init__(self,nome):
      self.nome = nome
      self.livros = [] #relaçao de composição (blioteca e livro)
    
    def criar_livro(self, titulo, ano, autor):
     livro = Livro(titulo,ano, autor)
     self.livros.append(livro)
     return livro
    
    def listar_livros(self):
       print(f"\n Livros disponíveis na biblioteca '{self.nome}': ")
       for livro in self.livros:
          print(f"titulo: {livro.titulo}, Ano{livro.ano}. Autor: {livro.autor.nome}({livro.autor.nacionalidade})")
       print()

class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca #relação de associação(cjto de usuario nao forma biblioteca, se associam)
    
    def pegar_emprestado(self, livro):
       if livro in self.biblioteca.livros:
          print(f"\n{self.nome} pegou emprestadp o livro {livro.titulo}.")
       else:
          print(f"\nLivro '{livro.titulo}' não está disponível.")

def main():
   autor1 = Autor("Machado de Assis", "Brasileiro")
   autor2 = Autor("Michael Sandel", "Americano")

   biblioteca = Biblioteca("Biblioteca do IFB")

   livro1 = biblioteca.criar_livro("Dom Casmurro", 1899, autor1)
   livro2 = biblioteca.criar_livro("Justica", 2011, autor2)
   
   biblioteca.listar_livros()

   usuario = Usuario("Carlos", biblioteca)

   usuario.pegar_emprestado(livro1)
   usuario.pegar_emprestado(livro2)

   #usuario.pegar_emprestado(Livro{"A Trança do Rei Careca", 2020, autor1}) 
   #criou-se o livro dentro do parametro(nao usual)


if __name__ == "__main__":
  main()

