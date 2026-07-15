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
    def __init__(self,nome): #uncionarios nao precisa esta no paramentro ppois é uma lista vazia
     self.nome = nome
     self.funcionarios= []
   
    def adicionar_funcionários(self,funcionario):
       self.funcionarios.append(funcionario)
       
    def listar_funcionarios(self):
       if not self.funcionarios:
          print("Nenhum funcionario neste departamento")
       else:
          for f in self.funcionarios:
             print(f"{f.nome} - R$ {f.salario:.2f}")
    def media_salarial(self):
       if not self.funcionarios:
        return 0
       soma = 0
       for f in self.funcionarios:
          soma += f.salario
          return soma / len (self.funcionarios)
       

def main():
    funcionarios= []
    departamentos = []
    

    while True:
        print("\n===MENU===")
        print("\n1 - Criar funcionario")
        print("2 - Criar departamento")
        print("3 - Adicionar funcionários ao departamento")
        print("4 - Listar funcionários")
        print("5 - Mostrar média salarial")
        print("6- Sair\n")


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