  # Ler um número e retornar True se for primo e False se não for primo.
  # Sobre o que é um número primo: https://pt.wikipedia.org/wiki/N%C3%BAmero_primo
  # Dica: veja o for/else: https://book.pythontips.com/en/latest/for_-_else.html#else-clause
  # exemplos:
  # prime_numbers(10) -> False
  # prime_numbers(13) -> True
  # prime_numbers(1) -> False
  # prime_numbers(2) -> True

from typing import Tuple

def is_prime_number(number):

  if number == 0:
    return False

  elif number == 1:
    return False

  elif number == 2:
    return True

  elif number == 3:
    return True

  elif number %2 == 0 or  number %3 == 0:
    return False

  elif number %2 > 0:
    return True

  else:
    return False

print(is_prime_number(97))












