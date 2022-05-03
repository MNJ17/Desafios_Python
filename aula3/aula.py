def approved_alunes():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}

    aprovados = []

    for notas in alunes.values():
        if notas >= 70:
         aprovados.append(notas)
    return (len(aprovados))




def approved_alunes_names():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}

    aprovados =[]

    for alunos, notas in alunes.items():
        if notas >= 70:
            aprovados.append(alunos)
    return(aprovados)

def count_letters(string):
    # TODO: crie uma função que conte quantas vezes cada letra aparece na string e
    # retorne um dicionário com a letra como chave e a quantidade como valor
    # Exemplo: string = 'textooo' deve retornar {'e':1, 't':2, 'x':1, 'o':3}
    # Dica: use laço de repetição, condicionais e seus conhecimentos sobre dicionários

    string_em_minusc = string.lower()
    dicio_letras = {}
    for letras in "abcdefghijklmnopqrstuvwxyz":
        if letras in string_em_minusc:
            dicio_letras[letras] = string_em_minusc.count(letras)
    return dicio_letras







