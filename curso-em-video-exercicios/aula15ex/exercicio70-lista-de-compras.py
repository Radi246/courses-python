contador = 0
soma = 0
menor = float('inf')
nome_b = ''

while True:
    nome = str(input('Qual o nome do produto que você vai comprar?: '))
    preço = float(input('Preço: R$'))

    soma += preço

    if preço > 1000:
        contador += 1

    if preço < menor:
        menor = preço
        nome_b = nome

    escolha = str(input('Você quer continuar? S/N: ')).upper()

    if escolha == 'N':
        break
print(f'A soma de todos os seus produtos foi: {soma:.2f}')
print(f'Produtos mais caros que 1000: {contador}')
print(f'O produto com o menor preço é {nome_b} com o valor de {menor:.2f}')