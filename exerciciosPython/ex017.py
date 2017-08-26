"""Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. """

from math import hypot

catOpo = float(input('comprimento do cateto oposto: '))
catAdj = float(input('comprimento do cateto adjacente: '))
hipo = hypot(catOpo, catAdj)

print('Se meu cateto oposto é {} e meu cateto adjacente é {}, então a minha hipotenusa é {:.2f}'.format(catOpo, catAdj, hipo))
