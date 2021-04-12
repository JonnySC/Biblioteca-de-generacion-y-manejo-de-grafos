# JonnySC-Biblioteca-de-generacion-y-manejo-de-grafos

Proyecto1
Escribir una biblioteca orientada a objetos, en Python 3.6, para describir y utilizar grafos. Debe, por lo menos contar con una clase llamada Grafo, una clase llamada Nodo y una clase llamada Arista. Asimismo, se deben realizar funciones para generar grafos con los siguientes modelos de generación:

Modelo Gm,n de malla. Crear m*n nodos. Para el nodo ni,j crear una arista con el nodo ni+1,j y otra con el nodo ni,j+1, para i<m y j<n
def grafoMalla(m, n, dirigido=False):

   """
   
   Genera grafo de malla
   
   :param m: número de columnas (> 1)
   
   :param n: número de filas (> 1)
   
   :param dirigido: el grafo es dirigido?
   
   :return: grafo generado
   
   """

