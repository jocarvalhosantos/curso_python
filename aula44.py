numeros = range(0, 10, 3)
print(numeros)

for valor in numeros:
    print(valor)
    

    # Iterável: Um objeto que pode ser percorrido ou iterado.
    # Exemplo: Uma lista, uma string, um dicionário.

    # Iterador: Um objeto que implementa o método __next__() e mantém o estado da iteração.
    # Exemplo: A função iter() retorna um iterador para um objeto iterável.

    # next(): Uma função que retorna o próximo elemento de um iterador.
    # Exemplo: Utilizado para obter o próximo valor de um iterador.

    # iter(): Uma função que retorna um iterador para um objeto iterável.
    # Exemplo: Utilizado para criar um iterador a partir de um objeto iterável.

    numeros = range(0, 10, 3)
    print(numeros)

    # Iterando sobre o objeto iterável
    for valor in numeros:
        print(valor)

    # Criando um iterador a partir do objeto iterável
    iterador = iter(numeros)

    # Obtendo o próximo elemento do iterador
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))