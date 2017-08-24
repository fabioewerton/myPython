#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite uma temperatura em ºC: '))
f = (9 / 5) * c + 32
line = ('*') * 30

print('A temperatura de {}ºC corresponde a {}ºF !'.format(c, f))