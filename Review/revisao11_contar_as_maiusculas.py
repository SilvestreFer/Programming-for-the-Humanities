def conta_maiusculas(frase):
    contador = 0
    for letra in frase:
        if letra.isupper():
            contador += 1
    print(f'A frase tem {contador} letras maiúsculas.')

conta_maiusculas("Linguística Computacional é TOP!")
