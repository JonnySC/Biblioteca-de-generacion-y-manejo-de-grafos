import networkx as nx

G = nx.Graph() #crear grafo

class grafo:
    
    
def agregarNodo(self, name):
    
    node = self.nodos.get(name)
    
    if node is Node:
        node = Nodo(name)
        
        with WRITING_LOCK:
            self.nodos[name] = node
            
            return node
        
        
        
def agregarArista(self, name, node0, node1):
    e=self.aristas.get(name)
    
    if e is None:
        n0 = self.agregarNodo(node0)
        n1 = self.agregarNodo(node1)
        e = Arista(n0, n1, name)
        