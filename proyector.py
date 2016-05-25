from articulo import Articulo
from reservable import Reservable
class Proyector(Articulo,Reservable):
    """docstring for """
    def __init__(self, fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado):
        Articulo.__init__(self, fecha_reserva,Funcionario,reservado)
        self.descripcion= descripcion
        self.codigo= codigo
        self.fecha_ingreso= fecha_ingreso
    def cargar_articulo(self):
        pass
    def eliminar_articulo(self):
        pass
    def reservar(self,):
        pass
    def cancelar_reserva(self):
        pass
    def aceptar_reserva(self):
        pass
    def rechazar_reserva(self):
        pass
