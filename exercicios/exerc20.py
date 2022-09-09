import random 
al1 = str(input('Nome do aluno a ser sorteado: '))
al2 = str(input('Nome do aluno a ser sorteado: '))
al3 = str(input('Nome do aluno a ser sorteado: '))
lista = [al1, al2, al3]
random.shuffle(lista)
print(lista)