from persistence import MiZODB,transaction
from funcionario import Funcionario
from notebook import Notebook
from persona import Persona
from proyector import Proyector
from articulo import Articulo
from usuario import Usuario
def reservar():
    print ('        RESERVAR EQUIPOS')
    print ("\n---------------------------------")
    print ('        LISTA DE EQUIPOS')
    print ("\n---------------------------------")
    note = Notebook('si','16/05/2016',None,'Notebook DELL', '113', '12/04/2016', False)
    note.listar_articulos()
    equipo= input( 'Ingresar codigo de Equipo a Reservar: ')
    usu = input('Ingrese codigo de Funcionario: ')
    print ("\n---------------------------------")
    db=MiZODB()
    dbroot=db.raiz
    articulo= dbroot[equipo]
    fun = dbroot[usu]
    if (articulo.reservado == False):
        articulo.funcionario= fun
        articulo.reservado=True
        dbroot[equipo]=articulo
    #    dbroot._p_changed=True
        transaction.commit()
        print ('Articulo reservado con exito por: ', articulo.funcionario.nombres, articulo.funcionario.apellidos, " CI: ", articulo.funcionario.documento_identidad)
    else:
        print ('El articulo esta reservado por:')
        print ( "Clave Articulo: ", equipo)
        print( "Clave Funcionario: ", articulo.funcionario.codigo)
        print ("Funcionario: ", articulo.funcionario.nombres, articulo.funcionario.apellidos, " CI: ", articulo.funcionario.documento_identidad)
        print ("Descripcion:  ", articulo.descripcion)
        print ("Fecha de Ingreso: ", articulo.fecha_ingreso)
        print ("\n---------------------------------")
        db.close()
reservar()
def cancelar():
    note = Notebook('si','16/05/2016',None,'Notebook DELL', '113', '12/04/2016', False)
    note.articulos_reservados()
    equipo= input( 'Ingresar codigo de Equipo a Cancelar: ')
    db=MiZODB()
    dbroot=db.raiz
    articulo= dbroot[equipo]
    if (articulo.reservado == True):
        articulo.reservado=False
        dbroot[equipo]=articulo
        transaction.commit()
        print ('Articulo liberado con exito')
    else:
        print('El articulo se encuentra libre')

    db.close()
    print('\n')
    print('Los siguientes articulos se encuentran reservados')
    note.articulos_reservados()
#cancelar()
