#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
'''n=int(input('digite um numero: '))
a=n*0
b=n*1
c=n*2
d=n*3
e=n*4
f=n*5
g=n*6
h=n*7
i=n*8
j=n*9
k=n*10
print('a tabuada de {} é {} x 0 = {} \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {}\n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {} '. format(n,n,a,n,b,n,c,n,d,n,e,n,f,n,g,n,h,n,i,n,j,n,k))'''
#outra forma 
n=int(input('digite um numero: '))
print('-'*13)
print(' {} X {} = {} '.format(n,1,n*1))
print(' {} X {} = {} '.format(n,2,n*2))
print(' {} X {} = {} '.format(n,3,n*3))
print(' {} X {} = {} '.format(n,4,n*4))
print(' {} X {} = {} '.format(n,5,n*5))
print(' {} X {} = {} '.format(n,6,n*6))
print(' {} X {} = {} '.format(n,7,n*7))
print(' {} X {} = {} '.format(n,8,n*8))
print(' {} X {} = {} '.format(n,9,n*9))
print(' {} X {} = {} '.format(n,10,n*10))
print('-'*13)