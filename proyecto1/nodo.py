class Nodo:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitando = False
        self.nivel = -1
        self.vecinos = []
    #Se crea la funcion de agregar vecinos a los nodos
    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
