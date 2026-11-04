r = 0
t = n = 1


while True:
    t = int(input('Digite um número: '))

    if t < 0:
        break

    while n <= 10:
        r = t * n
        print(f'{t} x {n} = {r}')
        n += 1

print('Programa encerrado, volte sempre.')