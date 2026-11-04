casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos vai pagar? '))

meses = 12 * anos
prestacao = casa / meses

limite = salario * 0.3

print(f'A prestação sera de {prestacao:.2f}')
print(f'O limite é de {limite:.2f}')

if prestacao <= limite:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')