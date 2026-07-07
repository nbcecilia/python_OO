class Livro:
    def __init__(self,titulo, autor, id_livro):
      self.__titulo = titulo
      self.__autor = autor
      self.__id_livro = id_livro
   
    def get_titulo(self):
        return  self.__titulo
    def get_autor(self):
        return  self.__autor
    def get_id_livro(self):
        return  self.__id_livro
   
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    def set_autor(self, novo_autor):
        self.__autor = novo_autor
    def set_id_livro(self, novo_id):
        self.__id_livro = novo_id


class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []
   
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula


    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula


    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"\n{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'\n")
    def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return
        print(f"\n{self.__nome} não possui com ID '{id_livro}'.\n")


    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\n Nenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados:")
            for livro in self.__livros_emprestados:
                print(f"\n{livro.get_titulo()}({livro.get_id_livro()})")
            print()


def main():
    livros = []
    usuario = None

    while True:
     print("\n[ MENU ]")
     print("1 - Cadastrar livro")
     print("2 - Cadastrar Usuário")
     print("3 - Emprestar Livro")
     print("4 - Devolver Livro ")
     print("5 - Listar livros")
     print("6 - Sair")

     opcao = input("\nEscolha uma opção: ")

     if opcao == "1":
        titulo = input("\nTítulo do livro:")  
        autor = input("\nAutor do livro:")  
        id_livro = int(input("\nID:"))  

        livro = Livro(titulo, autor, id_livro)
        livros.append(livro)

        print(f"Livro '{titulo}' cadastrado com sucesso!")
    
     elif opcao == "2":
        nome = input("\nDigite o nome:")  
        matricula = int(input("\nDigite a matrícula:")) 

        usuario = Usuario(nome, matricula)   
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    
     elif opcao == "3":
        if usuario is None:
         print("Cadastre um usuário primeiro!")

        elif len(livros) == 0:
         print("Nenhum livro cadastrado!")

        else:
         id_livro = int(input("Digite o ID do livro: "))

         for livro in livros:
            if livro.get_id_livro() == id_livro:
                usuario.emprestar_livro(livro)
                livros.remove(livro)
                
            else:
              print("Livro não encontrado.")
    
     elif opcao == "4":
        if usuario is None:
         print("Cadastre um usuário primeiro!")
        else:
         id_livro = int(input("Digite o ID do livro: "))
         usuario.devolver_livro(id_livro)

     elif opcao == "5":
        if usuario is None:
         print("Cadastre um usuário primeiro!")
        else:
         usuario.listar_livros_emprestados()

     elif opcao == "6":
        print("\nObrigado por usar nosso sistema.")
        break
    
    else:
       print("\nOpção inválida!")
 
if __name__ == "__main__":
  main()



