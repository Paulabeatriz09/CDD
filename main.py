from biblioteca import Conta

c1=Conta(123,"Paula","Poupança")
c1.ativar()
print(c1.saldo)
c1.depositar(100)
print(c1.saldo)
c1.sacar(10)
c1.verificar_saldo()