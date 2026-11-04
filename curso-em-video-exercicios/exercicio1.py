numero = int(input('Digite um numero\n'))

antecessor = numero - 1
sucessor = numero + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(numero, antecessor, sucessor))

numero2 = int(input('Digite outro número\n'))

dobro = numero2 * 2
triplo = numero2 * 3
raiz = numero2 **(1/2)

print('O dobro de {} é {}, o triplo é {}, e a raiz é {}'.format(numero2, dobro, triplo, raiz))

nota1 = int(input('Digite a primeira nota nota\n'))
nota2 = int(input('Digite a segunda nota\n'))
nota3 = int(input('Digite a terceira nota\n'))

somaNota = nota1 + nota2 + nota3
media = somaNota / 3
print('Sua média é {}'.format(media))