def duplicar(x):
    def triplicar():
        def quadruplicar():
            return x * 4
        return quadruplicar
    return triplicar

# Cria um closure que quadruplica o número 2
quadruplicar_dois = duplicar(2)()

# Usa o closure para obter o resultado
resultado = quadruplicar_dois()
print(resultado)  # Saída: 8