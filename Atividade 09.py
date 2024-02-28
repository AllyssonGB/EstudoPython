from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Pensei em um numero entre 0 é 5 tente adivinha')
print('-=-' * 20)
jogador = int(input('Diga o numero que estou pensando: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens o numero que eu pensei era {} voce ganhou'.format(computador))
else:
    print('Voce errou o numero era {}'.format(computador))
