from persistence import MiZODB,transaction
from funcionario import Funcionario

#db=MiZODB()
#dbroot=db.raiz
f1 = Funcionario('Jose', 'Gonzalez', 5644600, '17/05/2016', 'M' , 'CUIDADOR','17/05/2016')
#dbroot['f4']= f1
#dbroot.keys()
#transaction.commit()
#db.close()
f1.buscar_funcionario()
#f1.eliminar_funcionario()
