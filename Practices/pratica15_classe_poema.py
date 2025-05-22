class Poema:
    def __init__(self, titulo, autor, versos):
        self.titulo = titulo
        self.autor = autor
        self.versos = versos
    def contar_versos(self):
        quantidade_de_versos = len(self.versos)
        print(f'O poema tem {quantidade_de_versos} versos!')
    def mostrar_poema(self):
        print('~'*30)
        print(f'{self.titulo} - {self.autor}')
        print('~' * 30)
        for verso in self.versos:
            print(verso)

texto = Poema('Amor','Álvares de Azevedo',['Descansem o meu leito solitário','Na floresta dos homens esquecida,','À sombra de uma cruz, e escrevam nela:','Foi poeta - sonhou - e amou na vida.'])
texto.contar_versos()
texto.mostrar_poema()