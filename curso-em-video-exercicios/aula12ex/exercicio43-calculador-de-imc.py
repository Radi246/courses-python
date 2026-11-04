peso = float(input('Digite o seu peso '))
altura = float(input('Digite a sua altura '))

imc = peso / (altura**2)
print(imc)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Seu peso está ideal')
elif imc <=30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está obeso')
elif imc > 40:
    print('Você está com obesidade morbida')