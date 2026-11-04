valores = [] #Uma lista vazia é criada

for i in range(5): 
    n = int(input('Digite um valor: '))
    if i == 0 or n > valores[-1]: #Na primeira vez, ele vai colocar um número. Se o N for menor que o ultimo valor da lista, ele vai adicionar um valor por ultimo
        valores.append(n) #Adiciona no fim da lista

    else: #Caso não for maior que o último valor, então ele vai verificar um por um se o n é menor que o valor
        pos = 0 #Começa o contador
        while pos < len(valores): #Conta até a quantidade de valores dentro da lista
            if n <= valores[pos]: #Se o item da lista for menor que o N, então...
                valores.insert(pos, n) #Ele vai inserir um valor naquela posição do item
                break
            pos += 1 #Adiciona mais um ao contador
print('-=' *30)
print(valores) #Imprime os valores em ordem crescente