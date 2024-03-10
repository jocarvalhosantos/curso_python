"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = "python"
tentativas = 0
letras_digitadas = []

while True:
    letra = input("Digite uma letra: ")
    tentativas += 1

    if letra in letras_digitadas:
        print("Você já digitou essa letra. Tente novamente.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f"A letra '{letra}' está na palavra secreta!")
    else:
        print("*")

    if set(palavra_secreta) == set(letras_digitadas):
        print(f"Parabéns! Você acertou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas.")
        break
    