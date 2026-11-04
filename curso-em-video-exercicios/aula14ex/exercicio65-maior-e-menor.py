media = 0
n = 'N'
maior = float('-inf')
menor = float('inf')
contador = 0
soma = 0

while n != 'S':
    valor = int(input('Digite um valor: '))

    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

    contador += 1
    soma += valor


    n = input('Quer encerrar? Digite [S] caso queira encerrar. Digite qualquer outra coisa caso queira continuar: ').upper()

if contador > 0:
    media = soma / contador
    print(f'O maior valor é {maior}, o menor é {menor}. A média entre ele foi {media}')
else:
    print('Nenhum número foi digitado.')