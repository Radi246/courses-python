expressão = str(input('Digite um valor: '))
pilha = []

for i in expressão: #Vai passar por cada elemento da expressão
    if i == '(': #Caso houver um abre parenteses na expressão...
        pilha.append('(') #Ele vai adicionar um parentese na lista
    elif i == ')': #Até chegar aos fechas parenteses
        if len(pilha) > 0: #Caso a lista não tiver vazia...
            pilha.pop() #Ele vai tirar um elemento da lista
        else:
            pilha.append(')') #Caso acontecer de de ter mais um fecha parenteses, ele será adionado a lista
if len(pilha) == 0: #Se a lista estiver vazia, deu tudo bom
    print('Correto')
else: #Senão...
    print('Errado')