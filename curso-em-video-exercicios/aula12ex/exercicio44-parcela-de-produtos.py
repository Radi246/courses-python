# Entrada do preço do produto
preco = float(input("Qual o preço do produto?: "))

# Entrada da forma de pagamento
formaDePgmt = int(input("""\nQual a condição do pagamento?
1 - À vista, 10% de desconto
2 - À vista no cartão, 5% de desconto
3 - Em 2x no cartão, preço normal
4 - Em 3x ou mais no cartão, 20% de juros
Escolha uma opção: """))

# Tratamento das opções de pagamento
if formaDePgmt == 1:
    valor = preco * 0.90
    print(f"Você ganhou 10% de desconto. O preço do produto será de R${valor:.2f}.")

elif formaDePgmt == 2:
    valor = preco * 0.95
    print(f"Você ganhou 5% de desconto. O preço do produto será de R${valor:.2f}.")

elif formaDePgmt == 3:
    parcela = preco / 2
    print(f"Você pagará R${preco:.2f} em duas parcelas de R${parcela:.2f}.")

elif formaDePgmt == 4:
    qtparcelas = int(input("Em quantas vezes?: "))

    if qtparcelas < 3:
        print("Erro: A quantidade mínima de parcelas para esta opção é 3.")
    else:
        valor = preco * 1.20
        valor_parcela = valor / qtparcelas
        print(
            f"O valor do produto será de R${valor:.2f}, dividido em {qtparcelas} parcelas de R${valor_parcela:.2f} cada.")

else:
    print("Erro: Opção de pagamento inválida.")
