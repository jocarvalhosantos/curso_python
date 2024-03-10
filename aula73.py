#higher order functions
#funções de alta ordem

def dobro(x):
    return x*2

def triplo(x):
    return x*3

def quadrado(x):
    return x**2

def aplicar(funcao, lista):
    return [funcao(x) for x in lista]

lista = [1,2,3,4,5]

print(aplicar(dobro, lista))