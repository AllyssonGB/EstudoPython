import random
import math
from playsound import playsound
n1 = float(input('Por favor diga um Angulo'))
C = math.cos(math.radians(n1))
S = math.sin(math.radians(n1))
T = math.tan(math.radians(n1))
print('O Cosseno Desse Angulo é {:.2f}\nO Seno Desse Angulo é {:.2f}\nO Tangente desse angulo é {:.2f}'.format(C, S, T))
n2 = str(input('Agora me diga o nome de 1 Aluno'))
n3 = str(input('Agora de outro aluno'))
n4 = str(input('E mais um'))
C2 = [n4, n2, n3]
random.shuffle(C2)
print('A ordem de apresentar o trabalho e essa')
print(C2)
p1 = float(input('diga um numero'))
p2 = float(input('diga outro numero'))
print('A sua media é {}'.format(math.floor((p1+p2)/2)))
playsound('teste.mp3')
