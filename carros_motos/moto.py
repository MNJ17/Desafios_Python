class Moto:

 def __init__(self, modelo, cor, ano, hodometro = 1000):

    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    self.hodometro = hodometro

 def buzinar(self):

   return 'bi bi'

 def pilotar(self):
   self.hodometro += self.hodometro
   print('pilotando')

 def __str__(self):
   return f'O modelo {self.modelo} de cor {self.cor} do ano {self.ano} tem {self.hodometro} km rodados'
