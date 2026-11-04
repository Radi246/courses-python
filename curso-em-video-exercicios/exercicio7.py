salario = int(input('Qual o seu salario?\n'))
porcento = int(input('Quanto porcento ira receber de aumento?\n'))

novo = porcento / 100
valor = salario * novo
final = salario + valor

print(f'Seu novo salario será de {final}')