n1 = float(input('Quantos dias o carro foi alugado?'))
n2 = float(input('Quantos KM voce andou nele'))
s = (n1*60)+(n2*0.15)
print('Voce Rodou {} KM e alugou o carro por {} dias e o total a pagar e {:.2f}'.format(n1,n2,s))