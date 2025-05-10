frase = 'Ousareis passar muito para além da Taprobana'
def invert_pair(calculo_da_frase):
    len(calculo_da_frase)
    middle = len(calculo_da_frase) / 2
    middle = int (middle) #eu preciso transformar em int, porque o quando o Python realiza uma divisão ele apresenta um float como produto
    first = calculo_da_frase [:middle]
    second = calculo_da_frase [middle:]
    return second + first
print(invert_pair(frase))
#com o 'invert_pair' estou chamando a função
#com o 'frase' estou chamando a minha variável