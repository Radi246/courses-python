nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a sua segunda nota '))
nota3 = float(input('Digite a sua terceira nota '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Você passou de ano com uma média de {media:.1f}')
elif media > 4.5 and media < 6:
    print(f'Você ficou de recuperação com uma media de {media:.1f}')
else:
    print(f'Você repetiu de ano com uma media de {media:.1f}')