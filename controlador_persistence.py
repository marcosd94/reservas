from persistence import MiZODB,transaction
class ControladorPersistence():
    """docstring for """
    def persistir(self,obj,clave):
        db=MiZODB()
        dbroot=db.raiz
        dbroot[clave]= obj
        transaction.commit()
        db.close()
    def leer(self,clave):
        db=MiZODB()
        dbroot=db.raiz
        obj=dbroot[clave]
        db.close()
        return obj
