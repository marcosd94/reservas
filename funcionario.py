from abc import ABCMeta, abstractmethod
from persona import Persona
from persistence import MiZODB,transaction
class Funcionario(Persona,metaclass=ABCMeta):
    """docstring for Funcionario"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo):
        Persona.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo)
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.codigo=codigo
    def buscar_funcionario(self):
        db = MiZODB()
        dbroot = db.raiz
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Funcionario):
                print ( "Clave: ", key)
                print ("Funcionario: ", obj.nombres,obj.apellidos)
                print ("CI: ", obj.documento_identidad)
                print ("Cargo: ", obj.cargo)
                print ("\n---------------------------------")
                db.close()
    def eliminar_funcionario(self,clave):
        db = MiZODB()
        dbroot = db.raiz
        del dbroot[clave]
        transaction.commit()
        db.close()
