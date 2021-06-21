import nodo 
import arista
import grafo

#Funcion principal de llamado del programa
def main():
    #Lamado a clase del modelo
    a = Malla()
    b = Erdosrenyi()
    c = Gilbert()
    d =

    #ejecución de la funcion del modelo
    a.malla()
    #Se ejecuta erdos que a su vez devuelve las cadenas de vertices y aristas
    #a variables para poder ser usadas en otras clases o funciones
    l, l3 = b.erdosrenyi()
    c.gilbert()
main()
