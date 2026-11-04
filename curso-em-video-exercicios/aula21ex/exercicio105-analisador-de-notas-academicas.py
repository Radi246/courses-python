def notas(* nota, sit=False):
    """
    Função para calcular notas
    :param nota: Pega todas as notas
    :param sit: Mostra a situação da média. Ruim, médio ou bom
    :return: Retorna a quantidades de notas, a maior nota, menor, a média e a situação
    """
    maior = menor = soma = 0
    notas1 = dict()

    total = len(nota)
    notas1['Total'] = total

    for c, i in enumerate(nota):
        if c == 0:
            maior = i
            menor = i
        elif i > maior:
            maior = i
        elif i < menor:
            menor = i
        soma += i
    notas1['Maior'] = maior
    notas1['Menor'] = menor
    notas1['Media'] = soma / len(nota)

    if sit:
        if notas1['Media'] < 6:
            notas1['SITUAÇÃO'] = 'Ruim'
        elif 6 <= notas1['Media'] <= 7:
            notas1['SITUAÇÃO'] = 'Razoavel'
        if notas1['Media'] > 7:
            notas1['SITUAÇÃO'] = 'Bom'

    return notas1

num = notas(10, 5.5, 6.0, sit=True)
print(num)
help(notas)
