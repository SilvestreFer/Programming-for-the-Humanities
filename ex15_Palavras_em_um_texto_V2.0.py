import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Texto:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def calcular_frequencia(self):
        palavras = self.conteudo.lower().split()
        frequencia = {}
        for palavra in palavras:
          frequencia[palavra] = frequencia.get(palavra, 0) + 1
        return frequencia

    def gerar_grafico(self):
        freq = self.calcular_frequencia()
        df = pd.DataFrame(freq.items(), columns=['Palavras', 'Frequência']).sort_values(by='Frequência', ascending=False)[:10]

        plt.figure(figsize=(8, 5))
        sns.barplot(x="Frequência", y="Palavras", data=df, hue="Palavras", palette="Blues_r", legend=False)
        plt.title(f'Frequência das Palavras - {self.titulo}')
        plt.show()

texto_exemplo = Texto ("Frase", "ele disse que ele tinha dito que não sabia como ele sabia, mas sabia que ele sabia que ele sabia e sabia de tudo.")
texto_exemplo.gerar_grafico()
