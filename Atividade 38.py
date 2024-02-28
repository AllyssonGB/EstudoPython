n1 = float(input('Diga a distancia da sua viagem '))
n2 = n1 * 0.50
n3 = n1 * 0.45
if n1 <= 200:
    print('A viagem custara {}R$'.format(n2))
else:
    print('A viagem custara {}R$ em promoção'.format(n3))