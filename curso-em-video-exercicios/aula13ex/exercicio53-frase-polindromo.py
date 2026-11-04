def eh_palindramo(frase):
    frase_limpa = ''.join(caractere.lower() for caractere in frase if caractere.isalnum()) #

    return frase == frase_limpa[::-1] # O [::-1] irá contar as frases de trás pra frente

frase = input('Digite a frase para saber se é polidromo: ')

if eh_palindramo(frase): # Caso a frase for um palindromo, elá virá pra cá
    print('A frase é um polidromo!')
else: # Caso ela não for um palindromo, ela virá pra cá
    print('A frase não é um polidromo')