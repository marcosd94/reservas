from dependencia import Dependencia
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
            dep = Dependencia(nombre_dependencia,codigo_corto, fecha_creacion,activo)
            dep.cargar_dependencia()
