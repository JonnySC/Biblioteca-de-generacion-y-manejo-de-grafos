class Grafo:
    #constructor
    def __init__(self):
        self.vertices = {}
    #Funcion para la agregación de vertices al Grafo
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Nodo(v)
    #Función para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)
