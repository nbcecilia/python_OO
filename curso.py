"""Implemente em Python um sistema para uma plataforma de
cursos online que utilize herança e polimorfismo,
armazenando os dados em uma lista. Crie uma classe base
chamada Participante, com os atributos nome e email, e um
método emitirCertificado() que retorna uma mensagem
genérica. Em seguida, crie as subclasses Aluno, com o
atributo curso, e Instrutor, com o atributo especialidade,
ambas sobrescrevendo o método emitirCertificado() com
mensagens específicas: o aluno recebe um certificado de
conclusão do curso e o instrutor um certificado de participação
como palestrante. O programa deve conter um menu com as
opções: 1) Cadastrar participante, 2) Listar participantes, 3)
Emitir certificados, e 0) Sair. O usuário deve escolher entre
cadastrar um aluno ou instrutor, e os dados devem ser
armazenados em uma lista de objetos do tipo Participante. O
método emitirCertificado() deve ser chamado de forma
polimórfica para cada participante cadastrado."""

class Participante:
    def __init__(self,nome, email):
       self.__nome = nome
       self.__email = email

    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email

    def emitirCertificado(self):
        #return f"{self.get_nome()} certificado de participação emitido!"
        print(f"{self.get_nome()} certificado de participação emitido!")

class Aluno(Participante):
    def __init__(self, nome, email, curso):
       super().__init__(nome, email)
       self.curso = curso


    def emitirCertificado(self):
        #return f"O aluno {self.get_nome()} concluiu o curso {self.curso} com sucesso!"
        print(f" O aluno {self.get_nome()} recebeu o certificado de conclusão do curso {self.curso}!")


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
       super().__init__(nome, email)
       self.especialidade = especialidade

    def emitirCertificado(self):
        #return f"O instrutor {self.get_nome()} participou como palestrante na area {self.especialidade} com sucesso!"
        print(f" O Instrutor{self.get_nome()} da especilidade {self.especialidade} certificado de participação como palestrante!")

def main():
    """participante = Participante()
    instrutor = Instrutor()
    aluno = Aluno()"""
    participantes = []
    while True:
        print("\n===MENU===")
        print("\n1 - Cadastrar participante")
        print("2 - Listar participantes")
        print("3 - Emitir certificados")
        print("4 - Sair\n")


        escolha = input("Escolha uma opção (1-4):")


        if escolha == "1":
        # while True:
             #print("\nDeseja cadastrar")
             #print("\n1 - Instrutor")
            # print("2 - Aluno")
            # escolha = input("Escolha uma opção (1-2):")
         
             #if escolha == "1":
             # nome = input("\nInforme o nome: ")
              #email = input("\nInforme o email: ")

              #nome.append(instrutor) break

          print("\n Cadastrar")
          print("1 - Aluno")
          print("2 - Instrutor")

          tipo = input("Tipo de participante")
          nome = input("\n Nome: ")
          email = input("Email: ")

          if tipo == 1:
              curso = input ("Curso: " )
              aluno = Aluno(nome, email, curso)
              participantes.append(aluno)
              print("\n Aluno cadastrado com sucesso")
          if tipo == 2:
              especialidade = input ("Especialidade: " )
              instrutor = Instrutor (nome, email, especialidade)
              participantes.append(instrutor)
              print("\n Instrutor cadastrado com sucesso")
          else:
              print()
          
        elif escolha =="2":
            if not participantes:
             print("Nenhum partipante cadastrado!")
            else:
                print("\nParticipantes cadastrados:")
                tipo = "Aluno" if isinstance(p, Aluno) else "Instrutor"
                for p in participantes:
                    print(f"\n{p.nome}{p.tipo}{p.email}")

                      
        elif escolha =="3":
            if not participantes:
              print("Nenhum partipante cadastrado!")
            else:
                print("\nCertificados")
                for p in participantes:
                    print("p.emitirCertificado{}")
            
        elif escolha =="4":
          print("\nSaindo do Programa. Até mais!")
          break
        else:
            print("\nOpção Inválida!")




if __name__ == "__main__":
  main()

    