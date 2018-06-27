class Item(object):
    def __init__(self, id=0, nome='', valor=0):
        self.id    = id
        self.nome  = nome
        self.valor = valor
    
    def to_string(self):
        return("nome: %s, valor: R$%d" %(self.nome, self.valor))