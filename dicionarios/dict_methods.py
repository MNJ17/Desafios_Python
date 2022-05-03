def find_dict_element():
  # TODO: No dicionário 'my_dict' são armazenados as notas de alunos
  # Retorne a nota do aluno 'Júlio'
  my_dict = {

    'Ana': 10,
    'Júlio': 8,
    'Antônio': 9,
    'Maria': 7,
  }
  return my_dict ['Júlio']
  pass

def correct_dict():
  # TODO: No dicionário 'my_dict' são armazenados as notas de alunos, mas a aluna 'Ana' faz mais parte da turma
  # TODO: Retorne my_dict revisada com a exclusão da aluna 'Ana'['Júlio']
  my_dict = {

    'Ana': 10,
    'Júlio': 8,
    'Antônio': 9,
    'Maria': 7,
  }

  del my_dict ['Ana']
  return my_dict
  pass

def add_dict_item():
  # TODO: No dicionário 'my_dict' são armazenados as notas de alunos, a aluna 'Carla' acabou de entrar na turma
  # TODO: Retorne my_dict revisada com a inclusão da aluna 'Carla' e sua nota 0, pois ela ainda fará seus exercícios
  my_dict = {

    'Ana': 10,
    'Júlio': 8,
    'Antônio': 9,
    'Maria': 7,
  }
  my_dict ['Carla'] = 0

  return my_dict
  pass

def find_out_key_error():
  # TODO: Encontrar o erro no código abaixo
  # TODO: my_dict não deverá ser modificada
  my_dict = {

      'Ana': 10,
      'Júlio': 8,
      'Antônio': 9,
      'Maria': 7,
    }

  return my_dict ['Maria']
  pass
