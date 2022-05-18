import random

class Loteria():

 resultado = []

 @staticmethod

 def sorteio():

   while len(Loteria.resultado) <6:
     numeros_sorteados = random.randint(0, 60)

     if numeros_sorteados not in Loteria.resultado:
       Loteria.resultado.append(numeros_sorteados)
   Loteria.resultado.sort()

 @staticmethod

 def exibir_sorteio():
   print(Loteria.resultado)

Loteria.sorteio()
Loteria.exibir_sorteio()
