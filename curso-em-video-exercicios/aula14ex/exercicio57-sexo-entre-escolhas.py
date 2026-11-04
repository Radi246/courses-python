sx = str
while sx != 'F' and sx != 'M' :
    sx = input('Digite um sexo de nascimento, F/M: ').upper()
    if sx != 'F' and sx != 'M':
        print('Digite um sexo entre F/M.')