numEs = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))

    if escolha in range(0, 21):
        print(f'Você digitou {numEs[escolha]}')

    else:
        print('Número invalido, digite novamente. ')