# Ler um número e gerar todos os números primos menores que o número fornecido retornando uma lista com todos eles.
# Sobre números primos
# exemplos:
# prime_numbers(10) -> [2,3,5,7]
# prime_numbers(13) -> [2,3,5,7,11]


import re

def prime_numbers (number):

  M = list(range(2,number))

  for N in range(2,int(number)):
    if N in M:
      for J in range (N**2, number, N):
        if J in M: M.remove(J)

  return M

print(prime_numbers(77))
