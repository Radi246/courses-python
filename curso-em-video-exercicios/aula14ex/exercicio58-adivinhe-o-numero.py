import random

num = random.randint(0, 10)
contador = 0
escolha = int

while escolha != num:
    escolha = int(input('Adivinhe o número que a maquina está pensando: '))
    if escolha != num:
        print('\033[31mEsse não é o número certo\033[m')
        contador += 1
print(f'Você acertou depois de tentar \033[31m{contador} vezes.')