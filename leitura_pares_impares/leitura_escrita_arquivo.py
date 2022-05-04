# TODO: Crie um método que irá ler o arquivo "pares.txt" e irá salvar no arquivo "multiplos.txt" todos os múltiplos de 3, um número por linha.
# IMPORTANTE: Este exercício não tem teste (pytest).

def leitura_escrita_arquivo():

    pares = open('pares.txt', 'r')
    numeros = pares.read().split()

    mult = open('multiplos.txt', 'w')
    for M in numeros:
      M = int(M)
      if M %3 == 0:
        mult.write('{}'.format(M) + '\n')
      else:
       continue

    mult.close()

