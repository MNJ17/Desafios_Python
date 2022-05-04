import string # Leia mais sobre a biblioteca string. https://docs.python.org/pt-br/3/library/string.html#string.ascii_letters
import random # Você pode gerar números aleatórios com o método random. https://docs.python.org/3/library/random.html

def advanced_password_generator(password_size):
  # Crie um gerador de senhas com números e caracteres de maneira alternada.
  # Ex.: A chamada advanced_password_generator(5) -> Irá resultar em algo parecido com 8j9D9 ou 5b7D6

  passe = ''
  caracteres = string.ascii_letters
  números = string.digits
  opições = caracteres + números

  for M in range(password_size):
        M = random.choice(opições)
        passe = passe + M

  return passe

# Use o print com a chamada do método para testar
#print(advanced_password_generator(5))
