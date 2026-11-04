ano = int(input('Digite um ano para saber se ele é um ano bissexto\n'))

if ano % 4 == 0:
    print(f'{ano} é um ano bissexto')

else:
    print(f'{ano} não é um ano bissexto')