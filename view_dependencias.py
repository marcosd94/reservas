import tkinter
from persistence import MiZODB,transaction
import login
import bienvenidos
import tkinter.ttk as ttk
from controlador_dependencia import ControladorDependencia
def cargar_dependencia(usu):
    dependencia=tkinter.Tk()
    dependencia.title("CARGAR DEPENDENCIA")
    dependencia.geometry("800x500")
    def cerrar():
        dependencia.destroy()
        login.inicio()
    def salir():
        dependencia.destroy()
    def inicio():
        dependencia.destroy()
        bienvenidos.ventana(usu)
    def cargar():
        def cerrar_exp():
            dependencia.destroy()
            cargar_dependencia(usu)
        try:
            ctrl_dep=ControladorDependencia()
            ctrl_dep.cargar_dependencia(str(nombre_dependencia.get()), str(codigo_corto.get()), str(fecha_creacion.get()) ,True)
        except Exception as e:
            alerta = tkinter.Message(dependencia, relief='raised', text='NO SE PUDO CARGAR LA DEPENDENCIA\nError: '+str(e), width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")
        else:
            alerta = tkinter.Message(dependencia, relief='raised', text='DEPENDENCIA CARGADA CON EXITO', width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

    titulo = tkinter.Label(dependencia, font='Arial', text="CARGAR DEPENDENCIAS")
    titulo.place(bordermode='outside', height=20, width=300, x=100)

    lbl_nombre_dependencia= tkinter.Label(dependencia, font='Arial', text="Dependencia")
    lbl_nombre_dependencia.place(bordermode='outside', height=20, width=200, x=50, y=30)
    lbl_codigo_corto = tkinter.Label(dependencia, font='Arial', text="Código corto")
    lbl_codigo_corto.place(bordermode='outside', height=20, width=200, x=50, y=55)
    lbl_fecha_creacion = tkinter.Label(dependencia, font='Arial',text="Fecha creación")
    lbl_fecha_creacion.place(bordermode='outside', height=20, width=200, x=50, y=80)

    nombre_dependencia=tkinter.Entry(dependencia, font='times')
    nombre_dependencia.place(bordermode='outside', height=20, width=200, x=250, y=30)
    codigo_corto=tkinter.Entry(dependencia, font='times')
    codigo_corto.place(bordermode='outside', height=20, width=200, x=250, y=55)
    fecha_creacion=tkinter.Entry(dependencia, font='times')
    fecha_creacion.place(bordermode='outside', height=20, width=200, x=250, y=80)

    cargar = tkinter.Button(dependencia,text="Cargar", command=cargar)
    cargar.place(bordermode='outside', height=40, width=100, x=50,y=110)
    inicio = tkinter.Button(dependencia,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=150,y=110)
    cerrar = tkinter.Button(dependencia,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=250,y=110)
    salir = tkinter.Button(dependencia,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=350,y=110)
    dependencia.mainloop()
def listar_dependencia(usu):
    dependencia=tkinter.Tk()
    dependencia.title("LISTADO DE DEPENDENCIAS")
    dependencia.geometry("950x500")
    def cerrar():
        dependencia.destroy()
        login.inicio()
    def salir():
        dependencia.destroy()
    def inicio():
        dependencia.destroy()
        bienvenidos.ventana(usu)

    mylistbox=tkinter.Listbox(dependencia,height=12,width=100,font=('times',13))
    mylistbox.place(x=32,y=110)
    ctrl_dep = ControladorDependencia()
    ctrl_dep=ctrl_dep.listar_dependencia()
    for values in ctrl_dep[1]:
        mylistbox.insert('end',values)

    titulo = tkinter.Label(dependencia, font='Arial', text="LISTADO DE DEPENDENCIAS")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    inicio = tkinter.Button(dependencia,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    cerrar = tkinter.Button(dependencia,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    salir = tkinter.Button(dependencia,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=240,y=400)
    dependencia.mainloop()
def eliminar_dependencia(usu):
    dependencia=tkinter.Tk()
    dependencia.title("ELIMINAR DEPENDENCIA")
    dependencia.geometry("950x500")
    def cerrar():
        dependencia.destroy()
        login.inicio()
    def salir():
        dependencia.destroy()
    def inicio():
        dependencia.destroy()
        bienvenidos.ventana(usu)
    def CurSelet(evt):
        def cerrar_exp():
            dependencia.destroy()
            eliminar_dependencia(usu)
        ctrl_dep=ControladorDependencia()
        ctrl_dep.eliminar_dependencia(usu, str(mylistbox.get(mylistbox.curselection())))
        frame2 = tkinter.Message(dependencia, relief='raised', text='DEPENDENCIA ELIMINADA CON EXITO', width=200)
        frame2.place(bordermode='outside', height=150, width=200, y=30,x=150)
        cerrar = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        cerrar.pack(side="bottom")
    titulo = tkinter.Label(dependencia, font='Arial', text="Seleccionar el código corto de la dependencia a eliminar")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    subtitulo1 = tkinter.Label(dependencia, font='Arial', text="Código")
    subtitulo1.place(bordermode='outside', height=20, width=150, y=80, x=5)
    subtitulo2 = tkinter.Label(dependencia, font='Arial', text="Descripción de la dependencia")
    subtitulo2.place(bordermode='outside', height=20, width=300, y=80, x=135)
    mylistbox=tkinter.Listbox(dependencia,height=12,width=50,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)
    mylistbox2=tkinter.Listbox(dependencia,height=12,width=70,font=('times',13))
    mylistbox2.place(x=132,y=110)
    ctrl_dep=ControladorDependencia()
    dep=ctrl_dep.listar_dependencia()
    for key in dep[0] :
        mylistbox.insert('end',key)
    for values in dep[1]:
        mylistbox2.insert('end',values)
    inicio = tkinter.Button(dependencia,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    button1 = tkinter.Button(dependencia,text="Cerrar Sesión", command=cerrar)
    button1.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(dependencia,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    dependencia.mainloop()
