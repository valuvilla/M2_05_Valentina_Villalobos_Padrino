import sys

def valor(valor):
    while True:
        valor=input("valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
            pass
        else:
            break
            sys.exit()
            
    return valor



valores=[]
def Evaluación_lista(valores):

        print ("Introduzca valores")
        for i in range(3):
             valores.append(valor(i))

        
        if valores[0]!=0:
            if valores[0]<=valores[1]<=valores[2]:
                print("{} están ordenados en creciente".format(valores))
            else:
                print("{} no están ordenados".format(valores))

        else:
            raise ValueError("{} no es valido".format(valores[0]))   
        return 'FIN'
        

print(Evaluación_lista(valores)) 