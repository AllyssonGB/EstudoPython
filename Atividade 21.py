import random
n1 = input('Diga o nome do primeiro Aluno')
n2 = input('Diga o nome do segundo Aluno')
n3 = input('Diga o nome do terceiro Aluno')
n4 = input('Diga o nome do Quarto Aluno')
s = (n1,n2,n3,n4)
print('O aluno escolhido foi {}'.format(random.choice(s)))
