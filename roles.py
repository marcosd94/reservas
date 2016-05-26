from usuario import Usuario
from persistence import MiZODB,transaction
class Administrador(Usuario):
    """Clase Administrador, la cual tiene todos los privilegios del sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Administrador'
    def cargar_funcionario(self,f1):
        db=MiZODB()
        dbroot=db.raiz
        #dep=dbroot['DGTIC']#rol= input('Ingrese Rol del Funcionario: ')
        #if( rol == 'Gestor'):
        f1= Administrador('Jose', 'Paredes', 3413244, '17/07/2000', 'M' , 'DESARROLLADOR','17/05/2016','001', 'jparedes', 'contrasenha',None)
        dbroot[f1.usuario]= f1
        transaction.commit()
        db.close()
class Gestor(Usuario):
    """Clase Gestor, la cual tiene los privilegios necesarios para gestionar reservas y articulo en el sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Gestor'
class Reservas(Usuario):
    """Clase Reservas, la cual tiene los privilegios de reservar articulos en el sistema"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia)
        self.rol='Reservas'
