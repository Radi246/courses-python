temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Digite o seu nome: ')))
    temp.append((float(input('Digite o seu peso: '))))

    if len(princ) == 0:
        mai = men = temp[1]

    if temp[1] >= mai:
         mai = temp[1]
    if temp [1] <= men:
        men = temp[1]

    princ.append(temp[:])
    temp.clear()

    escolha = str(input('Quer continuar? S/N ')).upper()

    if escolha == 'N':
        break

print(f'Foram cadastrados {len(princ)} pessoas')

print(f'O maior peso foi de {mai}kg. De: ',end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print('')
print(f'O menor peso foi de {men}kg. De: ', end='')

for p in princ:
        if p[1] == men:
            print(f'[{p[0]}] ', end='')