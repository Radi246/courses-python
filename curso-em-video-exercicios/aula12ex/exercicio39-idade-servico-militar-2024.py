from time import perf_counter

idade1 = int(input('Digite seu ano de nascimento '))
militar = 18
idade = 2024 - idade1

if idade < militar:
    anos_servir = militar - idade
    print(f'Falta {anos_servir} ano(s) para você se apresentar')

elif idade == militar:
    print('Está na hora de se apresentar')

else:
    tempo = idade - 18
    print(f'Já passou {tempo} ano(s) do seu alistamento')