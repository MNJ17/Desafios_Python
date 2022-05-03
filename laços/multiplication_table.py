def multiplication_table(number):
    # TODO: use o for para retorna uma lista com a tabuada do number selecionado pelo usuário
    # Exemplo: number = 3 deve retorna [3,6,9,12,15,18,21,24,27,30]

    tabuada = []
    for i in range(1,11):
       tabuada.append(number*i)
    return tabuada


def other_multiplication_table(number):
    # TODO: use o while para retorna uma lista com a tabuada do number selecionado pelo usuário
    # Exemplo: number = 3 deve retorna [3,6,9,12,15,18,21,24,27,30]

    tabuada = []
    i = 1
    while i <=10:
     tabuada.append(number*i)
     i += 1
    return tabuada


