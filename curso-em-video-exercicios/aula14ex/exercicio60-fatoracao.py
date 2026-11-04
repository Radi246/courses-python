numero = int(input('Digite um número para fatorar: '))
n = 1
sequencia = ''
resultado = 1

while n <= numero:
    resultado *= n
    sequencia += f'{n}x' if n < numero else f'{n}'
    n += 1
print(f'{numero}! = {sequencia} = {resultado}')