#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = 2
line = '\n' + ('*' * 100) + '\n'

print(line)
print('Sua parede tem dimensão de {}m x {}m então sua área mede {}m².'.format(larg, alt, area))
print('Para pintar essa área da parede, você precisará de {:.3f}l de tinta.'.format(area/tinta))
print(line)
