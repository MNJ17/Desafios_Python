def can_vote(age):
  # Melhorar função can_vote já implementada em 02-if/01-posso-votar/my_vote.py
  # TODO: Sendo informado a idade retorne a informação se a pessoa poderá votar seguindo as regras:
  # Menores de 0 anos = "Idade inexistente"
  # Menores de 16 anos = "Não pode votar"
  # Entre 16 e 17 anos = "Podem votar mas não são obrigados"
  # Entre 18 e 70 anos = "Obrigados a votar"
  # Maiores de 70 anos = "Podem votar mas não são obrigados"

  if age < 0:
   return ('Idade inexistente')
  elif age < 16:
    return ('Não pode votar')
  elif (age > 16) and (age < 17):
    return('Podem votar mas não são obrigados')
  elif (age > 17) and (age <= 70):
    return ('Obrigados a votar')
  else:
    return ('Podem votar mas não são obrigados')




def valid_password(password):
  # TODO: Verifique se a senha (password) é válida e retorne 'Válida' ou 'Não válida' conforme as regras:
  # Somente senhas com tamanho mínimo de 6 e máximo de 16 caracteres

   if  len(password) >= 6 and len (password) <=16:
    return ('Válida')

   else:
     return ('Não válida')



def vowel_count(string):
  # TODO: Conte o número de vogais existentes na string passada como parâmetro.
  # Exemplo 1: string = 'Olá Mundo' return = 4
  # Exemplo 2: string = 'Sirius Education' return = 8

  string_em_minusc = string.lower()
  dicio_vogais = {}
  for vogais in 'aeiou':
   contar = string_em_minusc.count(vogais)
   dicio_vogais[vogais] = contar
  valores = dicio_vogais.values()
  tsd_vogais = sum(valores)
  return(tsd_vogais)
