import time


def cont(a,b,c):
    if c < 1:
        c = 1
    print(f'Contando de {a} até {b} pulando de {c} em {c}')
    if a < b:
        print('=-' * 20)
        time.sleep(1)
        while a <= b:
            print(f'{a} ', end='')
            a += c
            time.sleep(0.5)
        print('FIM!')
        return
    if b < a:
        print('=-' * 20)
        time.sleep(1)
        while b <= a:
            print(f'{a} ', end='')
            a -= c
            time.sleep(0.5)
        print('FIM!')
        return



#Programa principal

cont(1, 10, 1)
cont(10, 0, 2)
print('=-'*30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(inicio, fim, passo)
