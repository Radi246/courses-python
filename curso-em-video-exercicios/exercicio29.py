vel = int(input('Você está dirigindo em uma via, qual é a sua velocidade?\n'))

if vel > 80:

    vel = float(vel - 80)*7

    print(f'Você foi multado, a multa será de R${vel}')

else:
    print('Você está dentro da velocidade aceitavel.')