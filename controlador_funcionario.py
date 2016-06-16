from roles import Administrador
from roles import Gestor
from roles import Reservas
from controlador_persistence import ControladorPersistence
from time import strptime
class ControladorFuncionario():
    """Clase Controlador de los Funcionarios"""
    def cargar_funcionario(self,nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep,rol):
        if ( usuario=='' or usuario == None):
            raise Exception('Usuario vacio')
        else:
            persistence = ControladorPersistence()
            try:
                strptime(fecha_nacimiento, '%d/%m/%Y')
                strptime(fecha_ingreso, '%d/%m/%Y')
                persistence.leer(usuario)
            except ValueError:
                raise Exception('El formato no corresponde\nfavor ingresar de la siguiente manera dd/mm/yyyy')
            except:
                dep=persistence.leer(dep)
                if( rol == 'Gestor'):
                    f1= Gestor(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
                elif(rol=='Administrador'):
                    f1= Administrador(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
                elif(rol=='Reservas'):
                    f1= Reservas(nombre, apellido, documento_identidad, fecha_nacimiento, sexo , cargo,fecha_ingreso,codigo, usuario, contrasenha,dep)
                f1.cargar_funcionario()
            else:
                raise Exception('El usuario ya existe')
    def eliminar_funcionario(self,usuario, codigo_usuario):
        usuario.eliminar_funcionario(codigo_usuario)
    def listar_funcionarios(self,usuario):
        return usuario.listar_funcionarios()
