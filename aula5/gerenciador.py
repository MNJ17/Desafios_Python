from tarefa import Tarefa

class Gerenciador():
  def __init__(self):
    self.tarefas = []

  def listar_tarefas(self):
    print(" ====== Sua lista de tarefas ======")
    contador = 0
    for tarefa in self.tarefas:
      print(f"{contador} - {'[M]' if tarefa.concluida else '[ ]'} | {tarefa.descricao}")
      contador += 1

  def adicionar_tarefa(self):
    print("Digite a sua tarefa")
    descricao = input(">>> ")
    tarefa = Tarefa(descricao)
    self.tarefas.append(tarefa)

  def marcar_como_concluida(self):
    self.listar_tarefas()
    print('Qual tarefa deseja marcar como concluída?')
    numero_da_tarefa = int(input('>>> '))
    self.tarefas[numero_da_tarefa].concluida = True
