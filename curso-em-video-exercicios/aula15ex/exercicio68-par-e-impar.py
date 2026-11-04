import random

escolha = int(input('Escolha [1] para impar e [2] para par: '))
contador = 0


while True:
    num = int(input('Escolha um número entre 0 e 5: '))
    if num < 0 or num > 5:
        print('Número invalido, escolha um número entre 0 a 5.')
        continue
    escolha_pc = random.randint(0, 5)
    soma = num + escolha_pc

    if soma % 2 == 0:
        resultado = 2
    else:
        resultado = 1


    if resultado == escolha:
        print('Você ganhou! +1 ponto. ')
        contador += 1
    else:
        print('Você perdeu.')
        break

print(f'Você conseguiu uma sequência de {contador} vitórias.')