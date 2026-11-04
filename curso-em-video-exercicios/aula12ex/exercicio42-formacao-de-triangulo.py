a = float(input('Digite o primeiro número '))
b = float(input('Digite o segundo número '))
c = float(input('Digite o terceiro número '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Um triangulo pode ser formado, ele sera um equilátero')
    elif a == b or b == c or c == a:
        print('Um triangulo pode ser formado, ele sera um isósceles')
    else:
        print('Um triangulo pode ser formado, ele sera um escaleno')
else:
    print('Um triangulo não pode ser formado')


