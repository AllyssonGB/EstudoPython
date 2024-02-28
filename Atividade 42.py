print('=-' * 20)
print('Analisador de Triangulos')
print('=-' * 20)
n1 = float(input('Digite primeiro seguimento '))
n2 = float(input('Digite segundo seguimento '))
n3 = float(input('Digite terceiro seguimento '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('Sim esses seguimentos forma um triangulo')
else:
    print('Nao esses seguimentos nao forma um triangulo')