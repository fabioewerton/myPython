#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
a = input('Digite algo: ')

print('O tipo primitivo de {} é {}!'.format(a, type(a)))
print(a, 'só tem espaços ?: ', a.isspace())
print(a, 'é numérico ?: ', a.isnumeric())
print(a, 'é alfanumético ?: ', a.isalnum())
print(a, 'é só letra ?: ', a.isalpha())
print(a, 'é só minuscula ?: ', a.islower())
print(a, 'é so maiuscula ?: ', a.isupper())
print(a, 'é Capitalizado ?: ', a.istitle())
