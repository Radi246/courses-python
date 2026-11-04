peso_maior = 0
peso_menor = 0

for i in range(6): #Vai pegar 6 pesos
    peso = float(input('Qual o seu peso?: '))

    if i == 0: # Inicia o valor do menor e do maior na primeira iteração
        peso_menor = peso
        peso_maior = peso
    else:
        if peso > peso_maior: # Atualiza o maior valor
            peso_maior = peso
        if peso < peso_menor: # Atualiza o menor valor
            peso_menor = peso

    print(peso_menor)
print(f'Maior peso: {peso_maior:.2f}kg \nMenor peso: {peso_menor:.2f}kg')