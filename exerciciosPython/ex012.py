#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$ '))
desconto = (5/100) * preco
novoPreco = preco-desconto

line = '\n' + ('*' * 100) + '\n'

print(line)
print('O produto que custava R$ {:.2f}, na promoção com 5% de desconto, vai custar R$ {:.2f}'.format(preco, novoPreco))
print(line)
