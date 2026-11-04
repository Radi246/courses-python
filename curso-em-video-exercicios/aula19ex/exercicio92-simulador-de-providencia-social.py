from datetime import datetime

dados = dict()

dados['Nome'] = str(input('Digite o seu nome: '))
ano = int(input('Digite o ano de nascimento: '))

dados['Idade'] = datetime.now().year - ano

dados['CTPS'] = int(input('Digite qualquer numero para Carteira de Trabalho (0 se não tem): '))

if dados['CTPS'] != 0:


    dados['Ano'] = int(input('Digite o ano da primeira contratação: '))

    dados['Aposento'] = dados['Idade'] + 35

    dados['Salário'] = float(input('Salário: R$ '))

    print('=-'*30)

    print(f'O nome tem o valor {dados['Nome']}')
    print(f'A idade tem o valor {dados['Idade']}')
    print(f'CTPS tem valor {dados['CTPS']}')
    print(f'Contratação tem o valor {dados['Ano']}')
    print(f'Salario tem valor {dados['Salário']}')
    print(f'A aposentadoria tem o valor {dados['Aposento']}')

else:
    print('=-'*30)
    print(f'O nome tem o valor {dados['Nome']}')
    print(f'A idade tem o valor {dados['Idade']}')