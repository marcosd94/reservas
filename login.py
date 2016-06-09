import tkinter
from persistence import MiZODB,transaction
import bienvenidos
def inicio():
    def salir():
        window.destroy()
    def verificar():
        try:
            db=MiZODB()
            dbroot=db.raiz
            usu=dbroot[usuario.get()]
            db.close()
        except:

            def cerrar_exp():
                frame2.destroy()
            db.close()
            frame2 = tkinter.Message(window, relief='raised', text='EL USUARIO '+usuario.get()+' NO EXISTE', width=200)
            frame2.place(bordermode='outside', height=150, width=200, y=30,x=150)
            button3 = tkinter.Button(frame2,text="Ok", command=cerrar_exp)
            button3.pack(side="bottom")
        else:
            if(usu.password == contraseña.get()):
                window.destroy()
                bienvenidos.ventana(usu)
                #frame3 = tkinter.Message(window, relief='raised', text='BIENVENIDO', width=50)
                #frame3.pack()
            else:
                def cerrar_inv():
                    frame4.destroy()
                frame4 = tkinter.Message(window, relief='raised', text='Contraseña invalida', width=200)
                frame4.place(bordermode='outside', height=150, width=200, y=30,x=150)
                invalid = tkinter.Button(frame4,text="Ok", command=cerrar_inv)
                invalid.pack(side="bottom")
    window=tkinter.Tk()
    window.title("VENTANA DE PRUEBA")
    window.geometry("500x300")
    #window.wm_iconbitmap('favicon.ico')
    titulo = tkinter.Label(window, font='Arial', text="SISTEMA DE RESERVAS")
    titulo.place(bordermode='outside', height=20, width=300, x=100)
    L1 = tkinter.Label(window, font='Arial', text="Usuario")
    L1.place(bordermode='outside', height=20, width=100, x=50, y=30)
    L2 = tkinter.Label(window, font='Arial',text="Contraseña")
    L2.place(bordermode='outside', height=20, width=100, x=50, y=60)
    usuario=tkinter.Entry(window, font='times')
    usuario.place(bordermode='outside', height=20, width=200, x=150, y=30)
    contraseña=tkinter.Entry(window, font='times',show='*') #se escoge encriptar con * la contraseña
    contraseña.place(bordermode='outside', height=20, width=200, x=150, y=60)
    button0 = tkinter.Button(window,text="Acceder", command=verificar)
    button0.place(bordermode='outside', height=40, width=100, x=50,y=90)
    button0 = tkinter.Button(window,text="Salir", command=salir)
    button0.place(bordermode='outside', height=40, width=100, x=160,y=90)
    window.mainloop()

#listbox = tkinter.Listbox(window)
#listbox.pack()

#listbox.insert(0, "a list entry")
#x=1
#for item in ["one", "two", "three", "four"]:
#    listbox.insert(x, item)
#    x=x+1
