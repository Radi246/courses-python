frase = input('Digite uma frase\n').lower()

quantidade_a = frase.count('a')

primeira_pose = frase.find('a') + 1
ultima_posi = frase.rfind('a') + 1 #Encontra a posição da última ocorrência da letra 'a'

print(f'A frase tem {quantidade_a} de letras "A", aparecendo pela primeira vez na posiçaõ {primeira_pose} e pela ultima na posição {ultima_posi}')


