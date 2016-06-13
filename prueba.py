from persistence import MiZODB,transaction
db=MiZODB()
dbroot=db.raiz
del dbroot['']
transaction.commit()
db.close()
