import random
import time
print('=-' *30)
print('                 JOGO DA MEGA           ')
print('=-'*30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer?: '))
print(f'Sorteando {quant} jogos, aguarde...')

cont = 0


for c in range(quant):
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    cont = 0
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    time.sleep(1)
    print(f'Jogo {c+1}: ',jogos[c])