n1 = float(input('Digite qual seu salario atual R$ '))
if n1 <= 1200:
    n2 = n1 + (n1 * 15/100)
else:
    n2 = n1 + (n1 * 10/100)
print('O seu salario com o reajuste ficou de {:.2f}R$'.format(n2))