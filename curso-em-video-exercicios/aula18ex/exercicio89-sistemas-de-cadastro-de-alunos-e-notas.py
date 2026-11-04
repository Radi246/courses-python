ficha = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    escolha = str(input('Quer continuar? Digite "n" para encerrer.'))

    if escolha in 'Nn':
        break


print('=-' *30)
print(f'{'No.':<4}{'Nome':<8}{'Media':<10}')
print(f'=-'*30)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<8}{a[2]:<10}')

while True:
    opc = int(input('Quer ver a nota de qual aluno? 999 para encerrar: '))
    if opc == 999:
        break
    print(f'O aluno {ficha[opc][0]} tem as seguintes notas: {ficha[opc][1]}')

print('Volte sempre. ')