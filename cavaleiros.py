"""Implemente um sistema em Python para representar
personagens do universo dos Cavaleiros do Zodíaco,
utilizando herança múltipla. Crie uma classe Personagem
com os atributos nome e constelacao, e métodos como
apresentar(). Crie também duas classes auxiliares:
CavaleiroDeBronze com o atributo poder_de_luta e um
método golpe_especial(), e CavaleiroDeOuro com o atributo
casa_do_zodiaco e um método defender_casa(). Em
seguida, implemente a classe CavaleiroHibrido, que herda
tanto de CavaleiroDeBronze quanto de CavaleiroDeOuro,
combinando os comportamentos de ambas. O programa deve
oferecer um menu interativo no console com as opções de
cadastrar personagens, listar todos os personagens, executar
os golpes especiais ou defesas, e encerrar o programa.
Explore o uso da herança múltipla e do polimorfismo para
definir o comportamento de cada tipo de cavaleiro."""

class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao
    
    def apresentar(self):
        print(f"\n Cavaleiro {self.nome} da constelação {self.constelacao}.")

class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"\n Cavalheiro {self.nome} executa o {self.poder_de_luta} ")

class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zodiaco = casa_do_zodiaco

    def defender_casa(self):
        print(f"\n Cavalheiro {self.nome} da constelação {self.constelacao} defende a casa de {self.casa_do_zodiaco}")

class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        CavaleiroDeBronze.__init__(self, nome, constelacao, poder_de_luta)
        CavaleiroDeOuro.__init__(self, casa_do_zodiaco)

    def golpe_especial(self):
        print(f"\n Cavalheiro {self.nome} executa o {self.poder_de_luta} ")
    def defender_casa(self):
        print(f"\n Cavalheiro {self.nome} da constelação {self.constelacao} defende a casa de {self.casa_do_zodiaco}")

def main():
    personagens = []

    while True:
        print("\n===MENU===")
        print("\n1 - Cadastrar personagens")
        print("2 - Listar personagens")
        print("3 - Executar os golpes especiais ou defesas ")
        print("4 - Sair\n")


        escolha = input("Escolha uma opção (1-4):")


        if escolha == "1":

          print("\n Cadastrar")
          print("1 - Cavaleiro De Bronze")
          print("2 - Cavaleiro De Ouro")
          print("3 - Cavaleiro Hibrido")

          tipo = input("\nTipo de personagem: ")
          nome = input("\n Nome: ")
          constelacao = input("Constelação: ")

          if tipo == 1:
              poder_de_luta = input ("Nome do poder de luta: " )
              personagem = CavaleiroDeBronze(nome, constelacao, poder_de_luta)
              #personagens.append(cavaleiroDeBronze) Aqui seria uma outra opção viável
              #print("\n  Cavaleiro de Bronze cadastrado com sucesso")

          elif tipo == 2:
              casa_do_zodiaco = input ("Casa do Zodíaco: " )
              personagem = CavaleiroDeOuro (nome, constelacao, casa_do_zodiaco)
              #personagens.append(cavaleiroDeOuro)
              #print("\n  Cavaleiro de Ouro cadastrado com sucesso")
          elif tipo == 3 :
              poder_de_luta = input ("Nome do poder de luta: " )
              casa_do_zodiaco = input ("Casa do Zodíaco: " )
              personagem = CavaleiroDeOuro (nome, constelacao, poder_de_luta, casa_do_zodiaco)
              #personagens.append(cavaleiroDeOuro)
              #print("\n  Cavaleiro de Ouro cadastrado com sucesso")
          else:
              print("Opção Inválida!")
              continue
          
          personagens.append(personagem)
          print("\n  Cavaleiro cadastrado com sucesso")
          
        elif escolha =="2":
            if not personagens:
             print("Nenhum personagem cadastrado!")
            else:
                print("\n==Personagens cadastrados:==")
                
                for p in personagens:
                    p.apresentar()

                      
        elif escolha =="3":
            if not personagens:
             print("Nenhum personagem cadastrado!")
            else:
                print("\n==Habilidade:==")
                
                for p in personagens:
                    print(f"\n{p.nome}: ")
                    if isinstance (p, CavaleiroDeBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()

            
            
        elif escolha =="4":
          print("\nSaindo do Programa. Até mais!")
          break
        else:
            print("\nOpção Inválida!")




if __name__ == "__main__":
  main()


     
