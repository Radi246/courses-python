minimo1 = maximo1 = 0
posi1 = posi2 = 0

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


maximo = minimo = valores[0]

for a,b in enumerate(valores):
    if b > maximo:
        maximo = b
        posi1 = a
    if b < minimo:
        minimo = b
        posi2 = a
print(f'O maior valor foi {maximo} na posição {posi1}. O menor foi {minimo} na posição {posi2}')
