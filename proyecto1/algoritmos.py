import numpy as np
import grafo

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
    g.agregarNodo(grafo.NNAME_PREFIX + str [0])
    
    for 
    