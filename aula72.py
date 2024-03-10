def multiplica_varios_numeros(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

resultado_multiplicacao = multiplica_varios_numeros(1, 2, 3, 4, 5)
print(resultado_multiplicacao)  # 120



def par_ou_impar(numero):
    return f'{numero} é Par' if numero % 2 == 0 else f'{numero} é Ímpar'

print(par_ou_impar(5))  # Par