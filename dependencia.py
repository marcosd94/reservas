from persistence import MiZODB,transaction
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
        lista=[]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Dependencia):
                if(obj.activo):
                    lista.append(key)
        db.close()
        return lista
