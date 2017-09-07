"""Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""
from random import choice
a1 = input('Aluno um: ')
a2 = input('Aluno dois: ')
a3 = input('Aluno três: ')
a4 = input('Aluno quatro: ')

print('O aluno escolhido foi {}!'.format(choice([a1, a2, a3, a4])))
