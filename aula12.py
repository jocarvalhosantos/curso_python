nome = "Jonas de Carvalho Santos"
altura = 9841189469.63366469
peso = 120

imc = peso / (altura ** 2)

acima_do_peso = imc >= 25

print (nome, "tem", altura, "de altura e seu IMC é", imc, "e está acima do peso?", acima_do_peso)

print (nome, "tem", altura, "de altura e seu IMC é", imc)

#utilizando o f-string
print (f'{nome} tem {altura:.2f} de altura e seu IMC é {imc:.2f} e está acima do peso? {acima_do_peso}')



