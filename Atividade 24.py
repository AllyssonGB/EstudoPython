n1 = str(input('Digite seu nome completo')).strip()
print('Analisando seu nome...')
print('Seu nome com todas Letras Maisculas é {}'.format(n1.upper()))
print('Seu nome com todas Letras minusculas é {}'.format(n1.lower()))
print('A quantidade de letras no seu nome é {}'.format(len(n1) - n1.count(' ')))
print('O seu primeiro nome tem {} Letras'.format(n1.find(' ')))