temp = []
princ = []
mai = men = 0
while True: #Começa um loop que vai contiar até a pessoa falar não
    temp.append(str(input('Nome: '))) #Guarda o nome temporariamente
    temp.append(float(input('Peso: '))) #Guarda o peso temporariamente
    if len(princ) == 0: #Na primeira vez, ele entrará aqui
        mai = men = temp[1] #E colocara o primeiro peso digitado como parametro de menor ou maior
    else: #Caso não for a primeira vez
        if temp[1] > mai: #Ele vê se o peso digitado é maior
            mai = temp[1] #Se for, ele salva
        if temp[1] < men: #Aqui verifica se é menor.
            men = temp[1] #Se for, ele salva
    princ.append(temp[:]) #Aqui ele faz uma cópia
    temp.clear() #E depois ele limpa a memória temporaria
    escolha = str(input('Quer continuar? S/N ')).upper() #Uma escolha com Upper
    if escolha == 'N': #Se a escolha for 'n',  a repetição se encerra
        break
print(f'Foram cadastradas {len(princ)} pessoas') #Conta o len da memoria principal
print(f'O maior peso foi de {mai}kg. Peso de: ', end='') #Pega o maior peso salvo
for p in princ: #Vai verificar todos os pesos pra ver se tem alguem com peso igual
    if p[1] == mai: #Se tiver...
        print(f'{p[0]} ', end='') #Ele coloca ao lado da frase
print('') #Linha em branco

print(f'O menor peso foi de {men} de: ', end='') #Pega o menor peso salvo e printa
for p in princ: #Procura por alguém que tenha o menor pesa igual
    if p[1] == men: #Se tiver...
        print(f'{p[0]} ', end='') #Ele mostra as pessoas com esses mesmos pesos