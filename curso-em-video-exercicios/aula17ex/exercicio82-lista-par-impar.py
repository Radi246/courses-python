lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? S/N: ')).upper().strip()

    if escolha == 'N':
        break

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print('-=' *30)
print(f'Lista normal: {lista}')
print(f'Lista par: {lista_par}')
print(f'Lista impar: {lista_impar}')