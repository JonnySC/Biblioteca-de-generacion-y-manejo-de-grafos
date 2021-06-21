class Arista:
    #constructor
    def __init__(self):
        self.id = 0
    #Funcion para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)
