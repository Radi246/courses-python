aproveitamento = dict()
golsL = list()
total = 0

aproveitamento['Nome'] = str(input('Qual o nome do jogador?: '))
aproveitamento['Partidas'] = int(input('Quantas partidas ele jogou?: '))

for i in range(aproveitamento['Partidas']):
    gols = int(input(f'Quantos gols na partida {i + 1}?: '))

    total += gols

    golsL.append(gols)

aproveitamento['Gols'] = golsL
aproveitamento['Total'] = total


print('=-'*30)
print(aproveitamento)
print('=-'*30)
print(f'O campo do nome tem o valor {aproveitamento['Nome']}')
print(f'O campos dos gols tem o valor {aproveitamento['Gols']}')
print(f'O campo total tem o valor {aproveitamento['Total']}')
print('=-'*30)
print(f'O jogador {aproveitamento['Nome']} jogou {aproveitamento['Partidas']} partidas')

for i in range(len(aproveitamento['Gols'])):
    print(f'=> Na partida {i + 1}, fez {aproveitamento['Gols'][i]} gol(s)')
print(f'Foi um total de {aproveitamento['Total']}')