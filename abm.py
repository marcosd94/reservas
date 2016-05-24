from persistence import MiZODB,transaction
from funcionario import Funcionario
from notebook import Notebook
from persona import Persona
from proyector import Proyector
from articulo import Articulo
from roles import Administrador
import os
import subprocess
nombre = None
clave = None
#clave= input ('Ingrese la clave del usuario: ')
#f1 = Funcionario(nombre, 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016',clave)
#f1.buscar_funcionario()
#nombre= input ('nombre: ')
#clave = input ('Clave: ')
#f1 = Funcionario('lalalala', 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016','252')
#p= Persona('nombre','apellido','documento_identidad','fecha_nacimiento','sexo')
#art = Articulo('asdffd','fasdf','asdfasd')
#f1.cargar_funcionario(f1)
#f1.buscar_funcionario(clave)
#f1.buscar_funcionario()
#f1.eliminar_funcionario(clave)
#usu = Usuario('marcos', 'peralta', 2354345, '17/07/2000', 'M' , 'DESARROLLADOR','17/05/2016','002', 'mperalta', 'contrasenha')
#roles = Administrador('Jose', 'Paredes', 34563456, '17/07/2000', 'M' , 'CONTADOR','17/05/2016','003', 'jparedes', 'contrasenha')
#roles.cargar_funcionario(roles)
#roles.buscar_funcionario()
#note = Notebook('si','16/05/2016','Marcos Peralta','Notebook HP', '252', '12/04/2016')
db=MiZODB()
dbroot=db.raiz
#try:
#    dbroot['mperalta']
#    db.close()
#except:
#    print ('no existe usuario')
#else:
#    print('el usuario ya exite')
#note = Notebook('16/05/2016',None,'Notebook DELL', '101', '12/04/2016', False)
#dbroot[note.codigo]= note
#del dbroot['001']
#del dbroot['002']
#del dbroot['003']
#del dbroot[None]
#del dbroot['001']
transaction.commit()
db.close()
print ("prueba\n"*10)
subprocess.call("clear")
#dbroot[note.codigo]= note
