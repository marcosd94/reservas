#persistence.py
from ZODB import FileStorage, DB
import transaction

class MiZODB():
    """Clase MiZODB para la persistencia de los objetos"""
    def __init__(self):
        self.storage = FileStorage.FileStorage('Data.fs')
        self.db = DB(self.storage)
        self.conexion = self.db.open()
        self.raiz=self.conexion.root()
    def close(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()
