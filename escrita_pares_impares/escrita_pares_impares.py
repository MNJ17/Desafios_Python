# TODO: Crie um método que irá gravar os números de 0 a 100 em dois arquivos, no arquivo "impares.txt" grave os números ímpares e
# no arquivo "pares.txt" grave os números pares.
# IMPORTANTE: Este exercício não tem teste (pytest).

def escrever_pares_impares():

  pares = open ('pares.txt', 'w')
  impares = open('impares.txt', 'w')

  for numeros in range(101):
      if numeros %2 == 0:
        pares.write('{}'.format(numeros) + ',')
      else:
        impares.write('{}'.format(numeros) + ',')

  pares.close()
  impares.close()
