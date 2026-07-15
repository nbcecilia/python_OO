"""Implemente uma classe Impressora com o método
imprimir(Documento d), que recebe um objeto da classe
Documento e imprime suas informações na tela. A classe
Documento deve conter os atributos título e conteúdo. A
classe Impressora apenas utiliza o documento, sem manter
uma referência permanente a ele, caracterizando uma relação
de dependência. Desenvolva um programa com um menu
interativo no console que permita criar vários documentos,
visualizar seu conteúdo por meio da impressora e encerrar o
programa."""

class Documento:
    def __init__(self, titulo, conteudo):
     self.__titulo = titulo
     self.__conteudo = conteudo

    def get_titulo(self):
        return  self.__titulo
    def get_conteudo(self):
        return  self.__conteudo
   
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo

class Impressora:

    def imprimir(self, documento):
     print("\nImpressão documento")
     print(f"Titulo: {documento.get._titulo()}")
     print(f"Conteudo")
     print(f"{documento.get._conteudo()}")
   

def main():
    documentos = []
    impressora = Impressora()

    while True:
        print("\n===MENU===")
        print("\n1 - Criar novo documento")
        print("2 - Listar documento")
        print("3 - Imprimir documento")
        print("4 - Sair\n")


        escolha = input("Escolha uma opção:")


        if escolha == "1":
              titulo = input("Titulo: ")
              conteudo = input("Conteudo: ")

              doc=  Documento(titulo, conteudo)#objeto da classe documento
              documentos.append(doc)
              print("Documento criado com sucesso!")

        elif escolha =="2":
           if not documentos:
              print("\nNenhum documento foi criado!")
           else:
              print("\n===Lista de documentos===")
              for i, doc in enumerate(documentos):
                 print(f"{i+1}.{doc.get_titulo()}")
              print()
           
        elif escolha =="3":
           if not documentos:
              print("Nenhum documento disponível para impressão.")
           else:
              print("\nEscolha o número do documento para imprimir")
              for i, doc in enumerate(documentos):
                 print(f"{i+1}.{doc.get_titulo()}")
              escolha = input("Número: ")
              if escolha.isdigit():
                 escolha = int(escolha)
                 if 1<= escolha <=len(documentos):
                    impressora.imprimir(documentos{escolha-1})
                 else:
                    print("\n Numero Invalido!")
              else:
                 print("Entrada Inválida.")
              print()          
        elif escolha =="4":
          print("\nEncerrando do Programa. Até mais!")
          break
        else:
            print("\nOpção Inválida!")




if __name__ == "__main__":
  main()