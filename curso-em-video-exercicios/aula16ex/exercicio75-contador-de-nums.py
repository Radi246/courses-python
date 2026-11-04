contador = posicao = 0
tres = True
pares = ''
posicao_tres = None

num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

num5 = (num, num2, num3, num4)

for i in num5:
    posicao += 1

    if i == 9:
        contador += 1

    if i == 3 and tres:
        posicao_tres = posicao

    if  i % 2 == 0:
        pares += f'{i}, '

print(f'O número nove apareceu essa quantidade de vezes: {contador}')

if posicao_tres is not None:
    print(f'O número três apareceu na posição: {posicao_tres}')
else:
    print('O número três não apareceu em nenhum momento.')

print(f'Os números pares são: {pares.rstrip(', ')}')