class Profesor:
	def __init__(self, nombre):
		self.nombre = nombre
	def obtener_enfoque(self):
		pass
class ProfesorInvestigador(Profesor):
	def __init__(self, nombre, publicaciones,areas_interes):
		Profesor.__init__(self, nombre)
		self.publicaciones=publicaciones
		self.areas_interes=areas_interes

	def obtener_enfoque (self):
		return 'enfoque cientifico'

class ProfesorTecnico(Profesor):
	def __init__ (self, nombre, especializaciones,experiencia_laboral):
		Profesor.__init__(self, nombre)
		self.especializaciones=especializaciones
		self.experiencia_laboral=experiencia_laboral

	def obtener_enfoque (self):
		return 'enfoque tecnico'

class ProfesorInvestigadorTecnico(ProfesorInvestigador, ProfesorTecnico):
	def __init__(self, nombre,publicaciones,areas_interes, especializaciones,experiencia_laboral):
		ProfesorInvestigador.__init__(self, nombre, publicaciones,areas_interes)
		ProfesorTecnico.__init__(self, nombre, especializaciones,experiencia_laboral)
	def obtener_enfoque (self):
		return ProfesorInvestigador.obtener_enfoque(self) + ' y ' + ProfesorTecnico.obtener_enfoque(self)

class ProfesorAficionado(Profesor):

	def obtener_enfoque (self):
		return 'enfoque indefinido'

#class Facultad:
#	def __init__

class Materia:
	def __init__ (self, nombre, Profesor):
		self.nombre=nombre
		self.profesor=Profesor
	def impartir_clase(self):
		print('Clase impartidad con ' + self.profesor.obtener_enfoque())





p1= ProfesorInvestigadorTecnico('Marcos','publicacion hecha', 'fisica','EDD','FP UNA 6 años')
p2=ProfesorTecnico('Eve','Base de datos', 'FP UNA 2 años')
m1 = Materia ('BD', p1)
m2= Materia ( 'algoritmica', p2)
m1.impartir_clase()
m2.impartir_clase()
