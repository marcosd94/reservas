import tkinter
from persistence import MiZODB,transaction
from funcionario import Funcionario
import bienvenidos
def salir():
    exit()
def  listar_funcionarios(usu):
    funcionarios=tkinter.Tk()
    funcionarios.title("LISTADO DE FUNCIONARIOS")
    funcionarios.geometry("1000x500")
    def cerrar():
        funcionarios.destroy()
        import login
    def inicio():
        funcionarios.destroy()
        bienvenidos.ventana(usu)
    #window.wm_iconbitmap('favicon.ico')
    #L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
    #L1.place(bordermode='outside', height=50,x=100, y=10)

    mylistbox=tkinter.Listbox(funcionarios,height=12,width=100,font=('times',13))
    mylistbox.place(x=32,y=110)
    db = MiZODB()
    dbroot = db.raiz
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Funcionario):
            f="Usuario: "+ key+", Funcionario: "+ obj.nombres+" "+obj.apellidos+ ", Cargo: "+ obj.cargo+ ", Rol: "+obj.rol
            #, Codigo: "+ obj.codigo)
            #print ("CI: ", obj.documento_identidad)
            #print ("Dependencia: ", obj.dependencia.nombre_dependencia)
            #print ("Cargo: ", obj.cargo, " Rol: ",obj.rol)
            #print ("\n---------------------------------")
            mylistbox.insert('end',f)
    db.close()

    inicio = tkinter.Button(funcionarios,text="Inicio", command=inicio)
    inicio.place(bordermode='outside', height=40, width=100, x=40,y=400)
    button1 = tkinter.Button(funcionarios,text="Cerrar Sesión", command=cerrar)
    button1.place(bordermode='outside', height=40, width=100, x=140,y=400)
    button0 = tkinter.Button(funcionarios,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=240,y=400)
    funcionarios.mainloop()
