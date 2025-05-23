class Barbeiro:
    def __init__(self, nome, especialidades=None):
        self.nome = nome
        self.especialidades = especialidades if especialidades is not None else []
        self.agenda = []

    def __str__(self):
        if self.especialidades:
            habilidades = ', '.join(self.especialidades)
        else:
            habilidades = 'nenhuma habilidade cadastrada'
        return f'O barbeiro {self.nome} tem habilidades em: {habilidades}'

    
