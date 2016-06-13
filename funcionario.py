from abc import ABCMeta, abstractmethod
from persona import Persona
from persistence import MiZODB,transaction
from controlador_persistence  import ControladorPersistence
class Funcionario(Persona,metaclass=ABCMeta):
    """Clase Funcionario, la misma desciende de la clase Persona y guarda los datos especificos que debe tener un funcionario"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo,cargo,fecha_ingreso,codigo,Dependencia):
        Persona.__init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo)
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.codigo=codigo
        self.dependencia=Dependencia
    def cargar_funcionario(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.usuario)
    def eliminar_funcionario(self,clave):
        persistence= ControladorPersistence()
        persistence.eliminar(clave)
    def listar_funcionarios(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Funcionario):
                lista[0].append(key)
                lista[1].append("Funcionario: "+ obj.nombres+" "+obj.apellidos+ ", Cargo: "+ obj.cargo+ ", Rol: "+obj.rol )
        db.close()
        return lista
