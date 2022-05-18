class Carro:

 def __init__ (self, modelo, cor, ano, hodometro = 1000):

    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    self.hodometro = hodometro

 def buzinar(self):

   return 'bi bi'

 def abrir_porta_malas(self):

   print ('Porta mala abrindo...')
   return True

 def dirigir(self):

   self.hodometro += self.hodometro

   print('Dirigindo')

 def __str__(self):
   return f'O modelo {self.modelo} de cor {self.cor} do ano {self.ano} tem {self.hodometro} km rodados'
