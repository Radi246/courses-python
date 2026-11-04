print('\033[07;35mPrograma para contar de par em par\033[m')

inicio = str(input('Digite "a" para iniciar, digite qualquer outra coisa para encerrar para encerrar: '))

if inicio == 'a':
    for i in range(0, 52, +2):
        print(i)

else:
    print('\033[07;31mPrograma encerrado')