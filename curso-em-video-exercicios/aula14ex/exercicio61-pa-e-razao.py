priTermo = float(input('Digite o primeiro termo da PA: '))
razão = float(input('Digite a raão da PA: '))
n = 0
termos = ''

while n < 10:
    print(priTermo)
    priTermo = razão + priTermo
    termos += f'{priTermo}, ' if n < 10 else f'{priTermo}'
    n += 1
print(termos)