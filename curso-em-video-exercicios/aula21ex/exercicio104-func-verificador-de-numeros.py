def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mO valor digitado não é um número inteiro.\033[m')
        if ok:
            break
    return valor


numero = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {numero}')