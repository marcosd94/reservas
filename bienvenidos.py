import tkinter
from roles import Administrador
from roles import Gestor
import view_listar_funcionarios
def salir():
    exit()
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
            pass
        elif (value=='Listar Funcionarios'):
            ventana.destroy()
            view_listar_funcionarios.listar_funcionarios(usu)
        elif(value=='Eliminar Funcionario'):
            pass
        elif(value=='Cargar Articulo'):
            pass
        elif(value=='Listar Articulos'):
            pass
        elif(value=='Reservar Articulo'):
            pass
        elif(value=='Cancelar Reserva'):
            pass
        elif(value=='Crear Dependencia'):
            pass
        elif(value=='Listar Dependencias'):
            pass
        elif(value=='Cerrar Sesión'):
            ventana.destroy()
            import login
        elif (value=='Salir'):
            exit()

    mylistbox=tkinter.Listbox(ventana,height=12,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=110)

    for items in itemsforlistbox:
        mylistbox.insert('end',items)

    ventana.mainloop()
