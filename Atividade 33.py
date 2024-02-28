n1 = str(input('Qual seu nome completo?')).strip()
n2 = n1.split()
print('Foi 1 prazer te conhecer {}..'.format(n1))
print('Seu primeiro nome é {}'.format(n2[0]))
print('Seu ultimo nome é {}'.format(n2[len(n2)-1]))

