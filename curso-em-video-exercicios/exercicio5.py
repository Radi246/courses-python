largura = int(input('Digite a largura da parede\n'))
altura = int(input('Digite a altura da parede\n'))
tinta = 2

area = altura * largura
quantidade = area // tinta

print(f'A area total da parede é {area}. Você vai precisar de {quantidade} lata(s) de tinta(s)')