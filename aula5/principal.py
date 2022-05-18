from gerenciador import Gerenciador

gerenciador = Gerenciador()

continuar = True
while(continuar): # Como o continuar é booleano não precisamos de continuar == True
  print("O que deseja fazer?")
  print("1 - Exibir a lista de tarefas")
  print("2 - Adicionar uma nova tarefa")
  print("3 - Marcar uma tarefa como concluída")
  print("4 - Sair")
  opcao = int(input(">>> "))
  if opcao == 1:
    gerenciador.listar_tarefas()
  elif opcao == 2:
    gerenciador.adicionar_tarefa()
  elif opcao == 3:
    gerenciador.marcar_como_concluida()
  else:
    continuar = False
  print("----")
