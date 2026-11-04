import random

num = random.randint(1,5)

escolha = int(input(f'Escolha um numero entre 1 a 5\n'))

if escolha == num:
    print('Parabens, acertou.')
else:
    print(f'Errou, o numero era {num}')