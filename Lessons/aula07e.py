class Artigo:
    def __init__(self, autor, titulo, revista, edicao, publicacao):
        self.author = autor
        self.title = titulo
        self.magazine = revista
        self.edition = edicao
        self.publication = publicacao
    def make_bio(self, separador):
        return self.author + '. ' + self.title + separador + self.magazine + separador + self.edition + ': ' + self.publication

article = Artigo('Feuerbach', 'Das Wesen des Christenthums', 'Sämmtliche Werke', '33', '1841')

print(article.make_bio(', '))
