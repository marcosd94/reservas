from articulo import Articulo
from notebook import Notebook
from controlador_persistence import ControladorPersistence
class ControladorArticulo():
    """Clase Controlador de los Articulos"""
    def articulo_libre(self,articulo):
        if(articulo.reservado == False):
            return True
        else:
            return False

    def reservar_articulo(self,usuario,articulo):
        persistence = ControladorPersistence()
        articulo=persistence.leer(articulo)
        articulo.reservar_articulo(usuario)
        persistence.persistir(articulo,articulo.codigo)
    def articulo_reservado(self,articulo):
        if(articulo.reservado == True):
            return True
        else:
            return False
    def cancelar_reserva(self,articulo):
        persistence = ControladorPersistence()
        articulo=persistence.leer(articulo)
        articulo.cancelar_reserva()
        persistence.persistir(articulo,articulo.codigo)
    def listar_articulos_reservados(self):
        a=Notebook(None,None,None, None, None,None)
        return a.listar_articulos_reservados()
    def listar_articulos_libres(self):
        a=Notebook(None,None,None, None, None,None)
        return a.listar_articulos_libres()
    def listar_articulos(self):
        a=Notebook(None,None,None, None, None,None)
        return a.listar_articulos()
