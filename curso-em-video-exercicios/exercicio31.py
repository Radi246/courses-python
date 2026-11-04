distancia = int(input('Qual a distancia da sua viagem?\n'))

if distancia <= 200:
    valor = float(0.50 * distancia)

else:
    valor = float(0.45 * distancia)

print(f'O valor da sua viagem será de R${valor}')
