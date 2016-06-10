from persistence import MiZODB,transaction
from abc import ABCMeta, abstractmethod
import datetime
class Articulo(metaclass=ABCMeta):
    """Clase Articulo, la cual se encarga de guardar los datos basico de los articulos que se tienen en la Institucion"""
    def __init__(self,fecha_reserva,Funcionario,reservado):
        self.fecha_reserva=fecha_reserva
        self.funcionario = Funcionario
        self.reservado= reservado
    @abstractmethod
    def cargar_articulo(self):
        pass
    @abstractmethod
    def eliminar_articulo(self):
        pass
    def listar_articulos(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                if(obj.reservado==True):
                    lista.append("Codigo articulo: "+ key+", descripcion: "+ obj.descripcion+ " Reservado: SI, en fecha: "+ str(obj.fecha_reserva))
                else:
                    lista.append("Codigo articulo: "+ key+", descripcion: "+ obj.descripcion+" Reservado: NO")
        db.close()
        return lista
    def listar_articulos_reservados(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                if(obj.reservado==True):
                    lista[0].append(key)
                    lista[1].append("Codigo articulo: "+ key+", descripcion: "+ obj.descripcion)
        db.close()
        return lista
    def listar_articulos_libres(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                if(obj.reservado==False):
                    lista[0].append(key)
                    lista[1].append("Codigo articulo: "+ key+", descripcion: "+ obj.descripcion)
        db.close()
        return lista
    def reservar_articulo(self,codigo):
        self.funcionario= codigo
        self.reservado=True
        self.fecha_reserva= datetime.datetime.now()
    def cancelar_reserva(self):
        self.reservado=False
        self.fecha_reserva= None
        self.funcionario=None
