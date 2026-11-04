from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for i in n:
    print(f'{i} ', end='')