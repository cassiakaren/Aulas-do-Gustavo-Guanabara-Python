#leia o preço do produto, e calcular qual o preço dele com desconto pra pagamento a vista, e com aumento pra parcelar
#se pagar a vista 10% de desconto
#se parcelar 8% de aumento
valor=float(input('digite o valor do produto: '))
avista=valor-(valor*10/100)
parcelado=valor+(valor*8/100)
print('para pagamento a vista com 10% de desconto seu produro custará R${:.2f}'.format(avista))
print('para pagamento parcelado será creditado em cima do valor do produto 8%, passando assim a custar: R${:.2f}'.format(parcelado))