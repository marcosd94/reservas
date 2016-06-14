import tkinter
from roles import Administrador
from roles import Gestor
import login
import view_funcionarios
import view_articulos
import view_dependencias
def  ventana(usu):
    def salir():
        ventana.destroy()
    def cerrar():
        ventana.destroy()
        login.inicio()
    ventana=tkinter.Tk()
    ventana.title("BIENVENIDO AL SISTEMA")
    ventana.geometry("500x500")
    L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    L1.place(bordermode='outside', height=50,x=100, y=10)
    if isinstance(usu, Administrador):
        itemsforlistbox=['Cargar Funcionario',
        'Listar Funcionarios',
        'Eliminar Funcionario',
        'Cargar Articulo',
        'Listar Articulos',
        'Eliminar Articulo',
        'Reservar Articulo',
        'Cancelar Reserva',
        'Crear Dependencia',
        'Listar Dependencias',
        'Eliminar Dependencia']
    elif isinstance(usu, Gestor):
        itemsforlistbox=[
        'Cargar Articulo',
        'Reservar Articulo',
        'Cancelar Reserva',
        'Listar Articulos',
        'Eliminar Articulo',
        'Listar Funcionarios',
        'Listar Dependencias']
    else:
        itemsforlistbox=[
        'Reservar Articulo']

    def CurSelet(evt):
        value=str(mylistbox.get(mylistbox.curselection()))
        if(value=='Cargar Funcionario'):
            ventana.destroy()
            view_funcionarios.cargar_funcionario(usu)
        elif (value=='Listar Funcionarios'):
            ventana.destroy()
            view_funcionarios.listar_funcionarios(usu)
        elif(value=='Eliminar Funcionario'):
            ventana.destroy()
            view_funcionarios.eliminar_funcionario(usu)
        elif(value=='Cargar Articulo'):
            ventana.destroy()
            view_articulos.cargar_articulos(usu)
        elif(value=='Listar Articulos'):
            ventana.destroy()
            view_articulos.listar_articulos(usu)
        elif(value=='Eliminar Articulo'):
            ventana.destroy()
            view_articulos.eliminar_articulo(usu)
        elif(value=='Reservar Articulo'):
            ventana.destroy()
            view_articulos.cargar_reserva(usu)
        elif(value=='Cancelar Reserva'):
            ventana.destroy()
            view_articulos.cancelar_reserva(usu)
        elif(value=='Crear Dependencia'):
            ventana.destroy()
            view_dependencias.cargar_dependencia(usu)
        elif(value=='Listar Dependencias'):
            ventana.destroy()
            view_dependencias.listar_dependencia(usu)
        elif(value=='Eliminar Dependencia'):
            ventana.destroy()
            view_dependencias.eliminar_dependencia(usu)

    mylistbox=tkinter.Listbox(ventana,height=12,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=45,y=110)

    for items in itemsforlistbox:
        mylistbox.insert('end',items)

    cerrar = tkinter.Button(ventana,text="Cerrar Sesión", command=cerrar)
    cerrar.place(bordermode='outside', height=40, width=100, x=40,y=400)
    salir = tkinter.Button(ventana,text="Salir", command=salir)
    salir.place(bordermode='outside', height=40, width=100, x=140,y=400)

    ventana.mainloop()
