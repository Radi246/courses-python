n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Digite um numero: '))

    if n != 999:
        soma = n + soma
        contador += 1
print(f'Você digitou {contador} números, e a soma deles é {soma}')

