from usuario import Usuario
from persistence import MiZODB,transaction
from controlador_persistence  import ControladorPersistence
class Administrador(Usuario):
    """Clase Administrador, la cual tiene todos los privilegios del sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Administrador'
    def cargar_funcionario(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.usuario)
        print(self.usuario)
class Gestor(Usuario):
    """Clase Gestor, la cual tiene los privilegios necesarios para gestionar reservas y articulo en el sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Gestor'
    def cargar_funcionario(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.usuario)
        print(self.usuario)
class Reservas(Usuario):
    """Clase Reservas, la cual tiene los privilegios de reservar articulos en el sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Reservas'
    def cargar_funcionario(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.usuario)
        print(self.usuario)
