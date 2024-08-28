from random import choice

class Perinola:
    def __init__(self):
        self.cara_visible= 1
    def __repr__(self):
        return f" salio : {self.cara_visible}"
    def tirar(self):
        self.cara_visible = choice (1, self.caras)
        return self.cara_visible    