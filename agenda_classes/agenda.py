# Nesse exercícios vamos recriar a nossa agenda.
# Intruções:
# 1 - Crie uma classe Agenda, que receba um nome na inicialização Você deverá ter um atributo chamado contatos do tipo dicionário (Hash) para armazenar os contatos.
# 2 - Crie um método chamado adicionar_contato que receba dois parâmetros nome e telefone
# 3 - Crie outro método chamado remover_contato que receba como parâmetro o nome de um contato a ser removido


# TODO: Escreva seu código aqui

class Agenda():

 def __init__(self):

   self.contatos = {}

 def adicionar_contato(self, nome, telefone):

   self.contatos[nome] = str(telefone)

 def remover_contato(self, nome):
    if nome in self.contatos.keys():
      del self.contatos[nome]

 def exibir(self):
    return self.contatos


 #Para testar:
 #agenda = Agenda()
 #print(agenda.exibir())
 #agenda.adicionar_contato("Tulio", "3333")
 #agenda.adicionar_contato("Carol", "3334")
 #agenda.adicionar_contato("Ana", "1111")
 #print(agenda.exibir())
 #print(agenda.remover_contato("Tulio"))
 #print(agenda.exibir())
