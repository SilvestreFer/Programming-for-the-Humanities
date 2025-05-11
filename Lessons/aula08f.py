import matplotlib.pyplot as plt

class Cadeira:
  def __init__(self, cadeiras, partidos):
     self.chair = cadeiras
     self.party = partidos

  def gerar_grafico(self):
    plt.figure(figsize=(6, 4))
    plt.pie(self.chair, None, self.party)
    plt.show()

grafico_de_pizza=Cadeira([7, 5, 15, 1, 22], ['Partido_01', 'Partido_02', 'Partido_03', 'Partido_04', 'Partido_05'])
grafico_de_pizza.gerar_grafico()
