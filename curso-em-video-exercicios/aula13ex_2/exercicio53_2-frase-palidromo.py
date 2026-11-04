frase = str(input('Digite uma frase: ')).strip().upper() #Tira os espaços externos e deixa tudo em maiusculo
palavras = frase.split() #Cria uma lista e joga para as apalavras
junto = ''.join(palavras) #Junta a lista sem os espaços internos
inverso = ''

for letra in range(len(junto)-1, -1, -1): #Vai contar da última até a primeira
    inverso += junto[letra] #Vai juntando as letras de trás para frente
    print(f'{inverso}')
if inverso == junto: #Verifica se a frase é igual
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')