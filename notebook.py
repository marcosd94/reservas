from articulo import Articulo
class Notebook(Articulo,Reservable):
    """docstring for """
    def __init__(self, Usuario):
        self.usuario = Usuario
