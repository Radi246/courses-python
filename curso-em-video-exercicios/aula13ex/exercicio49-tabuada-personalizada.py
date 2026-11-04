numero = int(input('Escreva um número inteiro para a tabuada '))
comeco = int(input('Agora, escolha o número de começo '))
final = int(input('Agora, escolha um número final '))

for i in range(comeco, final+1):
    resultado = numero * comeco
    print(f'{numero} x {comeco} = {resultado}')
    comeco = comeco + 1

#Programa para fazer tabuadas