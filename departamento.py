"""Desenvolva uma classe Departamento com nome e um vetor
de objetos Funcionario, onde cada funcionário tem nome e
salário, permitindo que funcionários existam
independentemente do departamento para que possam ser
adicionados ou removidos livremente (agregação).
Implemente métodos no Departamento para adicionar
funcionários, calcular a média salarial e listar todos os
funcionários. Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa."""

class Funcionario:
   def __init__(self,nome, salario):
      self.nome = nome
      self.salario = salario


class Departamento:
    def __init__(self,nome, funcionario):
     self.nome = nome
     funcionario = []
   
    def adicionar_funcionários(self):
    
    def remover_funcionario(self):
       
    def calcular_media(self):
       
    def listar_funcionarios(self):

def main():
    
    

    while True:
        print("\n===MENU===")
        print("\n1 - Criar departamento")
        print("2 - Criar funcionários")
        print("3 - Adicionar funcionários ao departamento")
        print("4 - Listar funcionários")
        print("5 - Mostrar média salarial")
        print("5 - Sair\n")


        escolha = input("Escolha uma opção:")


        if escolha == "1":
          
        elif escolha =="2":
         
        elif escolha =="3":
          
        elif escolha =="4":
           
        elif escolha =="5":
          
        elif escolha =="6":
          print("\nSaindo do Programa. Até mais!")
          break
        else:
            print("\nOpção Inválida!")




if __name__ == "__main__":
  main()