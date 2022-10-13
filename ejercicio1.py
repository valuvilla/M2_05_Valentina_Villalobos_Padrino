import sys

def valor(valor):
    while True:
        valor=input("Valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
            pass
        else:
            break
        sys.exit()
    return valor



def Evaluación(valor):
        #Definimos la variables
        print("introduce tres valores: ")
        valor1=valor(valor)
        valor2=valor(valor)
        valor3=valor(valor)   
        if valor1!=0:
            if valor1<=valor2<=valor3:
                print("valores ordenados")
            else:
                print("valores no ordenados")
                sys.exit()
        else:
            raise ValueError("{} no es valido".format(valor1))               
        return valor1, valor2, valor3


print(Evaluación(valor))