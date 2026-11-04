def ajuda():
    while True:
        print('\033[42m~'*40)
        print(' SISTEMA DE AJUDA PyHELP')
        print('~'*40)
        func = str(input('\033[mFuncção ou biblicoteca > '))

        if func == 'quit':
            return
        print('\033[44m~'*40)
        print(f' Acessando o manual do comando "{func}"')
        print('~' * 40)
        print('\033[m')
        print('\033[7m')
        print(help(func))
        print('\033[m')


ajuda()