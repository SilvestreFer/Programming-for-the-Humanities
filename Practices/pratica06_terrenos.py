def titulo(mensagem):
   print('-' * 30)
   print(mensagem)
   print('-' * 30)

def tamanho_de_terreno(largura, comprimento):
   area = largura * comprimento
   print(f'A área de um terreno {largura} x {comprimento} é de {area} metros quadrados')

#Programa principal:
titulo('CONTROLE DE TERRENOS')
tamanho_de_terreno(largura = float(input('LARGURA (m): ')), comprimento = float(input('COMPRIMENTO (m): ')))
