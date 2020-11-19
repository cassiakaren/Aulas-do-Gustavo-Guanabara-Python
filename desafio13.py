#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salarioO=float(input('digite seu salario:'))
a=salarioO+(salarioO*15/100)
print('seu novo salario com 15% de aumento é: {:.2f}'.format(a))