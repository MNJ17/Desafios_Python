# Leia mais sobre criptografia
# Nesse exercício iremos implementar dois métodos um para criptografar e outro para descriptografar com a Cifra de César.
# Leia mais aqui: https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar
# Desconsidere acentos
# Sua função receberá a chave e o texto

def criptografar(chave, texto):

  letras = []
  alfabeto_minusc = 'abcdefghijklmnopqrstuvwxyz'
  alfabeto_maiusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for letra in texto:
      if letra == " ":
        letras.append(letra)
      elif letra in alfabeto_minusc:
        letras.append(alfabeto_minusc[(alfabeto_minusc.index(letra)+chave)% len(alfabeto_minusc)])
      elif letra in alfabeto_maiusc:
        letras.append (alfabeto_maiusc[(alfabeto_maiusc.index(letra)+ chave)% len(alfabeto_maiusc)])
      password = "".join(letras)
  return password

def descriptografar(chave, texto):

  letras = []
  alfabeto_minusc = 'abcdefghijklmnopqrstuvwxyz'
  alfabeto_maiusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for letra in texto:
      if letra == " ":
        letras.append(letra)
      elif letra in alfabeto_minusc:
        letras.append(alfabeto_minusc[(alfabeto_minusc.index(letra)-chave)% len(alfabeto_minusc)])
      elif letra in alfabeto_maiusc:
        letras.append (alfabeto_maiusc[(alfabeto_maiusc.index(letra)- chave)% len(alfabeto_maiusc)])
      password = "".join(letras)
  return password
