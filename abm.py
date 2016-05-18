from persistence import MiZODB,transaction
from funcionario import Funcionario
from notebook import Notebook
from persona import Persona
from proyector import Proyector
nombre = None
clave = None
#clave= input ('Ingrese la clave del usuario: ')
#f1 = Funcionario(nombre, 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016',clave)
#f1.buscar_funcionario()
#nombre= input ('nombre: ')
#clave = input ('Clave: ')
#f1 = Funcionario(nombre, 'Gimenez', 4785758, '17/07/2000', 'F' , 'CONTADOR','17/05/2016','252')
#f1.cargar_funcionario(f1)
#f1.buscar_funcionario(clave)
#f1.buscar_funcionario()
#f1.eliminar_funcionario(clave)

#note = Notebook('si','16/05/2016','Marcos Peralta','Notebook HP', '252', '12/04/2016')
db=MiZODB()
dbroot=db.raiz
#usuario= dbroot['252']
#note = Notebook('si','16/05/2016',usuario,'Notebook HP', '100', '12/04/2016')
#dbroot[note.codigo]= note
#del dbroot['001']
#del dbroot['002']
#del dbroot['003']
#del dbroot[None]
#del dbroot['001']
transaction.commit()

for key in dbroot.keys():
    obj = dbroot[key]
    if isinstance(obj, Notebook):
        print ( "Clave Articulo: ", key)
        print ("Funcionario: ", obj.funcionario.nombres, obj.funcionario.apellidos, " CI: ", obj.funcionario.documento_identidad)
        print ("Descripcion:  ", obj.descripcion)
        print ("Fecha de Ingreso: ", obj.fecha_ingreso)
        print ("\n---------------------------------")
    elif isinstance(obj, Funcionario):
        print ( "Clave Funcionario: ", key)
        print ("Funcionario: ", obj.nombres,obj.apellidos)
        print ("CI: ", obj.documento_identidad)
        print ("Cargo: ", obj.cargo)
        print ("\n---------------------------------")
        db.close()
#print (note.codigo)
#dbroot[note.codigo]= note
transaction.commit()
db.close()
