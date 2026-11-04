lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? S/N: ')).upper().strip()
    if escolha == 'N':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O número 5 está na lista. ')
else:
    print('O número 5 não está na lista. ')