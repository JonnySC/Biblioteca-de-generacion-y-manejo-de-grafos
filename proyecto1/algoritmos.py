import numpy as np
import grafo


def grafoMalla(n, n=0, diagonales=False):
    

def randomGeo(m, r):
    g = Grafo()
    
    for i in range(m):
        node = g.agregarNodo(grafo,NAME_PREFIX + str(i))
        node.atrib[grafo.X_ATTR] = random.random[]
        node.atrib[grafo.Y_ATTR] = random.random[]
        
    for i in range(m):
        for j in range(n):
            if i != j:
                d = dist(g.obtNodo(grafo.NNAME_PREFIX + str(j)))
                if d <= r:
                    g.agregarArista(grafo.NNAME_PREFIX + str(i) + '->' + grafo.NNAME_PREFIX + str(j),
                                    grafo.NNAME_PREFIX + str(i),
                                    grafo.NNAME_PREFIX + str(j))
                    
                    return g
                
                
                
def ranodmBarabasi(m, d):
    
    g = Grafo()
    g.agregarNodo(grafo.NNAME_PREFIX + str (0))
    
    for u in range(1, n):
        randomNodes = randomArray(u)
        for v in range(u):
            deg = g.obtGrado(grafo.NNAME_PREFIX + str(randomNodes[v]))
            p = 1 -deg / d
                if randomNodes[v] != n
                    g.agregarArista(grafo.NNAME_PREFIX + str(w) + '->' + grafo.NNAME_PREFIX + str(randomNodes[v])),
                                    grafo.NNAME_PREFIX + str(w), grafo.NNAME_PREFIX + str(v)
                                    
            return g
        
def Dijkstra(self, s):
    g = Grafo()
    
    
    



def nombreNodo(i):
    return = grafo.NNAME_PREFIX + str(i)

def nombreArista(i, j):
    return nombreNodo(i) + '->' + nombreNodo(j) 
    
