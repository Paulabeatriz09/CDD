class Conta:

    def __init__(self, numero, nome, tipo,limite=0,saldo=0,novo=0,status=False):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.saldo = saldo
        self.limite= limite
        self.status= status
        self.novo=novo


    def ativar(self):
        if self.status == False:
            print("A conta está ativa")
            self.status=True
        else:
            print("COnta não está ativada pois esta inativa")



    def inativa(self):
        if self.status == False:
            print("A conta está inativa")


    def depositar(self, valor):
        if self.status == True:
            self.saldo = self.saldo + valor
            print(self.nome,"deposito realizado",self.saldo)


    def sacar(self, saque):
        if saque > (self.saldo+self.limite) and self.status == True:
            print("Saque realizado")
        else:
            print()


    def verificar_saldo(self):
        print(self.saldo,self.limite)


    def ativar1(self,valor):
        if self.status==True:
            self.limite=self.limite+valor

    def nov(self):
        if self.status==True:
            self.nov=self.limite+self.saldo
            print(self.nov)

