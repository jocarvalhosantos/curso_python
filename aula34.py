nome = '*L*u*i*z *O*t*á*v*i*o'

tamanho_nome = len(nome)

contadorAux = 0

nome_junto = ''

while (contadorAux != tamanho_nome):
    if (nome[contadorAux]!='*'):
        nome_junto = nome_junto + nome[contadorAux]
    contadorAux += 1

print(nome_junto)

