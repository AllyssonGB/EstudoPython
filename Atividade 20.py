import math
angulo = float(input('Digite um angulo?'))
a = math.radians(angulo)
print('O angulo de {} tem o COSENO {:.2f}'.format(angulo,math.cos(a)))
print('O angulo de {} tem o SENO {:.2f}\nO angulo de {} tem o TANGENTE de {:.2f}'.format(angulo,math.sin(a),angulo,math.tan(a)))

