n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
s = n1+n2
m = n1-n2
v = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('Os Resultados São Adição:{} Subtração:{} Divisão:{:.3f} Multplicação:{}'.format(s,m,d,v), end=' ')
print('DInteira:{} Potencia:{}'.format(di,p))