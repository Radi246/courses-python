num = 0
rasultado = int
while num != 5:

    if num == 4 or num == 0:  # Para a primeira vez ou escolha "Novos Números"
        val1 = int(input('Digite o primeiro valor: '))
        val2 = int(input('Digite o segundo valor: '))


    print("\nMenu de Operações:")
    num = int(input('O que você quer fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair\n'))



    if num == 1:
        resultado = val1 + val2
        print(f'A soma é {resultado}')
        break

    elif num == 2:
        resultado = val1 * val2
        print(f'O resultado da multiplicação é {resultado}')
        break

    elif num == 3:
        if val1 > val2:
            print(f'{val1} é o maior valor')
            break
        else:
            print(f'{val2} é o maior valor')
            break

    elif num == 4:
        print('Digite os números novamente.')

print('Programa encerrado')