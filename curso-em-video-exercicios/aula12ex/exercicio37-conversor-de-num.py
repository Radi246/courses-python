numero = int(input('Digite um numero '))

escolha = input("""\nEscolha uma conversão\n
Binario = 1
Octal = 2
Hexadecimal = 3
""")

if escolha == '1':
    print(f'\nBinario: {bin(numero)}')

elif escolha == '2':
    print(f'Octal: {oct(numero)}')

elif escolha =='3':
    print(f'Hexadecimal {hex(numero)}')

else:
    print('Impossivel prosseguir, algo deu errado.')