# Você deve copiar o seu código do Exercício anterior e realizar algumas modificações.
# Agora no método extrato deverá retornar as operações:
# Exemplo:
#
# conta=Conta("Yasmin", 1, 100)
# conta.saque(50)
# conta.deposito(40)
# conta.saque(9)
# conta.extrato()
# O método extrato() deverá retornar uma extrato bancário (Você deve retornar frases exatamentes como essas, até com os mesmos espaços):
# Operação: Saque    | Valor: R$ 50
# Operação: Depósito | Valor: R$ 40
# Operação: Saque    | Valor: R$ 9
# Saldo Final: R$ 81

# Faça as modificações necessárias nos outros métodos para contemplar o novo extrato.

class Conta():

 lista_conta = []

 def __init__(self, nome_cliente, numero_conta, saldo = 0):

    self.nome_cliente = nome_cliente
    self.numero_conta = numero_conta
    self.saldo = saldo


 def deposito(self, deposito):
   self.saldo += deposito
   self.lista_conta.append(f'Operação: Depósito | Valor: R$ {deposito}')



 def saque(self, saque):
   if self.saldo >= saque:
     self.saldo -= saque
     self.lista_conta.append(f'Operação: Saque  | Valor: R$ {saque}')



 def extrato(self):
   self.lista_conta.append(f'Saldo final: R$ {self.saldo}')
   for M in self.lista_conta:
     print (M, '\n')

conta=Conta("Yasmin", 1, 100)
print(conta.saque(50))
print(conta.deposito(40))
print(conta.saque(9))
print(conta.extrato())



