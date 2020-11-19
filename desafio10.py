#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre  quantos dolares ela pode comprar
#considere: US$1.00=R$3.27
real=float(input('quantidade de dinheiro voce tem na carteira: '))
dolar=real/3.27
print('com R$ {:.2f} você pode comprar US${:.2f} '.format(real,dolar))