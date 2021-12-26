# calculadora 
# calculadora de média UAM

a1 = int(input('digite a nota 1'))
while a1>10:
    a1=int(input('você digitou uma nota errada!Entre com a nota correta.'))

a2 = int(input('digite a nota 2'))
while a2>10:
    a2=int ( input ( 'você digitou uma nota errada!Entre com a nota.' ))

a3 = int(input('digite a nota 3'))
while a3>10:
   a3= int ( input ( 'você digitou uma nota errada!Entre com a nota.' ))

a4 = int(input('digite a nota 4'))
while a4>10:
    a4=int ( input ( 'você digitou uma nota errada!Entre com a nota.' ))

p1 = int(input('digite a nota p1'))
while p1>10:
    p1=int ( input ( 'você digitou uma nota errada!Entre com a nota.' ))

s = (a1 + a2 + a3 + a4) / 4
N1 = (s / 100) * 40
N2 = (p1 / 100) * 60
M = N1 + N2

if M>=7:
    print('a média é {}!Você foi aprovado!'.format(M))
else:
    print('Bomba !!')
