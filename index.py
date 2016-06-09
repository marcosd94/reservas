from persistence import MiZODB,transaction
from notebook import Notebook
from multiple import MultipleElectrico
from proyector import Proyector
from roles import Administrador
from roles import Gestor
from roles import Reservas
from usuario import Usuario
from funcionario import Funcionario
from dependencia import Dependencia
from articulo import Articulo
from controlador_articulo import ControladorArticulo
import datetime
import subprocess
import sys
def limpiar():
   subprocess.call("clear")
def inicio(codigo):
    if isinstance(codigo, Administrador):
        print('\n*******BIENVENIDO AL SISTEMA*******')
        print ('    ELIJA LA TAREA A EJECUTAR')
        print( '1- Cargar Funcionario')
        print( '2- Listar Funcionarios')
        print( '3- Eliminar Funcionario')
        print( '4- Cargar Articulo')
        print( '5- Listar Articulos')
        print( '6- Reservar Articulo')
        print( '7- Cancelar Reserva')
        print( '8- Crear Dependencia')
        print( '9- Listar Dependencias')
        print( '10- Cerrar Sesión')
        print( '11- Salir')
        tarea = input('Ingrese número de tarea: ')
        if(tarea=='1'):
            limpiar()
            cargar_funcionario(codigo)
        elif(tarea=='2'):
            limpiar()
            listar_funcionarios(codigo)
        elif(tarea=='3'):
            limpiar()
            eliminar_funcionario(codigo)
        elif(tarea=='4'):
            limpiar()
            cargar_articulo(codigo)
        elif(tarea=='5'):
            limpiar()
            listar_articulos(codigo)
        elif(tarea=='6'):
            limpiar()
            cargar_reserva(codigo)
        elif(tarea=='7'):
            limpiar()
            cancelar_reserva(codigo)
        elif(tarea=='8'):
            limpiar()
            crear_dependencia(codigo)
        elif(tarea=='9'):
            limpiar()
            listar_dependencia(codigo)
        elif(tarea=='10'):
            limpiar()
            login()
        elif(tarea=='11'):
            sys.exit()
        else:
            limpiar()
            print('Tarea no valida!!')
            inicio(codigo)
    elif isinstance(codigo, Gestor):
        print('\n*******BIENVENIDO AL SISTEMA*******')
        print ('    ELIJA LA TAREA A EJECUTAR')
        print( '1- Cargar Articulo')
        print( '2- Reservar Articulo')
        print( '3- Cancelar Reserva')
        print( '4- Listar Articulos')
        print( '5- Listar Funcionarios')
        print( '6- Cerrar Sesión')
        print( '7- Salir')
        tarea = input('Ingrese número de tarea: ')
        if(tarea=='1'):
            limpiar()
            cargar_articulo(codigo)
        elif(tarea=='2'):
            limpiar()
            cargar_reserva(codigo)
        elif(tarea=='3'):
            limpiar()
            cancelar_reserva(codigo)
        elif(tarea=='4'):
            listar_articulos(codigo)
            limpiar()
        elif(tarea=='5'):
            limpiar()
            listar_funcionarios(codigo)
        elif(tarea=='6'):
            limpiar()
            login()
        elif(tarea=='7'):
            sys.exit()
        else:
            limpiar()
            print('Tarea no valida!!')
            inicio(codigo)
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
            limpiar()
            print('Tarea no valida!!')
            inicio(codigo)
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
        db.close()
        return True
    else:
        return False
def verificar_art(codigo):
        try:
            db=MiZODB()
            dbroot=db.raiz
            dbroot[codigo]
            db.close()
        except:
            print ('Codigo de articulo ingresado válido')
            db.close()
            return False
        else:
            print('El codigo de articulo ya existe, vuelva a ingresar usuario')
            return True
def existe_art(codigo):
        try:
            db=MiZODB()
            dbroot=db.raiz
            dbroot[codigo]
            db.close()
        except:
            print ('Articulo ingresado no existe. Favor verificar')
            db.close()
            return True
        else:
            return False
def verificar_dep(codigo):
        try:
            db=MiZODB()
            dbroot=db.raiz
            dbroot[codigo]
            db.close()
        except:
            print ('Codigo corto de dependencia ingresado válido')
            db.close()
            return False
        else:
            print('El Codigo corto de dependencia ya existe, vuelva a ingresar usuario')
            return True
def existe_dep(codigo):
        try:
            db=MiZODB()
            dbroot=db.raiz
            dbroot[codigo]
            db.close()
        except:
            print ('Dependencia ingresada no existe. Favor verificar')
            db.close()
            return True
        else:
            return False
def cargar_funcionario(usu):
    print('\n     CARGA DE FUNCIONARIOS')
    print ("---------------------------------")
    print('ROLES:\n-Administrador\n-Gestor\n-Reservas')
    rol= input('Ingrese Rol del Funcionario: ')
    nombre= input('Nombres: ')
    apellido= input('Apellidos: ')
    documento_identidad= input('Documento de identidad: ')
    fecha_nacimiento = input('Fecha de Nacimiento: ')
    sexo= input('Sexo: ')
    cargo= input('Cargo : ')
    dependencias_activas()
    dep_existe=True
    while(dep_existe):
        dep=input('Dependencia : ')
        dep_existe=existe_dep(dep)
    db=MiZODB()
    dbroot=db.raiz
    dep= dbroot[dep]
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
def cargar_articulo(usu):
    free=True
    Funcionario=None
    print('\n     CARGA DE ARTICULOS')
    print ("---------------------------------")
    descripcion=input('Ingrese descripcion del articulo: ')
    while(free):
        codigo=input('Ingrese codigo unico del articulo: ')
        free= verificar_art(codigo)
    fecha_ingreso=input('Ingrese fecha de alta del articulo: ')
    reservado= False
    print('Tipos:\n-Notebook\n-Proyector\n-Multiple')
    tipo=input('Tipo de Equipo: ')
    if( tipo == 'Notebook'):
        db=MiZODB()
        dbroot=db.raiz
        art= Notebook(None, Funcionario, descripcion, codigo, fecha_ingreso , reservado)
        dbroot[art.codigo]= art
        transaction.commit()
        print('Articulo: ', art.descripcion,' cargado con exito')
        db.close()
        inicio(usu)
    elif( tipo == 'Proyector'):
        db=MiZODB()
        dbroot=db.raiz
        art= Proyector(None, Funcionario, descripcion, codigo, fecha_ingreso , reservado)
        dbroot[art.codigo]= art
        transaction.commit()
        print('Articulo: ', art.descripcion,' cargado con exito')
        db.close()
        inicio(usu)
    elif( tipo == 'Multiple'):
        db=MiZODB()
        dbroot=db.raiz
        art= MultipleElectrico(None, Funcionario, descripcion, codigo, fecha_ingreso , reservado)
        dbroot[art.codigo]= art
        transaction.commit()
        print('Articulo: ', art.descripcion,' cargado con exito')
        db.close()
        inicio(usu)
    else:
        print('No existe el Tipo de articulo indicado')
        inicio(usu)
def cargar_reserva(codigo):
    print ('*******RESERVAR EQUIPOS*******')
    print ("\n---------------------------------")
    note = Notebook(None,None,None, None, None, None)
    print('*******ARTICULOS LIBRES******* ')
    art=note.articulos_libres()
    if(art>0):
        while(True):
            free=True
            while(free):
                equipo= input( 'Ingresar codigo de Equipo a Reservar: ')
                free= existe_art(equipo)
            print ("\n---------------------------------")
            db=MiZODB()
            dbroot=db.raiz
            articulo= dbroot[equipo]
            controller=ControladorArticulo()
            if (controller.articulo_libre(articulo)):
                controller.reservar_articulo(articulo,codigo)
                dbroot[equipo]=articulo
                transaction.commit()
                print ('Articulo: ',articulo.descripcion,' reservado con exito por: ', articulo.funcionario.nombres, articulo.funcionario.apellidos, " CI: ", articulo.funcionario.documento_identidad)
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
    else:
        print('Todos los articulos se encuentran reservados')
        inicio(codigo)
def listar_funcionarios(codigo):
    db = MiZODB()
    dbroot = db.raiz
    print('\n     LISTADO DE FUNCIONARIOS')
    print ("---------------------------------")
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Funcionario):
            print ("Usuario: ", key)
            print("Codigo: ", obj.codigo)
            print ("Funcionario: ", obj.nombres,obj.apellidos)
            print ("CI: ", obj.documento_identidad)
            print ("Dependencia: ", obj.dependencia.nombre_dependencia)
            print ("Cargo: ", obj.cargo, " Rol: ",obj.rol)
            print ("\n---------------------------------")
            db.close()
    inicio(codigo)
def funcionarios_activos():
    db = MiZODB()
    dbroot = db.raiz
    print('\n     FUNCIONARIOS ACTIVOS')
    print ("---------------------------------")
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Funcionario):
            print ("Usuario: ", key)
            print ("Funcionario: ", obj.nombres,obj.apellidos)
            print ("CI: ", obj.documento_identidad)
            print ("\n---------------------------------")
            db.close()
def cancelar_reserva(codigo):
    note = Notebook(None,None,None, None, None, None)
    print('ARTICULOS RESERVADOS: ')
    print ("\n---------------------------------")
    art=note.articulos_reservados()
    if(art>0):
        free=True
        while(free):
            equipo= input( 'Ingresar codigo de Equipo a Cancelar: ')
            free= existe_art(equipo)
        db=MiZODB()
        dbroot=db.raiz
        articulo= dbroot[equipo]
        controller=ControladorArticulo()
        if (controller.articulo_reservado(articulo)):
            articulo.cancelar_reserva(articulo)
            dbroot[equipo]=articulo
            transaction.commit()
            print ('Articulo: ',articulo.descripcion,' liberado con exito')
        else:
            print('El articulo: ',articulo.descripcion,' se encuentra libre')
        db.close()
    else:
        print('Ningun articulo se encuentra reservado')
    #print('\n')
    #print('Los siguientes articulos se encuentran reservados')
    #note.articulos_reservados()
    inicio(codigo)
def eliminar_funcionario(codigo):
    print('*******ELIMINAR FUNCIONARIOS********')
    funcionarios_activos()
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
    print(' *******CARGAR DEPENDENCIAS********')
    print ("---------------------------------")
    free=True
    nombre_dependencia=input('Ingrese nombre de la dependencia: ')
    while(free):
        codigo_corto=input('Ingrese codigo corto de la dependencia: ')
        free=verificar_dep(codigo_corto)
    fecha_creacion=input('Ingrese fecha de creación: ')
    activo=True
    dep= Dependencia(nombre_dependencia,codigo_corto, fecha_creacion,activo)
    db=MiZODB()
    dbroot=db.raiz
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
def dependencias_activas():
    db = MiZODB()
    dbroot = db.raiz
    print('\n     DEPENDENCIAS ACTIVAS')
    print ("---------------------------------")
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Dependencia):
            print ( "Codigo corto de la dependencia: ", key)
            print ("Nombre de la Dependencia: ", obj.nombre_dependencia)
            print ("\n---------------------------------")
    db.close()
def listar_articulos(codigo):
    print ('        LISTA DE EQUIPOS')
    print ("\n---------------------------------")
    db = MiZODB()
    dbroot = db.raiz
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Articulo):
            print ("Clave del Articulo: ", key)
            print ("Descripcion: ", obj.descripcion)
            if(obj.reservado==True):
                print ("Reservado: SI, en fecha: ", obj.fecha_reserva)
            else:
                print ("Reservado: NO")
            print ("\n---------------------------------")
    transaction.commit()
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
