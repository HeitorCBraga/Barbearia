class unidade:
    def __init__(self, nome_da_unidade, endereco):
        self.nome = nome_da_unidade
        self.endereco = endereco
    
    def __str__ (self,):
       return f'{self.nome} - {self.endereco}' 