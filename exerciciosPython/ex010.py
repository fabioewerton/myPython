#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#http://dolarhoje.com/

real = float(input('Quanto dinheiro você tem na carteira: R$ '))
dolar = real/3.16
euro = real/3.74
libra = real/4.08
pesoA = real*5.56
iene = real*34.50
bitcoin = real/13514.24

line = '+'*35

print(line)
print('')
print('Com R$ {:.2f} você pode comprar:'.format(real))
print('')
print('{:>3} {:.2f}'.format('US$', dolar))
print('{:>3} {:.2f}'.format('€', euro))
print('{:>3} {:.2f}'.format('£', libra))
print('{:>3} {:.2f}'.format('$', pesoA))
print('{:>3} {:.2f}'.format('¥', iene))
print('{:>3} {:.2f}'.format('฿', bitcoin))
print('')
print(line)
