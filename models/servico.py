class servico:
    def __init__(self, nome, duracao):
        self.nome_do_corte = nome
        self.duracao = duracao
        
    def __str__ (self):
        return f'{self.nome_do_corte} ({self.duracao} min)'
        