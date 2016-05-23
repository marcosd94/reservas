from persistence import MiZODB,transaction
from notebook import Notebook
from roles import Administrador
from roles import Gestor
from usuario import Usuario
def verificar(usu):
    try:
        dbroot[usu]
        db.close()
    except:
        print ('Usuario ingresado válido')
        return False
    else:
        print('El usuario ya existe, vuelva a ingresar usuario')
        return True
def cargar_funcionario():
    db=MiZODB()
    dbroot=db.raiz
    rol= input('Ingrese Rol del Funcionario: ')
    nombre= input('Nombres: ')
    apellido= input('Apellidos: ')
    documento_identidad= input('Documento de identidad: ')
    fecha_nacimiento = input('Fecha de Nacimiento: ')
    sexo= input('Sexo: ')
    cargo= input('Cargo : ')
    fecha_ingreso= input('Fecha de ingreso : ')
    codigo= input('Codigo : ')
    free=True
    while (free):
        usuario= input('Usuario : ')
        free=verificar(usuario)
    contrasenha= input('Contraseña : ')
    if( rol == 'Gestor'):
        f1= Gestor(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha)
        dbroot[f1.usuario]= f1
    else:
        print('No existe el Rol indicado')
    transaction.commit()
    print('Funcionario cargado con exito')
    db.close()
print('******** BIENVENIDOS AL SISTEMA DE RESERVAS ********')
print('INICIAR SESION')
print('FAVOR INGRESE: ')
login= True
usuario= input('Usuario: ')
contrasenha=input('Contraseña: ')
db=MiZODB()
dbroot=db.raiz
codigo = dbroot[usuario]
while(login):
    if(contrasenha == codigo.password):
        print('ACCESO CORRECTO')
        login= False
    else:
        print('Lo sentimos, la contraseña ingresada es incorrecta.')
        contrasenha=input('Vuelva a ingresar la contraseña: ')
db.close()
if isinstance(codigo, Administrador):
    print('\n     BIENVENIDO AL SISTEMA')
    print ('ELIJA LA TAREA A EJECUTAR')
    print( '1- Cargar Funcionario')
    tarea = input('Ingrese número de tarea: ')
    if(tarea=='1'):
        cargar_funcionario()
    print ('        RESERVAR EQUIPOS')
    print ("\n---------------------------------")
    print ('        LISTA DE EQUIPOS')
    print ("\n---------------------------------")
    note = Notebook('16/05/2016',None,'Notebook DELL', '113', '12/04/2016', False)
    note.listar_articulos()
    equipo= input( 'Ingresar codigo de Equipo a Reservar: ')
    print ("\n---------------------------------")
    db=MiZODB()
    dbroot=db.raiz
    articulo= dbroot[equipo]
    if (articulo.reservado == False):
        articulo.funcionario= codigo
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
elif isinstance(codigo, Gestor):
    print('esta actividad es solo para gestores')
    #reservar()
