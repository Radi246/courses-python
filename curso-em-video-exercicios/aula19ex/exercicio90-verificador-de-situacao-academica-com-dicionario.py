dados = dict()

dados['Nome'] = str(input('Digite o nome do aluno: '))
dados['Media'] = float(input('Digite a média do aluno: '))

if dados['Media'] < 6:
    dados['Situação'] = 'Reprovado'
else:
    dados['Situação'] = 'Aprovado'

print(f'O nome do aluno é {dados['Nome']}')
print(f'Sua média foi {dados['Media']}')
print(f'Por isso foi {dados['Situação']}')