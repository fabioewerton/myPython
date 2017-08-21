#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número inteiro: '))

print("O número informado foi {}\nLogo...\nSeu dobro é {}\nE seu triplo é {}\nE sua raiz quadrada é {:.2f}".format(n1, n1*2, n1*3, n1**(1/2)))
