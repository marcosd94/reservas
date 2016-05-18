from articulo import Articulo
from reservable import Reservable
class Notebook(Articulo,Reservable):
    """docstring for """
    def __init__(self, reservas,fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso):
        Articulo.__init__(self, reservas,fecha_reserva,Funcionario)
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
#note = Notebook('si','16/05/2016','Marcos Peralta','Notebook HP', '001', '12/04/2016')
#print ( note.descripcion,note.funcionario)
