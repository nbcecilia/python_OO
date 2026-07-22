class Personagem:
    def __init__(self,nome, nivel):
        self.__nome = nome
        self.__nivel = nivel
    def get_nome(self):
       return self.__nome
    def get_nivel(self):
       return self.__nivel
    def set_nome(self, nome):
        self.__nome = nome
    def set_nivel(self, nivel):
        self.__nivel = nivel


    def atacar(self):
        print(f"\n {self.get_nome()} Ataca!!")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel,forca):
        super().__init__(nome, nivel)
        self.forca = forca
    def atacar(self):
        print(f"\n{self.get_nome()} realiza um ataque com sua espada! (Força: {self.forca}).")


class Mago(Personagem):
    def __init__(self, nome, nivel,mana):
        super().__init__(nome, nivel)
        self.mana = mana
    def atacar(self):
        print(f"\n{self.get_nome()} realiza um ataque com magia! (Mana: {self.mana}).")


def main():
    gue1 = Personagem("Silver", 80)
    gue2 = Guerreiro("Raiox", 95, 80)
    mago = Mago ("Gandalf", 90, 100)
   


    lista_personagens = [gue1, gue2, mago]

    print("\n---Ação dos Personagens---")
    for p in lista_personagens:
        p.atacar()



if __name__ == "__main__":
    main()

