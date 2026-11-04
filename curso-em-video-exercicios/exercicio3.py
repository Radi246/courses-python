numero = input('Digite um numero\n')
resultado = int
numero1 = 11

try:
    numero = int(numero)
    for i in range(1, numero1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print('O que foi digitado não é inteiro')

