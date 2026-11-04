salario = float(input('Qual o seu salario? Salario abaixo ou iguais a 1250.00 receberão um aumento de 15%\n'))

if salario > 1250.00:
    aumento = (10/100)*salario
    aumento1 = salario + aumento
    print(f'Seu salário será de {aumento1}')

if salario <= 1250.00:
    aumento = (15/100)*salario
    aumento1 = salario + aumento
    print(f'Seu salario será de {aumento1}')