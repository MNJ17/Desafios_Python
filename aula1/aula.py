def days_in_a_month(month):
  # TODO: Informado o mês desejado, retornar o número de dias
  # Auxílio: Utilize um dicionário para facilitar o trabalho
  dicionario = {

      'janeiro': 31,
      'fevereiro': 28,
      'março': 31,
      'abril': 30,
      'maio': 31,
      'junho': 30,
      'julho': 31,
      'agosto': 31,
      'setembro': 30,
      'otubro': 31,
      'novembro': 30,
      'dezembro': 31,

     }


  return dicionario[month]

print(days_in_a_month('novembro'))



