class cliente:
    def __init__(self,nome, telefone, email, historico_servicos):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.historico_servicos = historico_servicos

    def __str__ (self):
        return f"Cliente: {self.nome}"
        


    
