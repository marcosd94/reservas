#simple.py
from persistence import MiZODB,transaction

db=MiZODB()
dbroot=db.raiz
dbroot['numero']=3
dbroot['string']= 'lalala'
dbroot['lista'] = [1,2,3,5,7,12]
dbroot['diccionario']= {1918,'Red Sox',1919, 'Reds'}
dbroot['anidado']={
1918:[('Red Sox',4),('Cubs',2)],
1919:[('Reds',5),('White Sox',3)]
}
transaction.commit()
db.close()
