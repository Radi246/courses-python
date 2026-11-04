import random
import time

lista = list()

def sorteio():
    print(f'Sorteando 5 valores na lista: ',end='')
    for i in range(5):
        num = random.randint(1,10)
        time.sleep(0.5)
        print(f'{num} ', end='')
        lista.append(num)
def soma_par():
    soma = 0

    for i in lista:
        if i % 2 == 0:
            soma += i

    print(f'\nSomando todos os valores de {lista} temos {soma}')

sorteio()
soma_par()