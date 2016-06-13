from articulo import Articulo
from notebook import Notebook
from multiple import MultipleElectrico
from proyector import Proyector
from controlador_persistence import ControladorPersistence
class ControladorArticulo():
    """Clase Controlador de los Articulos"""
    def reservar_articulo(self,usuario,articulo):
        persistence = ControladorPersistence()
        articulo=persistence.leer(articulo)
        articulo.reservar_articulo(usuario)
        persistence.persistir(articulo,articulo.codigo)
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
    def cargar_articulos(self,fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado,tipo):
        if( tipo == 'Notebook'):
            a= Notebook(fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado)
        elif(tipo=='Proyector'):
            a= Proyector(fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado)
        elif(tipo=='Multiple Electrico'):
            a= MultipleElectrico(fecha_reserva,Funcionario,descripcion, codigo, fecha_ingreso,reservado)
        a.cargar_articulos()
