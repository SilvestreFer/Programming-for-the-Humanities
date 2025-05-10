#Classe - corresponde a uma abstração de uma entidade (o que podemos fazer sobre um mundo)
#Conjuto de caracteristicas que são interessantes para o que queremos fazer
#Objetos pertencem a uma classe
#Ex.: classe: livro - O que tem nela: autor, título, conjunto ordenado de páginas

#Objetos - concretização das características de ima determinada classe.
#Ex: autor -> Kant, título  -> Kritik, Páginas -> 53

class Book:
    def __init__(self, auth, titl):
        self.author = auth
        self.title = titl
        self.pages = []

#criamos a classe com os atributos que queremos que tenha

kpv = Book ('Immanuel Kant', 'Kritik der praktischen Vernunft')
#atribuimos um objeto para as características dessa classe
#para asceder a um dos atributos colocamos o nome do objeto seguido de ponto e a características/atributo
print(kpv.author)
print(kpv.title)

#Podemos definir um método para, por exemplo, gerar uma referência bibliografica do livro

class Book:
    def __init__(self, auth, titl):
        self.author = auth
        self.title = titl
        self.pages = []
    def make_bioblio(self,separador):
        return self.author + separador + self.title
#biblio = kpv(',')