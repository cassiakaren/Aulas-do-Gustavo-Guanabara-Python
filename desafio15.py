#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('quantidade de km percorridos: '))
q=int(input('quantidade de dias alugado: '))
valor=(q*60)+(km*0.15)
print('total a ser pago:{:.2f}'.format(valor))