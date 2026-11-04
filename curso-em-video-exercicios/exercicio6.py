preco = int(input('Digite o valor do produto\n'))
porcento = int(input('Qual o desconto do produto?\n'))

desconto = porcento / 100
valor = preco * desconto
final = preco - valor

print((f'O preço com desconto fica {final}'))

