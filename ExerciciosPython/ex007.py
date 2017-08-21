#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, (n1+n2)/2))
