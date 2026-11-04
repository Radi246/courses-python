import time


def maior(*num):
    cont = 0
    m = 0
    print('Analisando os valores passados...')
    time.sleep(1)
    for i in num:
        print(f'{i} ', end='')
        time.sleep(0.5)
    print(f'Foram informados {len(num)} números')

    while cont < len(num):
        if num[cont] > m:
            m = num[cont]
        cont +=1

    print(f'O maior valor informado foi {m}')

#Programa principal

maior(1, 2, 3, 4)
maior(1, 8, 9, 4)
maior()