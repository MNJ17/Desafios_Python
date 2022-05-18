class Tarefa():

 def __init__(self, descricao):
   self.descricao = descricao
   self.concluida = False

 def concluir (self):
    self.concluida = True
