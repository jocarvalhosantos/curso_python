a = 'A'
b = 'B'
c = 1.1

formato = 'a={0} b={1} jonas={2:.2f}'

print(formato.format(a, b, c))


#Parâmetros nomeados
a = 'A'
b = 'B'
c = 1.1

formato = 'a={nome1} b={nome2} jonas={nome3:.2f}'

print(formato.format(nome1=a, nome2=b, nome3=c))

