from articulo import Articulo
from reservable import Reservable
class Notebook(Articulo,Reservable):
    """Clase Notebook, que desciende de la clase Articulo"""
    def __init__(self, fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado):
        Articulo.__init__(self, fecha_reserva,Funcionario,reservado)
        self.descripcion= descripcion
        self.codigo= codigo
        self.fecha_ingreso= fecha_ingreso
    def eliminar_articulo(self,clave):
        super(Notebook, self).eliminar_articulo(clave)
    def reservar(self,):
        pass
    def aceptar_reserva(self):
        pass
    def rechazar_reserva(self):
        pass
