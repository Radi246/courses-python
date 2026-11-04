import time
from emoji import emojize
inicio = int(input('Digite o tempo para os fogos: '))

for i in range(inicio, 0, -1):
    print(f'\033[07;33m{i}')

    time.sleep(1)
print(emojize('\033[07;31mBoom :fireworks:'))