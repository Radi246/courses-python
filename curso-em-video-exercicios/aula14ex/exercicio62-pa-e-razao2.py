priTermo = float(input('Digite o primeiro termo da PA: '))
razão = float(input('Digite a raão da PA: '))
n = 0
termos = ''
quantTermos = int(input('Quantos termos você quer saber?: '))

while quantTermos != 0:
    for i in range(quantTermos):
        termos += f'{priTermo}, '
        priTermo += razão
        n += 1

    print(termos[:-2])
    quantTermos = int(input('Quantos termos adicionais quer que seja mostrado?: '))
print(f'Programa finalizado com {n} termos exibidos')
