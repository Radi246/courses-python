num = int(input('Digite um número: '))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[32m', end='')
    print(f'{i} ', end='')

print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')