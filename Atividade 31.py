n1 = str(input('Diga seu nome completo')).upper()
print('O seu nome tem {} de Letras A'.format(n1.count('A')))
print('A letra A aparece a primeira vez no seu nome na {} pocisão'.format(n1.find('A')+1))
print('A ultima letra A aparece na pocisão {}'.format(n1.rfind('A')+1))