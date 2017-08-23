#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário R$ '))
aumento = ((15/100) * salario) + salario

line = '\n' + ('*' * 100) + '\n'

print(line)

print('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {:.2f}.\n'.format(salario, aumento))

print('Descrição'.upper())
print('Salário: R$ {:.2f};\nAumento: R$ {:.2f};\nTotal  : R$ {:.2f}.'.format(salario, (15/100) * salario, aumento))

print(line)