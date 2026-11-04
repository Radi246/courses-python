matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = pares = soma = 0


for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um número para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
        if l ==  2:
            soma += matriz[l][c]

print('=-'*30)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
    print('')
print(f'A soma dos valores pares é: ',pares)
print(f'O maior número da segunda linha é: ', maior)
print(f'A soma de todos os valores da última linha é: ', soma)