import datetime

nome = 'Jonas'
idade = 27
maior_de_idade = idade >= 18
altura_metros = 1.80
sobrenome = 'de Carvalho Santos'
ano_nascimento = datetime.datetime.now().year - idade

print('Nome', nome)
print('Sobrenome', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('Maior de Idade:', maior_de_idade)
print('Altura:', altura_metros)