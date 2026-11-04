numero = 0
valor = 0

for i in range(numero, 500):
     numero = numero + 1

     if numero % 2 != 0:
        if numero % 3 == 0:
            valor = valor + numero

print(valor)

#Programa para saber a soma de todos os números impares divisiveis por 3 de 0 até 500