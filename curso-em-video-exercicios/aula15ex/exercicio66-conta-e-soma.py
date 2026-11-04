n = s = c = 0
while n != 999:
    n = int(input('Digite um número: '))

    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} números, a soma deles foi {s}')