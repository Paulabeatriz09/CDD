# Crie uma classe chamada Ingresso, que
# possui um valor em reais e um método
# imprimeValor()
# – Crie uma classe VIP, que herda de Ingresso e
# possui um valor adicional. Crie um método que
# retorne o valor do ingresso VIP (com o adicional
# incluído)

class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def impprimevalor(self,valor):
        print(self.valor," R$")

class Vip(Ingresso):
    def _init_(self,adicional):
        super()._init_(valor)
        self.adiconal=adicional

    def valorad(self,adicional):
        print(self.valor+adicional," R$")