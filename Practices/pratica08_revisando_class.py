class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    def passar_de_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')

controle_preto = ControleRemoto('preto', '10cm','2cm', '2cm')
print(f'A cor do controle é {controle_preto.cor}.')
controle_preto.passar_de_canal('+')

controle_cinza = ControleRemoto('cinza','8cm','2cm','2cm')
print(f'A altura do controle é {controle_cinza.altura}.')
controle_cinza.passar_de_canal('-')
