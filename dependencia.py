class Dependencia(object):
    """Clase Dependencia, la cual guarda los datos de todos los departamentos creados dentro de la Institucion """
    def __init__(self, nombre_dependencia,codigo_corto, fecha_creacion,activo):
        self.nombre_dependencia = nombre_dependencia
        self. fecha_creacion=  fecha_creacion
        self.activo=activo
        self.codigo_corto=codigo_corto
