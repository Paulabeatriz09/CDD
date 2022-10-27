class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(self.nome," Foi comer")

class Gato(Animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def miar(self):
        print(self.nome," Está miando")
        
class Cachorro(Animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def latir(self):
        print(self.nome," está latindo")

class Coelho(Animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def pula(self):
        print(self.nome," está pulando")

class Vaca(Animal):
    def _init_(self,nome,cor):
        super()._init_(nome,cor)

    def anda(self):
        print(self.nome," está andando")