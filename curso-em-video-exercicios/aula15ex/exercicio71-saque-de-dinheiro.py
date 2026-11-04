valor = int(input('Quanto você quer sacar?: '))
cont50 = cont20 = cont10 = cont1 = 0


while True:

    if valor >= 50:
        cont50 += 1
        valor -= 50

    elif valor >= 20:
        cont20 += 1
        valor -= 20

    elif valor >= 10:
        cont10 += 1
        valor -=10

    elif valor >= 1:
        cont1 += 1
        valor -= 1


    if valor == 0:
        break
print(f'Notas de 50: {cont50}')
print(f'Notas de 20: {cont20}')
print(f'Notas de 10: {cont10}')
print(f'Notas de 1: {cont1}')
