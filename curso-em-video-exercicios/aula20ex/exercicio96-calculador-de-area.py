def area(a, b):
    resultado = b * a
    print(f'A área do terreno do terreno {b}x{a} é de {resultado:.2f}m2.')

#Programa principal
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(comp, lar)