def fatorial(n, show=False):
    """

    :param n: O valor a ser calculado
    :param show: Este parâmetro é opcional. Por padrão, ele estará com o valor False
    :return: Retorna o resultado da conta
    Criado por: Radi
    """

    f = 1

    for c in range(n, 0, -1):
        if show:
            print(c, end='')

            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')

        f *= c

    return f

print(fatorial(5, show=False))