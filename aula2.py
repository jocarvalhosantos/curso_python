#\r\n é o caractere de quebra de linha no Windows
# \n é o caractere de quebra de linha no Unix

print(12, 34, sep="-", end='\n##') # Imprime a mensagem "12 13" no console
print(56, 78, sep="-", end='\n')
print(12, 34, sep="-", end='\r\n##') # Imprime a mensagem "12 13" no console
print(56, 78, sep="-", end='\r\n')

