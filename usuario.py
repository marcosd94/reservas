from funcionario import Funcionario
class Usuario(Funcionario):
    """Clase Usuario, la cual desciende de la clase Funcionario y guarda los datos basicos de un usuario"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Funcionario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,Dependencia)
        self.usuario= usuario
        self.password= password
