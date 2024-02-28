n1 = int(input('Primeiro Valor '))
n2 = int(input('Segundo Valor '))
n3 = int(input('Terceiro Valor '))
# Verificando quem é menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O Menor Numero Escolhido foi {}'.format(menor))
# Verificando quem e Maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O Maior Numero Escolhido Foi o {}'.format(maior))
