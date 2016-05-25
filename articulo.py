from persistence import MiZODB,transaction
from abc import ABCMeta, abstractmethod
class Articulo(metaclass=ABCMeta):
    """docstring for """
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
                    print ("Reservado: SI")
                    print ("\n---------------------------------")
        transaction.commit()
        db.close()
        return count
    def cant_articulos():
            db = MiZODB()
            dbroot = db.raiz
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, Articulo):

                    if(obj.reservado==True):
                        print ("Clave del Articulo: ", key)
                        print ("Descripcion: ", obj.descripcion)
                        print ("Reservado: SI")
                    print ("\n---------------------------------")
            transaction.commit()
            db.close()
