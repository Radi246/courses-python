from datetime import datetime

ano_atual = datetime.now().year # Pega o ano atual

menor = 0
maior = 0

for i in range(0, 6):
    ano_nascimento = int(input('Digite o ano de seu nascimento: '))
    idade = ano_atual - ano_nascimento # Faz o calculo para saber a idade

    if idade >= 18: # Pessoas maiores de 18 serão contabilizadas aqui
        maior = maior + 1

    else: # Pessoas de menor serão aqui
        menor = menor + 1

print(f'Uma quantidade de {maior} é de maior, uma quantidade de {menor} é de menor')