from abc import ABCMeta, abstractmethod
class Persona(metaclass=ABCMeta):
    __metaclass__= ABCMeta
    """docstring for Persona"""
    def __init__(self, nombre,apellido,documento_identidad,fecha_nacimiento,sexo):
        self.nombres = nombre
        self.apellidos = apellido
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo= sexo
