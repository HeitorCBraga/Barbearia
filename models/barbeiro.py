class barbeiro:
    def __init__ (self, nome, especialidades=None):
        self.nome = nome 
        self.epecialidades = especialidades if especialidades is not None else []
        self.agenda = []

    def __str__(self,):
        return f'O barbeiro {self.nome} tem habilidades em: {", ".join(self.especialidades)}'
