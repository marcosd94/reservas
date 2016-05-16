from articulo import Articulo
class Reservado(Articulo):
    """docstring for """
    def __init__(self, reservas):
        Articulo.__init__(self, reservas,'lalala','foo')
    def cargar_articulo(self, impr):
        self.lista = ['Proyector','Notebook','Pizarra']
        self.lista.append(impr)
        print(self.lista )

pr = Reservado('notebook')
pr.cargar_articulo('Mouse ')
