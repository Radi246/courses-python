def leiaint(msg):
    valido = False
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('Erro, valor inserido é invalido')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número')
            return 0



def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print('Erro, número real invalido')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu nao digitar esse número')
            return 0

