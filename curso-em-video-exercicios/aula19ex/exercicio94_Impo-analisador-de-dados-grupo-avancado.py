lista = list()
lista_m = list()
lista_me = list()
dados = dict()
cont = media = cont_f = 0

while True:
    dados['Nome'] = str(input('Digite o seu nome: '))
    dados['Sexo'] = str(input('Digite seu sexo F/M: ')).upper().strip()
    dados['Idade'] = int(input('Digite a sua idade: '))

    escolha = str(input('Quer continuar?: '))

    lista.append(dados.copy())  # Adicionando o dicionário copiado à lista

    if escolha in 'Nn':
        break

print(f'=-'*30)
print(f'Foram cadastradas {len(lista)} pessoas')


# Calculando a média de idade
for pessoa in lista:
    cont += pessoa['Idade']

media = cont / len(lista)

# Separando as mulheres
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        lista_m.append(pessoa)

# Separando as pessoas com idade acima da média
for pessoa in lista:
    if pessoa['Idade'] > media:
        lista_me.append(pessoa)

# Imprimindo a lista das pessoas com idade acima da média
print('=-'*30)
print(f'A média de idades das pessoas é: {media}')
print('=-'*30)
print('     MULHERES CADASTRADAS    ')

# Imprimindo os nomes das mulheres
for pessoa in lista_m:
    print(pessoa['Nome'])

# Imprimindo pessoas acima da média de idade
print('=-'*30)
print('     PESSOAS ACIMA DA MÉDIA DE IDADE DO GRUPO    ')
for pessoa in lista_me:
    print(pessoa['Nome'])