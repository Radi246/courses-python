num = int(input('Digite o primeiro numero\n'))
num2 = int(input('Digite o segundo numero\n'))
num3 = int(input('Digite o terceiro numero\n'))

menor = num
maior = num

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3


if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f'O numero maior é o {maior}')
print(f'O numero menor é {menor}')