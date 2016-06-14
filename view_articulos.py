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
        cerrar = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        cerrar.pack(side="bottom")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    titulo = tkinter.Label(articulos, font='Arial', text="Seleccionar el código del articulo a reservar")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    subtitulo1 = tkinter.Label(articulos, font='Arial', text="Código")
    subtitulo1.place(bordermode='outside', height=20, width=150, y=80, x=5)
    subtitulo2 = tkinter.Label(articulos, font='Arial', text="Descripción del articulo")
    subtitulo2.place(bordermode='outside', height=20, width=200, y=80, x=130)
    mylistbox=tkinter.Listbox(articulos,height=12,width=50,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=22,y=110)
    mylistbox2=tkinter.Listbox(articulos,height=12,width=70,font=('times',13))
    mylistbox2.place(x=122,y=110)
    ctrl_art=ControladorArticulo()
    ctrl_art=ctrl_art.listar_articulos_libres()
    for key in ctrl_art[0] :
        mylistbox.insert('end',key)
    for values in ctrl_art[1]:
        mylistbox2.insert('end',values)
    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    cerrar = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(articulos,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
def cargar_articulos(usu):
    articulos=tkinter.Tk()
    articulos.title("CARGAR ARTICULO")
    articulos.geometry("800x500")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    def cargar():
        def cerrar_exp():
            articulos.destroy()
            cargar_articulos(usu)
        try:
            ctrl_art=ControladorArticulo()
            ctrl_art.cargar_articulos(None, None, str(descripcion.get()), str(codigo.get()), str(fecha_alta.get()) ,False, str(tipo_articulo.get()))
        except Exception as e:
            alerta = tkinter.Message(articulos, relief='raised', text='NO SE PUDO CARGAR EL ARTICULO\nError: '+str(e), width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")
        else:
            alerta = tkinter.Message(articulos, relief='raised', text='ARTICULO CARGADO CON EXITO', width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30,x=150)
            ok = tkinter.Button(alerta,text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

    titulo = tkinter.Label(articulos, font='Arial', text="CARGAR ARTICULOS")
    titulo.place(bordermode='outside', height=20, width=300, x=100)
    lbl_descripcion= tkinter.Label(articulos, font='Arial', text="Descripcion")
    lbl_descripcion.place(bordermode='outside', height=20, width=200, x=50, y=30)
    lbl_codigo = tkinter.Label(articulos, font='Arial', text="Código articulo")
    lbl_codigo.place(bordermode='outside', height=20, width=200, x=50, y=55)
    lbl_fecha_alta = tkinter.Label(articulos, font='Arial',text="Fecha alta")
    lbl_fecha_alta.place(bordermode='outside', height=20, width=200, x=50, y=80)
    lbl_tipo_articulo = tkinter.Label(articulos, font='Arial',text="Tipo de articulo")
    lbl_tipo_articulo.place(bordermode='outside', height=20, width=200, x=50, y=105)

    descripcion=tkinter.Entry(articulos, font='times')
    descripcion.place(bordermode='outside', height=20, width=200, x=250, y=30)
    codigo=tkinter.Entry(articulos, font='times')
    codigo.place(bordermode='outside', height=20, width=200, x=250, y=55)
    fecha_alta=tkinter.Entry(articulos, font='times')
    fecha_alta.place(bordermode='outside', height=20, width=200, x=250, y=80)
    tipo= ['Notebook','Proyector','Multiple Electrico']
    tipo_articulo=ttk.Combobox(articulos,value=tipo,state= 'readonly')
    tipo_articulo.place(bordermode='outside', height=20, width=200, x=250, y=105)

    cargar = tkinter.Button(articulos,text="Cargar", command=cargar)
    cargar.place(bordermode='outside', height=40, width=100, x=50,y=130)
    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=150,y=130)
    cerrar = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=250,y=130)
    salir = tkinter.Button(articulos,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=350,y=130)
    articulos.mainloop()
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
        cerrar = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        cerrar.pack(side="bottom")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    titulo = tkinter.Label(articulos, font='Arial', text="Seleccionar el código del articulo a liberar")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    subtitulo1 = tkinter.Label(articulos, font='Arial', text="Código")
    subtitulo1.place(bordermode='outside', height=20, width=150, y=80, x=5)
    subtitulo2 = tkinter.Label(articulos, font='Arial', text="Descripción del articulo")
    subtitulo2.place(bordermode='outside', height=20, width=200, y=80, x=135)
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
    cerrar = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(articulos,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
def listar_articulos(usu):
    articulos=tkinter.Tk()
    articulos.title("LISTADO DE ARTICULOS")
    articulos.geometry("1050x500")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    mylistbox=tkinter.Listbox(articulos,height=12,width=110,font=('times',13))
    mylistbox.place(x=32,y=110)
    ctrl_art=ControladorArticulo()
    ctrl_art=ctrl_art.listar_articulos()
    for values in ctrl_art:
        mylistbox.insert('end',values)

    titulo = tkinter.Label(articulos, font='Arial', text="LISTADO GENERAL DE ARTICULOS")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    cerrar = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=140,y=400)
    salir = tkinter.Button(articulos,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
def eliminar_articulo(usu):
    articulos=tkinter.Tk()
    articulos.title("ELIMINAR ARTICULOS")
    articulos.geometry("800x500")
    def cerrar():
        articulos.destroy()
        login.inicio()
    def salir():
        articulos.destroy()
    def inicio():
        articulos.destroy()
        bienvenidos.ventana(usu)
    def CurSelet(evt):
        def cerrar_exp():
            articulos.destroy()
            eliminar_articulo(usu)
        ctrl_art=ControladorArticulo()
        ctrl_art.eliminar_articulo(usu, str(mylistbox.get(mylistbox.curselection())))
        frame2 = tkinter.Message(articulos, relief='raised', text='ARTICULO ELIMINADO CON EXITO', width=200)
        frame2.place(bordermode='outside', height=150, width=200, y=30,x=150)
        cerrar = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
        cerrar.pack(side="bottom")
    titulo = tkinter.Label(articulos, font='Arial', text="Seleccionar el código del articulo a eliminar")
    titulo.place(bordermode='outside', height=20, width=600, y=30, x=100)
    subtitulo1 = tkinter.Label(articulos, font='Arial', text="Código")
    subtitulo1.place(bordermode='outside', height=20, width=150, y=80, x=5)
    subtitulo2 = tkinter.Label(articulos, font='Arial', text="Descripción del articulo")
    subtitulo2.place(bordermode='outside', height=20, width=200, y=80, x=135)
    mylistbox=tkinter.Listbox(articulos,height=12,width=50,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)
    mylistbox2=tkinter.Listbox(articulos,height=12,width=70,font=('times',13))
    mylistbox2.place(x=132,y=110)
    ctrl_art=ControladorArticulo()
    art=ctrl_art.listar_articulos_libres()
    for key in art[0] :
        mylistbox.insert('end',key)
    for values in art[1]:
        mylistbox2.insert('end',values)
    inicio = tkinter.Button(articulos,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    button1 = tkinter.Button(articulos,text="Cerrar Sesión", command=cerrar)
    button1.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(articulos,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    articulos.mainloop()
