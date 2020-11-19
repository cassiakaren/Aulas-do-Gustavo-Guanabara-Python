#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua sua area e a quantidade de tinta necessária para pinta-la
#sabendo que cada litro de tinta pinta uma área de 2m²
largura=float(input('digite a largura da parede em metros : '))
altura=float(input('digite a altura da parede em metros : '))
area= altura*largura
print('sua parede tem a dimensão de {}x{} e sua area é de {} m²'.format(largura,altura,area))
tinta= area/2
print('para pintar essa parede voce precisa de {}l de tinta'.format(tinta))