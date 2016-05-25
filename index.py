from persistence import MiZODB,transaction
from notebook import Notebook
from roles import Administrador
from roles import Gestor
from roles import Reservas
from usuario import Usuario
from funcionario import Funcionario
from dependencia import Dependencia
import os
import subprocess
import sys

def limpiar():
   subprocess.call("clear")


def inicio(codigo):
    if isinstance(codigo, Administrador):
        print('\n*******BIENVENIDO AL SISTEMA*******')
        print ('    ELIJA LA TAREA A EJECUTAR')
        print( '1- Cargar Funcionario')
        print( '2- Cargar Articulo')
        print( '3- Reservar Articulo')
        print( '4- Listar Funcionarios')
        print( '5- Cancelar Reserva')
        print( '6- Eliminar Funcionario')
        print( '7- Crear Dependencia')
        print( '8- Listar Dependencias')
        print( '9- Cerrar Sesión')
        print( '10- Salir')
        tarea = input('Ingrese número de tarea: ')
        if(tarea=='1'):
            limpiar()
            cargar_funcionario(codigo)
        elif(tarea=='2'):
            limpiar()
            cargar_articulo(codigo)
        elif(tarea=='3'):
            limpiar()
            cargar_reserva(codigo)
        elif(tarea=='4'):
            limpiar()
            buscar_funcionario(codigo)
        elif(tarea=='5'):
            limpiar()
            cancelar_reserva(codigo)
        elif(tarea=='6'):
            limpiar()
            eliminar_funcionario(codigo)
        elif(tarea=='7'):
            limpiar()
            crear_dependencia(codigo)
        elif(tarea=='8'):
            limpiar()
            listar_dependencia(codigo)
        elif(tarea=='9'):
            limpiar()
            login()
        elif(tarea=='10'):
            sys.exit()
        else:
            print('Tarea no valida')
    elif isinstance(codigo, Gestor):
        print('\n*******BIENVENIDO AL SISTEMA*******')
        print ('    ELIJA LA TAREA A EJECUTAR')
        print( '1- Cargar Articulo')
        print( '2- Reservar Articulo')
        print( '3- Listar Funcionarios')
        print( '4- Cancelar Reserva')
        print( '5- Cerrar Sesión')
        print( '6- Salir')
        tarea = input('Ingrese número de tarea: ')
        if(tarea=='1'):
            limpiar()
            cargar_articulo(codigo)
        elif(tarea=='2'):
            limpiar()
            cargar_reserva(codigo)
        elif(tarea=='3'):
            limpiar()
            buscar_funcionario(codigo)
        elif(tarea=='4'):
            limpiar()
            cancelar_reserva(codigo)
        elif(tarea=='5'):
            limpiar()
            login()
        elif(tarea=='6'):
            sys.exit()
        else:
            print('Tarea no valida')
    elif isinstance(codigo, Reservas):
        print('\n*******BIENVENIDO AL SISTEMA*******')
        print ('    ELIJA LA TAREA A EJECUTAR')
        print( '1- Reservar Articulo')
        print( '2- Cerrar Sesión')
        print( '3- Salir')
        tarea = input('Ingrese número de tarea: ')
        if(tarea=='1'):
            limpiar()
            cargar_reserva(codigo)
        elif(tarea=='2'):
            limpiar()
            login()
        elif(tarea=='3'):
            sys.exit()
        else:
            print('Tarea no valida')
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
def existe_usu(usu):
    try:
        db=MiZODB()
        dbroot=db.raiz
        dbroot[usu]
        db.close()
    except:
        print ('El usuario no existe. Favor verificar')
        return True
        db.close()
    else:
        return False

def cargar_funcionario(usu):
    db=MiZODB()
    dbroot=db.raiz
    rol= input('Ingrese Rol del Funcionario: ')
    nombre= input('Nombres: ')
    apellido= input('Apellidos: ')
    documento_identidad= input('Documento de identidad: ')
    fecha_nacimiento = input('Fecha de Nacimiento: ')
    sexo= input('Sexo: ')
    cargo= input('Cargo : ')
    dep=dbroot[input('Dependencia : ')]

    fecha_ingreso= input('Fecha de ingreso : ')
    codigo= input('Codigo : ')
    free=True
    while (free):
        usuario= input('Usuario : ')
        free=verificar(usuario)
    contrasenha= input('Contraseña : ')
    if( rol == 'Gestor'):
        f1= Gestor(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
        dbroot[f1.usuario]= f1
    elif(rol=='Administrador'):
        f1= Administrador(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
        dbroot[f1.usuario]= f1
    elif(rol=='Reservas'):
        f1= Reservas(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
        dbroot[f1.usuario]= f1
    else:
        print('No existe el Rol indicado')
    transaction.commit()
    print('Funcionario cargado con exito')
    db.close()
    inicio(usu)

def cargar_articulo(codigo):
    db=MiZODB()
    dbroot=db.raiz
    fecha_reserva=input('Ingrese fecha de reserva: ')
    Funcionario=None
    descripcion=input('Ingrese descripcion del articulo: ')
    codigo=input('Ingrese codigo unico del articulo: ')
    fecha_ingreso=input('Ingrese fecha de alta del articulo: ')
    reservado= False
    tipo=input('Tipo de Equipo: ')
    if( tipo == 'Notebook'):
        art= Notebook(fecha_reserva, Funcionario, descripcion, codigo, fecha_ingreso , reservado)
        dbroot[art.codigo]= art
    else:
        print('No existe el Tipo de articulo indicado')
    transaction.commit()
    print('Articulo cargado con exito')
    db.close()
    inicio(codigo)

def cargar_reserva(codigo):
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
        transaction.commit()
        print ('Articulo reservado con exito por: ', articulo.funcionario.nombres, articulo.funcionario.apellidos, " CI: ", articulo.funcionario.documento_identidad)
        db.close()
        inicio(codigo)
    else:
        print ('El articulo esta reservado por:')
        print ( "Clave Articulo: ", equipo)
        print( "Clave Funcionario: ", articulo.funcionario.codigo)
        print ("Funcionario: ", articulo.funcionario.nombres, articulo.funcionario.apellidos, " CI: ", articulo.funcionario.documento_identidad)
        print ("Descripcion:  ", articulo.descripcion)
        print ("Fecha de Ingreso: ", articulo.fecha_ingreso)
        print ("\n---------------------------------")
        db.close()
        inicio(codigo)

def buscar_funcionario(codigo):
    db = MiZODB()
    dbroot = db.raiz
    os.system('clear')
    print('\n     LISTADO DE FUNCIONARIOS')
    print ("---------------------------------")
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Funcionario):
            print ( "Usuario: ", key)
            print("Codigo: ", obj.codigo)
            print ("Funcionario: ", obj.nombres,obj.apellidos)
            print ("CI: ", obj.documento_identidad)
            print ("Dependencia: ", obj.dependencia.nombre_dependencia)
            print ("Cargo: ", obj.cargo)
            print ("\n---------------------------------")
            db.close()
    inicio(codigo)
def cancelar_reserva(codigo):
    note = Notebook('16/05/2016',None,'Notebook DELL', '113', '12/04/2016', False)
    print('ARTICULOS RESERVADOS: ')
    print ("\n---------------------------------")
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
    #print('\n')
    #print('Los siguientes articulos se encuentran reservados')
    #note.articulos_reservados()
    inicio(codigo)

def eliminar_funcionario(codigo):
    print('     ELIMINAR FUNCIONARIOS')
    existe= True
    while(existe):
        clave= input('Ingrese codigo del funcionario a Eliminar: ')
        existe=existe_usu(clave)
    db = MiZODB()
    dbroot = db.raiz
    del dbroot[clave]
    transaction.commit()
    db.close()
    print('Funcionario eliminado con existo')
    inicio(codigo)
def crear_dependencia(codigo):
        db=MiZODB()
        dbroot=db.raiz
        nombre_dependencia=input('Ingrese nombre de la dependencia: ')
        codigo_corto=input('Ingrese codigo corto de la dependencia: ')
        fecha_creacion=input('Ingrese fecha de creación: ')
        activo=True
        dep= Dependencia(nombre_dependencia,codigo_corto, fecha_creacion,activo)
        dbroot[dep.codigo_corto]= dep
        transaction.commit()
        print('Dependencia creada con exito')
        db.close()
        inicio(codigo)
def listar_dependencia(codigo):
    db = MiZODB()
    dbroot = db.raiz
    print('\n     LISTADO DE DEPENDENCIAS')
    print ("---------------------------------")
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Dependencia):
            print ( "Codigo corto de la dependencia: ", key)
            print ("Nombre de la Dependencia: ", obj.nombre_dependencia)
            print ("Fecha de creacion: ", obj.fecha_creacion)
            if(obj.activo):
                print ("Activo: SI")
            else:
                print ("Activo: NO")
            print ("\n---------------------------------")
    db.close()
    inicio(codigo)
def login():
    print('******** BIENVENIDOS AL SISTEMA DE RESERVAS ********')
    print('INICIAR SESION')
    print('FAVOR INGRESE: ')
    login= True
    existe= True
    while(existe):
        usuario= input('Usuario: ')
        existe=existe_usu(usuario)
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
    inicio(codigo)
login()
