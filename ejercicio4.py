print('Vamos a averiguar cual es la palabra más larga de nuestra lista')
print('Para ello el usuario construira su propia lista')

#Creamos una lista vacia 

lista_palabras=[]

#Mediante el bucle for rellenamos la lista de valores
for j in range(4):
    lista_palabras.append(input("Palabra: "))
    
#print(lista_palabras)

#Funcion que analice la palabra más larga
def palabra_mas_larga(lista_palabras):
    
    #Creamos otra lista vacia
    longitudes=[]

    #Asociamos a cada palabra su longitud.
    """
    Es escencial poner primer la longitud de la palabra
    Será importante a la hora de ordenar los elementos de la lista
    """
    for x in lista_palabras:
        longitudes.append((len(x), x))
  
    #Ordenamos la lista del valor más pequeño al más grande
    """
    En este caso, al estar primero el numero se ordenara numericamente
    """
    longitudes.sort()  
    

    return 'la pabra más larga de la lista es '+str(longitudes[-1][1])+' con '+str(longitudes[-1][0])+' caracteres'

    
print(palabra_mas_larga(lista_palabras))
    