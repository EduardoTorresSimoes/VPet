
class VPET:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.xcoord = x
        self.ycoord = y
        
        self.energia = 50
        self.felicidade = 50

    def posicao(self,x,y):
        self.xcoord = x
        self.ycoord = y
    