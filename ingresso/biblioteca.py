# Crie uma classe chamada Ingresso, que
# possui um valor em reais e um método
# imprimeValor()
# – Crie uma classe VIP, que herda de Ingresso e
# possui um valor adicional. Crie um método que
# retorne o valor do ingresso VIP (com o adicional
# incluído)

class Ingresso():
    def __init__(self,valor,adicional):
        self.adicional=adicional
        self.valor=valor

    def impprimevalor(self):
        print(self.valor," R$")

class Vip(Ingresso):
    def _init_(self,valor,adicional):
        super().__init__(valor,adicional)


    def valorad(self):
        print(self.valor*self.adicional," R$")
