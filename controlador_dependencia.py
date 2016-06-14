from dependencia import Dependencia
from controlador_persistence import ControladorPersistence
class ControladorDependencia():
    """docstring for """
    def listar_dependencia(self):
        dep = Dependencia(None,None, None,None)
        lista= dep.listar_dependencia();
        return lista
    def cargar_dependencia(self,nombre_dependencia,codigo_corto, fecha_creacion,activo):
        if ( codigo_corto=='' or codigo_corto == None):
            raise Exception('Codigo corto vacio')
        else:
            try:
                persistence = ControladorPersistence()
                persistence.leer(codigo_corto)
            except:
                dep = Dependencia(nombre_dependencia,codigo_corto, fecha_creacion,activo)
                dep.cargar_dependencia()
            else:
                raise Exception('El Codigo corto de la Dependencia ya existe')
    def eliminar_dependencia(self,usuario, codigo_corto):
        persistence = ControladorPersistence()
        dep = persistence.leer(codigo_corto)
        dep.eliminar_dependencia(codigo_corto)
