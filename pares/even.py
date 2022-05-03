def is_even(number):
  # Melhorar função is_even já implementada em 01-Essencial/07-aula/aula.py
  # TODO: Retorne 'Número é par' se number for par e 'Número é inpar' se number for impar
  # Exemplo 1: number = 2,  resultado = 'Número é par'
  # Exemplo 2: number = 3,  resultado = 'Número é inpar'

  if (number%2) == 0:
    return f'Número é par'
  if (number%2) >=1:
    return f'Número é inpar'

