a = float(input('Digite o primeiro número\n'))
b = float(input('Digite o segundo número\n'))
c = float(input('Digite o terceiro número\n'))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Um triangulo pode ser formado!')
        else:
            print('Um triangulo não pode ser formado.')
    else:
        print('Um triangulo não pode ser formado.')
else:
    print('Um triangulo não pode ser formado.')