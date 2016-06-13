import tkinter
from roles import Administrador
from roles import Gestor
import login
import view_funcionarios
import view_articulos
import view_dependencias
def salir():
    ventana.destroy()
def  ventana(usu):
    ventana=tkinter.Tk()
    ventana.title("BIENVENIDO AL SISTEMA")
    ventana.geometry("500x500")
    #window.wm_iconbitmap('favicon.ico')
    L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    L1.place(bordermode='outside', height=50,x=100, y=10)
    if isinstance(usu, Administrador):
        itemsforlistbox=['Cargar Funcionario',
        'Listar Funcionarios',
        'Eliminar Funcionario',
        'Cargar Articulo',
        'Listar Articulos',
        'Reservar Articulo',
        'Cancelar Reserva',
        'Crear Dependencia',
        'Listar Dependencias',
        'Cerrar Sesión',
        'Salir']
    elif isinstance(usu, Gestor):
        itemsforlistbox=[
        'Cargar Articulo',
        'Reservar Articulo',
        'Cancelar Reserva',
        'Listar Articulos',
        'Listar Funcionarios',
        'Cerrar Sesión',
        'Salir']
    else:
        itemsforlistbox=[
        'Reservar Articulo',
        'Cerrar Sesión',
        'Salir']

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
        elif(value=='Cerrar Sesión'):
            ventana.destroy()
            login.inicio()
        elif (value=='Salir'):
            ventana.destroy()

    mylistbox=tkinter.Listbox(ventana,height=12,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)

    for items in itemsforlistbox:
        mylistbox.insert('end',items)

    ventana.mainloop()
