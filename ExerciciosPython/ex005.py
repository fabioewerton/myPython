#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input("Digite um número inteiro: "))
print('Baseado no número {}, seu antecessor é {} e seu sucessor é {}.'.format(n1, n1-1, n1+1))
