#escreva um programa que leia um valor em metros e o exiba convertido em
#centimetros e milimetros 
metros=int(input('digite o valor em metros: '))
cm=metros*100
ml=metros*1000
print('o valor {} em centimetros é: {} em milimetros é: {}'.format(metros,cm,ml))