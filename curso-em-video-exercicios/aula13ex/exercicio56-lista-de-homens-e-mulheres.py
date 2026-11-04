idade_soma = 0
idade_velho = 0
mulher_nova = 0

for i in range(4):
    nome = input('Qual o seu nome?: ').strip()
    idade = int(input('Quantos anos você tem?: '))
    sex = input('Qual o seu sexo?\n[M] para masculino\n[F] para feminino\n').strip().upper()

    idade_soma = idade_soma + idade

    if sex == 'M':
        if idade > idade_velho:
            nome_velho = nome
            idade_velho = idade

    if sex == 'F':
        if idade < 20:
            mulher_nova =+1

idade_media = idade_soma / 4

print(f'A idade média do grupo é: {idade_media}\nO homem mais velho é: {nome_velho}\nA quantidade de mulheres abaixo de 20 é: {mulher_nova}')