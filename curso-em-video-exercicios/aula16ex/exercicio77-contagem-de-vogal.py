palavras = ('ola', 'carro', 'sapato', 'mouse', 'arroz', 'feijao',
            'teclado', 'mosquito')
sequencia = ''

for i in palavras:
    for x, letras in enumerate(i):
        if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
            sequencia += f'{letras}'
    print(f'A palavra {i} tem {sequencia}')
    sequencia = ''
