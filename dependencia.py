from persistence import MiZODB,transaction
from controlador_persistence import ControladorPersistence
class Dependencia(object):
    """Clase Dependencia, la cual guarda los datos de todos los departamentos creados dentro de la Institucion """
    def __init__(self, nombre_dependencia,codigo_corto, fecha_creacion,activo):
        self.nombre_dependencia = nombre_dependencia
        self.fecha_creacion=  fecha_creacion
        self.activo=activo
        self.codigo_corto=codigo_corto
    def listar_dependencia(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Dependencia):
                if(obj.activo):
                    lista[0].append(key)
                    lista[1].append("Dependencia: "+ obj.nombre_dependencia+", Codigo corto: "+obj.codigo_corto+", Fecha de Creacion: "+ obj.fecha_creacion )
        db.close()
        return lista
    def cargar_dependencia(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.codigo_corto)
    def eliminar_dependencia(self,codigo_corto):
        persistence= ControladorPersistence()
        persistence.eliminar(codigo_corto)
