numero = int(input('Digite um valor '))
numero1 = int(input('Digite outro valor '))

if numero > numero1:
    print(f'O numero maior é o {numero} e o menor é o {numero1}')
elif numero1 > numero:
    print(f'Numero {numero1} é maior que {numero}')
else:
    print('Não existe maior, os dois número são iguais')
