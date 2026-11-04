def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2): #Ele irá começar do 3, um número primo até a raiz do número colocado, pulando de 2 em 2
        resultado = numero % i
        print(resultado)

        if numero % i == 0: # Aqui ele irá verificar se um número é primo pela sua divisão, se ele tiver divisão exata até chegar na sua raiz, então ele não é primo
            return False # Se ele não for primo, ele retornará falso
    return True # Mas se ele for primo, ele retornará positivo

# Teste
n = int(input('Digite um número: '))
if eh_primo(n): #Caso for positivo (primo), ele entra aqui
    print(f'{n} é um número primo')
else: #Caso ele não for positivo (um não primo), ele entra aqui
    print(f'{n} não é um número primo')

# Esse programa vai testar se os números são primos ou não
# Admito que não entendi muito bem por haver muita matematica
# O programa irá tentar encontrar se há alguma divisão exata até sua raiz, caso não encontrar, ele sera retornado como True