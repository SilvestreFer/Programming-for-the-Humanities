import matplotlib.pyplot as plt
class MeuGrafico:
  def __init__(self, titulo):
    self.titulo = titulo

  def desenhar(self):
    plt.figure(figsize=(6, 4))
    plt.title(self.titulo)
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
meu_grafico = MeuGrafico('Meu próprio gráfico')
meu_grafico.desenhar()
