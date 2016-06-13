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
        except:
            alerta = tkinter.Message(dependencia, relief='raised', text='NO SE PUDO CARGAR LA DEPENDENCIA', width=200)
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
    salir.place(bordermode='outside', height=40, width=100, x=350,y=130)
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

    inicio = tkinter.Button(dependencia,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    cerrar = tkinter.Button(dependencia,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    salir = tkinter.Button(dependencia,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=240,y=400)
    dependencia.mainloop()
