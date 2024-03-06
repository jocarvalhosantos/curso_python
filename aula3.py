"""_summary_
Python - Aula 3 - 23/03/2021
Tipo de tipagem = dinâmica / forte
str -> string -> texto
int -> inteiro -> número inteiro
float -> número decimal
bool -> booleano -> True / False
"""

#aspas simples
print(1, 'aspas simples')

#aspas duplas
print(2, "aspas duplas")

#escape de aspas
print(3, "Jonas \"O Brabo\"") #O funcionamento do escape é que ele lê o caractere seguinte como um caractere comum, e não como um caractere especial

#r antes da string
print(4, r"Jonas \"O Brabo\"") #O r antes da string faz com que o Python ignore os caracteres especiais, utilizado muito em expressões regulares

#Outra maneira, é utilizar aspas simples e duplas juntas
print(5, 'Jonas "O Brabo"')