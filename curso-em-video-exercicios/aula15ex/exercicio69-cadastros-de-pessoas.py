sexo = str
cont_idade = 0
cont_m = 0
cont_f = 0



while True:
    sexo = input('Qual o seu sexo? F/M?: ').upper()
    idade = int(input('Digite a sua idade?: '))

    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1

    cont = str(input('Você quer continuar? S/N: ')).upper()

    if cont == 'N':
        break

print(f'{cont_idade} pessoas são maiores de 18.\nForam cadastrados {cont_m} homens foram cadastrados.\nForam cadastrados {cont_f} mulheres menores de 20')