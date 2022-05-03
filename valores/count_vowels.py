def count_vowels(string):
    # TODO: a função deve retornar a quantidade de vogais em string
    # Dica: use loop for e condicionais
    # Exemplo: string = 'qualquer texto' deve retornar 6


    string_em_minusc = string.lower()
    dicio_vogais = {}
    for vogais in 'aeiou':
        contar = string_em_minusc.count(vogais)
        dicio_vogais[vogais] = contar
    valores = dicio_vogais.values()
    tds_vogais = sum(valores)

    return (tds_vogais)
    pass


