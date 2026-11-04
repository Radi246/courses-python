import random

escolha = int(input('Escolha entre: pedra(1), papel(2) ou tesoura(3)\n'))

if escolha not in [1, 2, 3]:
    print('Escolha invlida, tente novamente.')

else:
    opcoes = ['Pedra', 'Papel', 'Tesoura']

    escolha_pc = random.randint(1,3)

    print(f'Você escolheu: {opcoes[escolha - 1]}')
    print(f'O computador escolheu {opcoes[escolha_pc - 1]}')

    if escolha == escolha_pc:
        print('\033[7;34mEmpate')

    elif (escolha == 1 and escolha_pc == 3) or \
         (escolha == 2 and escolha_pc == 1) or \
         (escolha == 3 and escolha_pc == 2):
        print('\033[7;32mVocê ganhou')

    else:
        print('\033[7;31mO computador ganhou')

