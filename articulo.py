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
        print ('        LISTA DE EQUIPOS')
        print ("\n---------------------------------")
        db = MiZODB()
        dbroot = db.raiz
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                print ("Clave del Articulo: ", key)
                print ("Descripcion: ", obj.descripcion)
                if(obj.reservado==True):
                    print ("Reservado: SI")
                else:
                    print ("Reservado: NO")
                print ("\n---------------------------------")
        transaction.commit()
        db.close()
    def articulos_reservados(self):
        db = MiZODB()
        dbroot = db.raiz
        count=0
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                if(obj.reservado==True):
                    count+=1
                    print ("Clave del Articulo: ", key)
                    print ("Descripcion: ", obj.descripcion)
                    print ("Reservado: SI, en fecha: ", obj.fecha_reserva)
                    print ("\n---------------------------------")
        transaction.commit()
        db.close()
        return count
    def articulos_libres(self):
        db = MiZODB()
        dbroot = db.raiz
        count=0
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, Articulo):
                if(obj.reservado==False):
                    count+=1
                    print ("Clave del Articulo: ", key)
                    print ("Descripcion: ", obj.descripcion)
                    print ("Reservado: NO")
                    print ("\n---------------------------------")
        transaction.commit()
        db.close()
        return count
    def reservar_articulo(self,codigo):
        self.funcionario= codigo
        self.reservado=True
        self.fecha_reserva= datetime.datetime.now()
    def cancelar_reserva(self,articulo):
        articulo.reservado=False
        articulo.fecha_reserva= None
        articulo.funcionario=None
        return articulo
