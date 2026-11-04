nome = input('Digite seu nome completo\n')

separado = nome.split() #Separa os nomes

primeiro_nome = separado[0] #Acessa o primeiro elemento da lista
ultimo_nome = separado[-1] #Acessa o ultimo elemento da lista

print(f'{primeiro_nome} {ultimo_nome}')