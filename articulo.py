from abc import ABCMeta, abstractmethod
class Articulo(metaclass=ABCMeta):
    """docstring for """
    def __init__(self, reservas,fecha_reserva,Usuario):
        self.reservas = reservas
        self.fecha_reserva=fecha_reserva
        self.usuario = Usuario
    @abstractmethod
    def cargar_articulo(self):
        pass
    @abstractmethod
    def eliminar_articulo(self):
        pass
