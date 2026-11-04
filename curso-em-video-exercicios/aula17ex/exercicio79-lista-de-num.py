valor = 0
valores = []
escolha = ''

while escolha != 'N':
    valor = int(input('Digite um número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso. ')

    else:
        print('O valor já foi adionado, tente outro valor. ')

    escolha = input('Quer continuar? S/N: ').upper()

valores.sort() #Acho que só funfa com números inteiros, tentei sem especificar o que o Valor era e não deu em nada :(
print(valores)


