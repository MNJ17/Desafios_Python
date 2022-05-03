
def factorial(number):
    # TODO: criar uma função que deve retornar o fatorial de number
    # Lembrando que o fatorial de um número natural n é calculado por n! = n*(n-1)*(n-2)*....*3*2*1
    # Exemplo: fatorial de 4 é calculado por 4! = 4*3*2*1
    # Dica: use laço de repetição

    fat = 1
    for m in range(1, number + 1):

     fat *= m

    return fat
    pass









