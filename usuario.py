from funcionario import Funcionario
class Usuario(Funcionario):
    """docstring for Usuario"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,usuario,password,Dependencia):
        Funcionario.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,Dependencia)
        self.usuario= usuario
        self.password= password
