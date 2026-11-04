num = int(input('Digite quantos números fibonacci '))
n = 2
sequencia = '0, 1'
num1 = 0
num2 = 1

if num == 1:
    sequencia = '0'

elif num == 2:
    sequencia = '0, 1'

else:
    while n < num:
        resultado = num1 + num2
        sequencia += f', {resultado}'
        num1 = num2
        num2 = resultado

        n += 1
print(sequencia)