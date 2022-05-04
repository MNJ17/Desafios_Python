
import string # Leia mais sobre a biblioteca string. https://docs.python.org/pt-br/3/library/string.html#string.ascii_letters
import random # Você pode gerar números aleatórios com o método random. https://docs.python.org/3/library/random.html

# Crie um gerador de senhas aleatórias com somente letras do tamanho passado como parâmetro
def password_generator(password_size):

  senha = ''
  letras = string.ascii_letters
  for M in range(password_size):
      senha += random.choice(letras)

  return senha

print(password_generator(10))


