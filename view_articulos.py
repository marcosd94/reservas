import tkinter
from persistence import MiZODB,transaction
from funcionario import Funcionario
import login
import bienvenidos
import tkinter.ttk as ttk
from controlador_articulo import ControladorArticulo
from articulo import Articulo
def cargar_reserva(usu):
    articulos=tkinter.Tk()
    articulos.title("LISTADO DE ARTICULOS LIBRES")
    articulos.geometry("800x500")
    def CurSelet(evt):
        def cerrar_exp():
            articulos.destroy()
            cargar_reserva(usu)
        ctrl_art=ControladorArticulo()
        ctrl_art.reservar_articulo(usu,str(mylistbox.get(mylistbox.curselection())))
        frame2 = tkinter.Message(articulos, relief='raised', text="ARTICULO RESERVADO CON EXITO", width=200)
        frame2.place(bordermode='outside', height=150, width=200, y=30,x=150)
        button3 = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        button3.pack(side="bottom")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    #window.wm_iconbitmap('favicon.ico')
    #L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    #L1.place(bordermode='outside', height=50,x=100, y=10)

    mylistbox=tkinter.Listbox(articulos,height=12,width=50,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)
    mylistbox2=tkinter.Listbox(articulos,height=12,width=70,font=('times',13))
    mylistbox2.place(x=132,y=110)
    ctrl_art=ControladorArticulo()
    ctrl_art=ctrl_art.listar_articulos_libres()
    for key in ctrl_art[0] :
        mylistbox.insert('end',key)
    for values in ctrl_art[1]:
        mylistbox2.insert('end',values)
    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    button1 = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    button1.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(articulos,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
def cargar_funcionario(usu):
    funcionarios=tkinter.Tk()
    funcionarios.title("CARGAR FUNCIONARIOS")
    funcionarios.geometry("1000x500")
    def cerrar():
        funcionarios.destroy()
        login.inicio()
    def salir():
        funcionarios.destroy()
    def inicio():
        #value=str(cbx.get())
        #print (value)
        funcionarios.destroy()
        bienvenidos.ventana(usu)
    def cargar():
        #value=str(cbx.get())

        def cerrar_exp():
            funcionarios.destroy()
            cargar_funcionario(usu)
        try:
            fun=ControladorFuncionario()
            fun.cargar_funcionario(str(nombre.get()), str(apellido.get()), str(documento_identidad.get()), str(fecha_nacimiento.get()), str(sexo.get()) , str(cargo.get()),
            str(fecha_ingreso.get()), str(codigo.get()), str(usuario.get()), str(contrasenha.get()), str(dep.get()), str(rol.get()))
        except:
            alerta = tkinter.Message(funcionarios, relief='raised', text='NO SE PUDO CARGAR AL FUNCIONARIO', width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")
        else:
            alerta = tkinter.Message(funcionarios, relief='raised', text='FUNCIONARIO CARGADO CON EXITO', width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")
    titulo = tkinter.Label(funcionarios, font='Arial', text="CARGAR FUNCIONARIOS")
    titulo.place(bordermode='outside', height=20, width=300, x=100)
    lbl_rol = tkinter.Label(funcionarios, font='Arial', text="Ingrese Rol del Funcionario")
    lbl_rol.place(bordermode='outside', height=20, width=200, x=50, y=30)
    lbl_nombre = tkinter.Label(funcionarios, font='Arial',text="Nombres",justify='left')
    lbl_nombre.place(bordermode='outside', height=20, width=200, x=50, y=55)
    lbl_apellido = tkinter.Label(funcionarios, font='Arial', text="Apellidos")
    lbl_apellido.place(bordermode='outside', height=20, width=200, x=50, y=80)
    lbl_documento_identidad = tkinter.Label(funcionarios, font='Arial',text="Documento de identidad")
    lbl_documento_identidad.place(bordermode='outside', height=20, width=200, x=50, y=105)
    lbl_fecha_nacimiento = tkinter.Label(funcionarios, font='Arial', text="Fecha de Nacimiento")
    lbl_fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=50, y=130)
    lbl_sexo = tkinter.Label(funcionarios, font='Arial',text="Sexo")
    lbl_sexo.place(bordermode='outside', height=20, width=200, x=50, y=155)
    lbl_cargo = tkinter.Label(funcionarios, font='Arial', text="Cargo")
    lbl_cargo.place(bordermode='outside', height=20, width=200, x=50, y=180)
    lbl_dep = tkinter.Label(funcionarios, font='Arial',text="Dependencia")
    lbl_dep.place(bordermode='outside', height=20, width=200, x=50, y=205)
    lbl_fecha_ingreso = tkinter.Label(funcionarios, font='Arial', text="Fecha de ingreso")
    lbl_fecha_ingreso.place(bordermode='outside', height=20, width=200, x=50, y=230)
    lbl_codigo = tkinter.Label(funcionarios, font='Arial',text="Codigo")
    lbl_codigo.place(bordermode='outside', height=20, width=200, x=50, y=255)
    lbl_usuario = tkinter.Label(funcionarios, font='Arial',text="Usuario")
    lbl_usuario.place(bordermode='outside', height=20, width=200, x=50, y=280)
    lbl_contrasenha = tkinter.Label(funcionarios, font='Arial',text="Contraseña")
    lbl_contrasenha.place(bordermode='outside', height=20, width=200, x=50, y=305)

    rol= ['Administrador','Gestor','Reservas']
    rol = ttk.Combobox(funcionarios,value=rol)
    rol.place(bordermode='outside', height=20, width=200, x=250, y=30)
    #rol=tkinter.Entry(funcionarios, font='times')
    #rol.place(bordermode='outside', height=20, width=200, x=250, y=30)
    nombre=tkinter.Entry(funcionarios, font='times')
    nombre.place(bordermode='outside', height=20, width=200, x=250, y=55)
    apellido=tkinter.Entry(funcionarios, font='times')
    apellido.place(bordermode='outside', height=20, width=200, x=250, y=80)
    documento_identidad=tkinter.Entry(funcionarios, font='times')
    documento_identidad.place(bordermode='outside', height=20, width=200, x=250, y=105)
    fecha_nacimiento=tkinter.Entry(funcionarios, font='times')
    fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=250, y=130)

    sexo=['MASCULINO','FEMENINO']
    sexo=ttk.Combobox(funcionarios,value=sexo)
    sexo.place(bordermode='outside', height=20, width=200, x=250, y=155)
    cargo=tkinter.Entry(funcionarios, font='times')
    cargo.place(bordermode='outside', height=20, width=200, x=250, y=180)
    ctrl_dep = ControladorDependencia()
    dep=ctrl_dep.listar_dependencia()
    dep=ttk.Combobox(funcionarios,value=dep)
    dep.place(bordermode='outside', height=20, width=200, x=250, y=205)
    fecha_ingreso=tkinter.Entry(funcionarios, font='times')
    fecha_ingreso.place(bordermode='outside', height=20, width=200, x=250, y=230)
    codigo=tkinter.Entry(funcionarios, font='times')
    codigo.place(bordermode='outside', height=20, width=200, x=250, y=255)
    usuario=tkinter.Entry(funcionarios, font='times')
    usuario.place(bordermode='outside', height=20, width=200, x=250, y=280)
    contrasenha=tkinter.Entry(funcionarios, font='times')
    contrasenha.place(bordermode='outside', height=20, width=200, x=250, y=305)
    cargar = tkinter.Button(articulos,text="Cargar", command=cargar)
    cargar.place(bordermode='outside', height=40, width=100, x=40,y=400)
    inicio = tkinter.Button(funcionarios,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=140,y=400)
    cerrar = tkinter.Button(funcionarios,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=240,y=400)
    salir = tkinter.Button(funcionarios,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=340,y=400)
    funcionarios.mainloop()
def cancelar_reserva(usu):
    articulos=tkinter.Tk()
    articulos.title("LISTADO DE ARTICULOS RESERVADOS")
    articulos.geometry("800x500")
    def CurSelet(evt):
        def cerrar_exp():
            articulos.destroy()
            cancelar_reserva(usu)
        ctrl_art=ControladorArticulo()
        ctrl_art.cancelar_reserva(str(mylistbox.get(mylistbox.curselection())))
        frame2 = tkinter.Message(articulos, relief='raised', text="ARTICULO LIBERADO CON EXITO", width=200)
        frame2.place(bordermode='outside', height=150, width=200, y=30,x=150)
        button3 = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        button3.pack(side="bottom")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    #window.wm_iconbitmap('favicon.ico')
    #L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    #L1.place(bordermode='outside', height=50,x=100, y=10)

    mylistbox=tkinter.Listbox(articulos,height=12,width=50,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)
    mylistbox2=tkinter.Listbox(articulos,height=12,width=70,font=('times',13))
    mylistbox2.place(x=132,y=110)
    ctrl_art=ControladorArticulo()
    ctrl_art=ctrl_art.listar_articulos_reservados()
    for key in ctrl_art[0] :
        mylistbox.insert('end',key)
    for values in ctrl_art[1]:
        mylistbox2.insert('end',values)

    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    button1 = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    button1.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(articulos,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
def listar_articulos(usu):
    articulos=tkinter.Tk()
    articulos.title("LISTADO DE ARTICULOS")
    articulos.geometry("800x500")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    #window.wm_iconbitmap('favicon.ico')
    #L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    #L1.place(bordermode='outside', height=50,x=100, y=10)

    mylistbox=tkinter.Listbox(articulos,height=12,width=100,font=('times',13))
    mylistbox.place(x=32,y=110)
    ctrl_art=ControladorArticulo()
    ctrl_art=ctrl_art.listar_articulos()
    for values in ctrl_art:
        mylistbox.insert('end',values)

    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    cerrar = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    salir = tkinter.Button(articulos,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
