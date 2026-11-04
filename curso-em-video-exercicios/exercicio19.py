import random

aluno1 = 'João'
aluno2 = 'Paulo'
aluno3 = 'Pedro'
aluno4 = 'Evaristo'
alunos = [aluno1, aluno2, aluno3, aluno4] #cria uma lista dentro dos alunos

aluno = random.choice(alunos) #Irá escolher aleatóriamente um aluno da lista criada acima

print(aluno)

random.shuffle(alunos)
for alunin in alunos:
    print(alunin)