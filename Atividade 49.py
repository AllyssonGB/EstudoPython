somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor = 0
for c in range(1,5):
    print('\033[33m=-=-=-=-= {}º Pessoa =-=-=-=-='.format(c))
    nome = str(input('Qual seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo [F/M]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 19:
        mulhermenor += +1
print('A soma da idade de todos os membros do grupo é {} anos.'.format(somaidade))
mediaidade = somaidade / 4
print('A media da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos é o nome dele é {}'.format(maioridadehomem, nomevelho))
print('Quantidade de mulheres menores de idade são de {}'.format(mulhermenor))