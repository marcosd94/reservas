from usuario import Usuario
from persistence import MiZODB,transaction
class Administrador(Usuario):
    """docstring for """
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password)

    def cargar_funcionario(self,f1):
        db=MiZODB()
        dbroot=db.raiz
        #rol= input('Ingrese Rol del Funcionario: ')
        #if( rol == 'Gestor'):
        #    f1= Gestor('Maria', 'Gonzalez', 4776313, '17/07/2000', 'M' , 'PRUEBA','17/05/2016','004', 'mgonzalez', 'contrasenha')
        dbroot[f1.usuario]= f1
        transaction.commit()
        db.close()
class Gestor(Usuario):
    """docstring for """
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password)

class Reservas(Usuario):
    """docstring for """
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password):
        Usuario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password)
