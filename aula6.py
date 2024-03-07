#Conversão de Tipos de Dados

#Exemplo de conversão de tipos de dados
print(int(11.0)) #float para int
print(float(11)) #int para float
print(str(11)) #int para string
print(bool(11)) #int para bool
print(bool(0)) #int para bool
print(bool(1)) #int para bool
print(bool(-1)) #int para bool
print(bool(0.0)) #float para bool
print(bool(0.1)) #float para bool
print(bool(0.0)) #float para bool
print(bool(0.1)) #float para bool
print(bool('')) #string para bool
print(bool(' ')) #string para bool
print(bool('0')) #string para bool
print(bool('1')) #string para bool
print(bool('False')) #string para bool
print(bool('True')) #string para bool
print(str(True)) #bool para string
print(str(False)) #bool para string
print(int(True)) #bool para int
print(int(False)) #bool para int
print(float(True)) #bool para float
print(float(False)) #bool para float

# Como declarar uma variável
aux = 1
auxString = '1'
print(aux + auxString) #TypeError: unsupported operand type(s) for +: 'int' and 'str'