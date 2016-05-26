from abc import ABCMeta, abstractmethod
class Reservable(metaclass=ABCMeta):
    """Clase Abstracta Reservable, la cual contiene los metodos para que un Articulo pueda ser reservado"""
    @abstractmethod
    def reservar(self):
        pass
    @abstractmethod
    def cancelar_reserva(self):
        pass
    def aceptar_reserva(self):
        pass
    @abstractmethod
    def rechazar_reserva(self):
        pass
