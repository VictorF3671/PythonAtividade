import random

palavras = ["Celta", "Siena", "Gol", "Corsa", "Onix", "Kwid", "Hilux"]
palavra = random.choice(palavras).lower()

letras_adivinhadas = ['_' for _ in palavra]
max_tentativas = 7
tentativas = 0



while tentativas < max_tentativas:
    print(' '.join(letras_adivinhadas))
    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        tentativas += 1

    if '_' not in letras_adivinhadas:
        print("Você Acertou")
        break
else:
    print("Você Errou, A palavra era " + palavra)