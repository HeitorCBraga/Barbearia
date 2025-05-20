class barbeiro:
    def __init__ (self, nome, especialidades=None):
        self.nome = nome 
        self.epecialidades = especialidades if especialidades is not None else []
        self.agenda = []

    