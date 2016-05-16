from abc import ABCMeta, abstractmethod
class Reservable(metaclass=ABCMeta):
    """docstring for """
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
