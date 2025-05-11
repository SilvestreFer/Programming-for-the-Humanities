import matplotlib.pyplot as plt

class Texto:
  def __init__(self, texto):
    self.texto = texto
  def desenhar(self):
    plt.figure(figsize=(6,4))
    plt.bar(['ele', 'sabia', 'que'], [5, 6, 4])
    plt.xlabel('Frequência')
    plt.ylabel('Palavras')
    plt.title('Frequência das palavras no texto')

meu_texto = Texto("ele disse que ele tinha dito que não sabia como ele sabia, mas sabia que ele sabia que ele sabia e sabia de tudo.")
meu_texto.desenhar()
