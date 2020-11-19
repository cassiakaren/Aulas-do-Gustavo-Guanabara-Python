#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
valorO=float(input('digite o valor: '))
a=valorO-(valorO*5/100)
print('o novo valor com 5% de desconto será: {:.2f}'.format(a))