import sys

nome = input('Digite seu nome: ')

if (not nome):
    print('Você não digitou nada')
    sys.exit()

contem_espacos = ...

if (' ' in nome):
    contem_espacos = 'Seu nome contém espaços'
else:
    contem_espacos = 'Seu nome não contém espaços'    

print(
    f'Seu nome é {nome}\n'
    f'Seu nome invertido é {nome[::-1]}\n'
    f'{contem_espacos}\n'
    f'Seu nome contém {len(nome)} letras\n'
    f'A primeira letra do seu nome é {nome[0]}\n'
    f'A última letra do seu nome é {nome[-1]}\n'
)