#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dia alugados ? '))
km = float(input('Km rodados ? '))
aPagar = (dias * 60) + (km * 0.15)

line = '\n' + '*' * 55 + '\n'

print(line)
print('Você precisa pagar R$ {:.2f} pelo aluguel do carro.'.format(aPagar))
print(line)