perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

perguntas_certas = 0

for pergunta in perguntas:
    
    print("Pergunta: ", pergunta['Pergunta'])
    print("Opções: ")
    
    chave = 0
    chave_da_resposta = None
    
    for chave, opcao in enumerate(pergunta['Opções']):
        print(f'{chave}) {opcao}')
        if opcao == pergunta['Resposta']:
            chave_da_resposta = chave
    
    resposta = input('Escolha uma opção: ')
    
    try:
        resposta = int(resposta)
    except:
        print("Não foi possível fazer casting da resposta")
    
    if (resposta == chave_da_resposta):
        print('Você acertou!')
        perguntas_certas += 1
    else:
        print('Você errou')
        
print(f"Você acertou {perguntas_certas} de {len(perguntas)} perguntas.")
    
        
