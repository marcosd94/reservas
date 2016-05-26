from articulo import Articulo
class ControladorArticulo():
    """Clase Controlador de los Articulos"""
    def articulo_libre(self,articulo):
        if(articulo.reservado == False):
            return True
        else:
            return False
    def reservar_articulo(self,articulo,codigo):
        articulo.reservar_articulo(codigo)
    def articulo_reservado(self,articulo):
        if(articulo.reservado == True):
            return True
        else:
            return False
    def cancelar_reserva(self,articulo):
        articulo=articulo.cancelar_reserva(articulo)
        return articulo
