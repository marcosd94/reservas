from persistence import MiZODB,transaction
from funcionario import Funcionario
nombre = None
clave = None
f1 = Funcionario(nombre, 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016',clave)
f1.buscar_funcionario()
#nombre= input ('nombre: ')
clave = input ( 'Clave: ')
f1 = Funcionario(nombre, 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016',clave)
#f1.cargar_funcionario(f1)
#f1.buscar_funcionario(clave)
#f1.buscar_funcionario()
f1.eliminar_funcionario(clave)
