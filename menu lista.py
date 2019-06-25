def MostrarMenu():
    opcion = -1

    while opcion < 0 or opcion > 7:
        print ("seleccione una opcion del menu:  ")
        print ("\t1: capturar una lista.")
        print ("\t2: sacar los ultimos j valores.")
        print ("\t3: invertir lista.")
        print ("\t4: mostrar sub-conjunto.")
        print ("\t5: mostrar elemento dada una posicion.")
        print ("\t6: buscar elemento.")
        print ("\t7: modificar la lista")
        print ("\t0: salir ")

        opcion = int(input("opcion :"))
    return opcion

def MostrarSubMenu():
    opcion = -1

    while opcion < 0 or opcion > 6:
        print ("seleccione una opcion del submenu:  ")
        print ("\t1: agregar elementos al final de la lista: ")
        print ("\t2: agregar elementos al incio de la lista : ")
        print ("\t3: agregar elementos a una posicion indicada")
        print ("\t4: captuar una nueva lista ")
        print ("\t5: eliminar un elemento de una posicion indicada")
        print ("\t6: buscar y eliminar un elemento")
        print ("\t0: salir al menu anterior ")

        opcion = int(input("opcion :"))
    return opcion

def CapturarLista():
    nuevaLista = []
    nuevaLista = [int(valor) for valor in input().split()]
    return nuevaLista

def SacarValores(lista,j):
    while j > 0:
        lista.pop()
        j-=1
    return lista

def InvertirLista(lista):
    return lista [::-1]

def subconjunto(lista,d,h,s):
    return lista [d:h:s]

def encontrarvalor(lista,posicion):
    return lista[posicion]

def encontrarvalorexacto (lista ,valor):
    return lista.index(valor)

def AgregarElemento (lista,elemento,posicion):
    lista.insert(posicion,elemento)
    
def AgregarNuevaLista(listado, alFinal):
    NuevaLista= CapturarLista()
    return lista + nuevaLista if alFinal else nuevaLista + lista

    """"if alFinal:
        return lista.extend(nuevaLista)
    else:
        return nuevaLista.extend(lista)""""
def EliminarPosicion(lista,posicion):
    del lista[posicion]
    
def EliminarElemento ( lista,elemento):
    try:
    lista.remove(elemento)
    except :
        print ("fulando no esta en la lista")
     
listado = []
seleccion = -1
while seleccion !=0:
    print ("la lista es : {0}, y su longitud : {1}".format(listado,len(listado)))
    seleccion = MostrarMenu()
    
    if seleccion == 1:
        listado = CapturarLista()
    elif seleccion == 2:
        nuevaEntrada = int(input("digite la cantidad de valores a sacar"))
        listado = SacarValores(listado,nuevaEntrada)
    elif seleccion == 3:
        print(InvertirLista(listado))
    elif seleccion == 4:
        desde = int(input("desde"))
        hasta = int(input("hasta"))
        step = int(input("step"))
        subconjunto(listado,desde,hasta,step)
    elif seleccion == 5:
        pos = int(input("digite la posicion"))
        print (obtenerElemento(listado,pos))
    elif seleccion == 6:
        val = int(input("digite el valor:"))
        print (encontrarvalorexacto(listado,val))
    elif seleccion == 7:
        nuevaSeleccion = -1
        while nuevaSeleccion != 0:
         nuevaSeleccion = MostrarSubMenu()

         if nuevaSeleccion == 1:
             AgregarElemento(listado,int(input("digite el nuevo valor: ")),len(listado)
                             
         elif nuevaSeleccion == 2:
             AgregarElemento(listado,int(input("digite el nuevo valor: ")),0)   
         elif nuevaSeleccion == 3:
             AgregarElemento(listado,int(input("digite el nuevo valor: ")),int(input("indique la posicion: ")))
         elif nuevaSeleccion == 4:
             alFinal = input("digite 1 para agregar al incio o 2 para el final") == "2"              
             AgregarNuevaLista(listado, alFinal):
             listado = AgregarNuevaLista(listado,alFinal)
         elif nuevaSeleccion == 5:
             EliminarPosicion (listado, int(input("digite la posicion para eliminar"))
         elif nuevaSeleccion == 6:
             EliminarElemento(listado , int(input("digite el elemento a eliminar"))
                        
