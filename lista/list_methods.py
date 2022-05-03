def sort_asc(my_list):
  # TODO: Retorne a lista de nomes recebida em ordem alfabética ascendente
  my_list.sort()
  return my_list


def sort_desc(my_list):
  # TODO: Retorne a lista de nomes recebida em ordem alfabética descendente
  my_list.sort(reverse = True)
  return (my_list)


def find_list_element(my_list):
  # TODO: Retorne o segundo elemento da lista recebida
  return (my_list[1])


def find_last_list_element(my_list):
  # TODO: Retorne o último elemento da lista recebida
  return (my_list[-1])


def find_out_of_range_error():
  # TODO: Encontrar o erro no código abaixo
  # TODO: my_list não deverá ser modificada
  my_list =[1, 2, 3, 4, 5]
  return my_list[4]

def x_not_in_the_list_error():
  # TODO: Encontrar o erro no código abaixo
  # TODO: my_list não deverá ser modificada
  # TODO: Último elemento da lista deverá ser removido
  my_list =[1, 2, 3, 4, 5]
  my_list.remove(5)
  return my_list [-1]

def list_remove_last(my_list):
  # TODO: Remover a lista recebida como argumento sem o último elemento
  del my_list[-1]
  return my_list
