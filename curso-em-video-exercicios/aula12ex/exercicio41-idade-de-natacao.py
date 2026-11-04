idade = int(input('Digite a sua idade para a natação. '))

if idade < 9:
    print(f'Com {idade} anos de idade, vai competir na categoria mirim')

elif idade < 14:
    print(f'Para {idade} anos idade, ira competir no infantil')

elif idade < 19:
    print(f'Para quem tem {idade} anos de idade, irá competir no junior')

elif idade < 21:
    print(f'Para quem tem {idade} anos de idade, vai competir no senior')

else:
    print('Para pessoas superiores, irão competir no master')