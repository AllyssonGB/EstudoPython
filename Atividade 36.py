n1 = int(input('Diga a velocidade em KM que vocé esta dirigindo '))
if n1 <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    multa = (n1-80) * 7
    print('MULTADO , Voce exedeu o limite maximo de Velocidade que é de 80KM é foi mutado em {:.2f}R$'.format(multa))
    print('Tenha um bom dia Dirija com segurança')