numeros = [[],[]]


for i in range(0, 6):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        numeros[1].append(num)
    else:
        numeros[0].append(num)

numeros[1].sort()
numeros[0].sort()

print('Números impares: ', numeros[0])
print('Números pares: ', numeros[1])