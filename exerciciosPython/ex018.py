"""Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo. """

from math import radians, sin, cos, tan
ang = float(input("Digite um angulo que você deseja: "))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print("O ângulo de {} tem o SENO de {:.2f}!".format(ang, seno))
print("O ângulo de {} tem o COSENO de {:.2f}!".format(ang, coss))
print("O ângulo de {} tem a TANGENTE de {:.2f}!".format(ang, tang))
