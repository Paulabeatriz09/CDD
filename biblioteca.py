class Conta:

    def __init__(self, numero, nome, tipo, saldo=0, status=False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status


    def ativar(self):
        if self.status == True:
            print("A conta está ativa")
        else:
            self.status = True
            print("A conta foi ativada com sucesso")


    def inativa(self):
        if self.status == False:
            print("A conta está inativa")


    def depositar(self, valor):
        if self.status == True:
            self.saldo = self.saldo + valor
            print(f'{self.nome} deposito realizado')


    def sacar(self, saque):
        if saque > self.saldo and self.status == True:
            print("Saldo insuficiente")
        else:
            print("Realizando saque")


    def verificar_saldo(self):
        print(self.saldo)
