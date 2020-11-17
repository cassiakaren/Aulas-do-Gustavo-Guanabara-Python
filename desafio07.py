#Desenvolva um programa que leia as duas notas de um aluno, calcule  e mostre sua media.
#nota1=float(input('digite sua primeira nota: '))
#nota2=float(input('digite sua segunda nota: '))
#media=(nota1+nota2)/2
#print('sua media é igual a: {}'.format(media))
#opcional: desenvolba um programa que leia as quatro notas de um aluno, calcule sua media e imprima na tela se a media final
#for maior igual a 7 "aprovado", se nao "reprovado"
nota1=float(input('digite sua primeira nota:'))
nota2=float(input('digite sua segunda nota: '))
nota3=float(input('digite sua terceira nota:'))
nota4=float(input('digite sua quarta nota:'))
media=(nota1+nota2+nota3+nota4)/4
if media>=7:
    print('sua media é igual a: {} aprovado!!!'.format(media))
else:
    print('sua media é igual a: {} reprovado!!!'.format(media))