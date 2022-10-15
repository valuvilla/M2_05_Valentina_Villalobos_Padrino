import sys

#Definimos una función que controle que el numero introducido sea un numero

def valor(valor):
    while True:
        #entramos en un bucle infinito

        #pedimos por teclado un valor
        valor=input("Valor: ")
        
        """
        Comprabamos que tal valor es un numero
        No se saldrá del bucle hasta que se capture un entero
        """
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
            pass
        else:
            break
            sys.exit()
        
    return valor


#Funcion para evaluar los valores

def Evaluación(valor):
        #Definimos la variables

        print("introduce tres valores: ")

        #LLamamos a la función antes definida para evaluar la informacion dada.
        valor1=valor(valor)
        valor2=valor(valor)
        valor3=valor(valor) 
        """
        Aplicamos las condiciones de la actividad 
        """  
        if valor1!=0:
            if valor1<=valor2<=valor3:
                print("valores ordenados")
            else:
                print("valores no ordenados")
               
        #Al introducir el 0 en primer valor, el sistema nos dará error.        
        else:
            raise ValueError("{} no es valido".format(valor1))          


        return valor1, valor2, valor3


print(Evaluación(valor))