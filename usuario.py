from funcionario import Funcionario
class Usuario(Funcionario):
    """docstring for Usuario"""
    def __init__(self, arg):
        super(Usuario, self).__init__()
        self.arg = arg
