from datetime import date
n1 = int(input('Diga o ano que quer analisar '))
if n1 == 0:
    n1 = date.today().year
if n1 % 4 == 0 and n1 % 100 or n1 % 400 == 0:
    print('O Ano {} é BISEXTO'.format(n1))
else:
    print('O ano {} nao é BISEXTO'.format(n1))