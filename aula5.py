#Tipo de dado bool (booleano)
#True -> Verdadeiro
#False -> Falso

#Exemplo de operações com bool
print(True)
print(False)

print(type(True))
print(type(False))

print(10 == 10) #True
print(10 == 11) #False
print(10 != 11) #True
print(10 != 10) #False
print(10 > 11) #False
print(10 < 11) #True
print(10 >= 11) #False
print(10 <= 11) #True
print(10 >= 10) #True
print(10 <= 10) #True

print(10 == 10 and 10 == 11) #False
print(10 == 10 or 10 == 11) #True
print(not 10 == 10) #False
print(not 10 == 11) #True