from random import randint
from time import sleep
from operator import itemgetter

inicio = str(input('Pressione enter para começar'))

jogo = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1, 6)}

ranking = list()

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('=-'*30)
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}')
