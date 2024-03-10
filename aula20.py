primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

primeiro_valor_maior_que_segundo_valor = primeiro_valor > segundo_valor

if (primeiro_valor_maior_que_segundo_valor):
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif (not primeiro_valor_maior_que_segundo_valor):
    print(f'{segundo_valor} é maior que {primeiro_valor}')
else:
    print(f'{primeiro_valor} é igual a {segundo_valor}')
    