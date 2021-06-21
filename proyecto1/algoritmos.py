#Se inicializa clase que permite crear los archivos de visualizaciónote
#Se genera el grafo en formato GV y en formato PNG para su futuro analisis
class graphviz:
    dot = Digraph(comment='The Round Graph')
    #constructor
    def __init__(self):
        self.graphvis = {}
    #Función que agrega nodo para generar el archivo GV y PNG
    def agregaNodo(self,v):
        vs = str(v)
        self.dot.node(vs, vs)
    #Función que permite crear la lista en formato adecuado
    def listaedges(self,l2,a,b):
        c = str(a) + str(b)
        l2.append(c)
    #funcion que agrega arista por arista con una variable c con valor false o true
    def agregaedge(self, a, b):
        c = str(a)
        d = str(b)
        self.dot.edge(c , d, constraint='false')
    #Función que permite agregar la lista de conexiónes
    def agregaedges(self,l2):
        self.dot.edges(l2)
    #Función encargada de generar el archivo GV como el PNG
    def imprimegrafo(self, nom):
        print('-------Impresion y generacion GV de Grafo')
        #self.dot.format = 'png'
        a ='Graphviz-output/'
        b = a + str(nom)+ '.gv'
        self.dot.render(b, view = True)
        print(self.dot.source) #doctest: +NORMALIZE_WHITESPACE


#clase del modelo Malla
#Función con la que se integra el GRAFO de estudio
class Malla():
    def __init__(self):
        self.id={}

    def malla(self):
        #Llamado de las clases
        g = Grafo()
        h = graphviz()
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO MALLA------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v)
        #Lista de aristas del Grafo
        l2 = []
        l3 = []
        ve = [1,2]
        #Ciclo generador de aristas en pares
        for i in ve:
            random.shuffle(l)
            for i in range(0, len(l) , 2):
                a = l[i]
                b = l[i + 1]
                #agregan aristas al grafo
                g.agregarArista(a, b)
                #Se genera la lista para el archivo GV
                h.agregaedge(a, b)
                c=str(a)
                d=str(b)
                e='->'
                l2.insert(i, c+e+d)
                l3.insert(i, c)
                l3.insert(i+1, d)

        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        nodos = str(N)
        nom = "1_Malla"
        h.imprimegrafo(nom+'_'+nodos)
        return (l, l3)

#clase del modelo erdos and enry
class Erdosrenyi():
    #constructor
    def __init__(self):
        self.id={}

    def erdosrenyi(self):
        #Inicializa un grafo
        g = Grafo()
        h = graphviz()
        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO ERDOS ENRY------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v)

        #Pide el rango d eprobabilidad P
        #print("Ingresa el valor de probabilidad de cada nodo: ")
        #P = float(input())
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            for j in l:
                if i < j:
                    #tomando un numero random R
                    #R = random.random()
                    #Verificar si R < P
                    #if (R < P):
                        # Agrega las aristas para el grafo
                        g.agregarArista(i, j)
                        #Se genera la lista para el archivo GV
                        h.agregaedge(i, j)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        nodos = str(N)
        nom = "2_ErdosRenyi"
        h.imprimegrafo(nom+'_'+nodos)
        return(l, l3)

class Gilbert():
    #constructor
    def __init__(self):
        self.id={}

    def gilbert(self):
        #Inicializa un grafo
        g = Grafo()
        h = graphviz()
        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO GILBERT------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v)

        #Pide el rango d eprobabilidad P
        print("Ingresa el valor de probabilidad de cada nodo: ")
        P = float(input())
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            for j in l:
                if i < j:
                    #tomando un numero random R
                    R = random.random()
                    #Verificar si R < P
                    if (R < P):
                        # Agrega las aristas para el grafo
                        g.agregarArista(i, j)
                        #Se genera la lista para el archivo GV
                        h.agregaedge(i, j)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        nodos = str(N)
        nom = "3_Gilbert"
        h.imprimegrafo(nom+'_'+nodos)
        return(l, l3)
