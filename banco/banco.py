# Você deverá criar uma classe chamada Conta, essa classe irá simular de forma simples o funcionamento de
# uma conta bancária.
# Essa conta devera ter atributos nome_cliente, numero_conta e saldo. Ao criar uma conta o saldo deverá ser 0.
# Você deverá fazer 3 métodos:
# 1 - extrato - nesse método você exibirá apenas o saldo.
# 2 - saque - Implemente a operação de saque, que irá receber um valor a ser retirado da conta.
# 3 - deposito - Implemente a operação de depósito, que irá receber um valor a ser depositado na conta.


# TODO: Criei seu código
class Conta():

 def __init__(self, nome_cliente, numero_conta, saldo = 0):

     self.nome_cliente = nome_cliente
     self.numero_conta = numero_conta
     self.saldo = saldo


 def extrato(self):
    return 'O saldo da conta é: ' + str(self.saldo)

 def saque (self, saque):
   if self.saldo >= saque:
    self.saldo -= saque
   else:
     print('Saldo insuficiente')

 def deposito (self, deposito):
     self.saldo += deposito


 # Para testar
 #conta1=Conta("Yasmin", 1, 100)
 #conta2=Conta("Joana", 2, 200)
 #print(conta1.extrato())
 #print(conta2.extrato())
 #conta1.saque(50)
 #conta2.deposito(50)
 #conta1.saque(10.15)
 #conta2.deposito(40)
 #conta2.deposito(1000)
 #conta1.saque(9)
 #conta2.deposito(45.50)
 #conta2.saque(250)
 #print(conta1.extrato())
 #print(conta2.extrato())
