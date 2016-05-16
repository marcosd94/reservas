#Leer_simple.py
from persistence import MiZODB
db = MiZODB()
dbroot = db.raiz
for key in dbroot.keys():
    print (key + ':', dbroot[key])
print ('asi se accede a una posicion' + dbroot['string'])
db.close
