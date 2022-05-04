from time import sleep


def menu():
  opicoes =int(input('''
  =====================================================
                    Agenda em python
  Menu:

  [1]Exibir Agenda
  [2]Adicionar contato
  [3]Buscar contato
  [4]Deletar contato
  [5]Sair

  ======================================================
  ESCOLHA UMA OPIÇÃO
  >>>  '''))

  if opicoes == 1:
    exibirAgenda()

  elif opicoes == 2:
   adicionarContato()

  elif opicoes == 3:
    buscarContato()

  elif opicoes == 4:
    deletarContato()

  elif opicoes == 5:
    print('Saindo')
    sleep(1)
    print('Te vejo na prixima ;)')
  else:
     print('ERRO')
     sleep(1)
     print('Comando inválido, tente novamente')
     return menu()

def exibirAgenda():
   agenda = open ('mini_agenda.txt', 'r')
   agenda2 = agenda.read().split()
   agenda3 = {}

   if len(agenda2) >0:
     for nome in agenda2:
      if agenda2.index(nome) %2 == 0:
        agenda3[nome] = agenda2[agenda2.index(nome) + 1]
     for nomes, numeros in agenda3.items():
         print(' Nome: {} - Número: {}'.format(nomes, numeros))
     agenda.close()
     return menu()
   else:
        print('Agenda vazia!!!')
        print('Para adicionar um novo número selecione a segunda opição (2)')
   agenda.close()
   return menu()


def adicionarContato():


   nome = str(input('''Adicione o nome do contato
   >>> ''')).strip()
   tell = str(input('''Digite o telefone do contato
   >>> ''')).strip()
   try:
     arquivo = open('mini_agenda.txt', 'a')
     dados = f'{nome} {tell} \n'
     arquivo.write(dados)
     arquivo.close()
     print ('Contato salvo !')
     return menu()

   except:
    print('ERRO, tente novamente !!!')

    return menu()

def buscarContato():

    agenda = open('mini_agenda.txt', 'r')
    agenda2 = agenda.read().split()
    agenda3 = {}

    if len(agenda2) > 0:
        for nomes in agenda2:
            if agenda2.index(nomes) % 2 == 0:
                agenda3[nomes] = agenda2[agenda2.index(nomes) + 1]
        nome = str(input('''Digite o nome do seu contato
        >>> ''')).strip()
        if nome in agenda3.keys():
            for nomes, numeros in agenda3.items():
                if nome in nomes:
                    print('Nome: {} - Contato: {}'.format(nome, numeros))
                    agenda.close()
                return menu()
        else:
            print('Contato inexistente!!!')
            print ('Para adicionar um novo contato selecione a segunda opição (2)')
            return menu()


def deletarContato():
  agenda = open('mini_agenda.txt','r')
  agenda2 = agenda.read().split()
  agenda3 = {}

  for nomes in agenda2:
    if agenda2.index(nomes) % 2 == 0:
      agenda3[nomes] = agenda2[agenda2.index(nomes) + 1]

    remover = str(input('''Digite o nome para remover
    >>> ''')).strip()
    if remover in agenda3:
      agenda3.pop(remover)
      print('Contato deletado !!!')
      agenda.close()
      return menu()
    else:
          print('ERRO')
          print('Tente novamente!!!')
          agenda.close()
          return menu()

menu()

