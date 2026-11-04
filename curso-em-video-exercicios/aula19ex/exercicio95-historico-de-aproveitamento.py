aproveitamento = dict() #Crio um dicionario
jogadores = list() # Crio uma lista

while True:
    aproveitamento = dict() #Um dicionario "temporario"
    golsL = list() #Uma lista temporaria
    total = 0

    aproveitamento['Nome'] = str(input('Qual o nome do jogador?: ')) #Escrevendo o nome dos jogadores
    aproveitamento['Partidas'] = int(input('Quantas partidas ele jogou?: ')) #Perguntando quantas partidas foram jogadas

    for i in range(aproveitamento['Partidas']): #Vai pegar o valor de 'partidas' e vai repetir com base nesse valor
        gols = int(input(f'Quantos gols na partida {i + 1}?: ')) #Vai ficar perguntando até a repetição do valor partidas chegar

        total += gols #Vai somando os gols para dar um total

        golsL.append(gols) #Cria uma lista de gols

    aproveitamento['Gols'] = golsL #Coloca a lista de gols dentro de um dicionario
    aproveitamento['Total'] = total #Coloca o total de gols dentro do dicionario
    jogadores.append(aproveitamento) #Joga o dicionario pra dentro de uma lista

    escolha = str(input('Quer continuar?: ')) #Pergunta se quer continuar

    if escolha in 'Nn': #Se não quiser continuar, ele encerra
        break


print('=-'*30)
print(f'{'cod':<4}{'Nome':<8}{'Gols':<8}{'Total':>13}')
for i, dados in enumerate(jogadores): #Mostra todos os jogadores numa lista, o i mostra o numero de i
    print(f'{i:<4}{dados['Nome']:<8}{dados['Gols']}{dados['Total']:>8}')
print('-'*30)

while True:
    escolha1 = int(input('Mostrar dados de qual jogador? '))

    print(f'Levantamento para o jogador {jogadores[escolha1]['Nome']}') #Vai imprimir o que tiver no nome, no valor digitado, na lista de jogadores

    for i, jogador in enumerate(jogadores[escolha1]['Gols']): #O 'jogador' pega o valor que esta em gols, no valor da escolha, dentro da lista jogadores
        print(f'Na partida {i} fez {jogador}')