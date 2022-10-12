from itertools import count


print("introduce tres valores: ")
valor1=int(input("Valor1: "))
valor2=int(input("Valor2: "))
valor3=int(input("Valor3: "))
valor=valor1,valor2,valor3
print(valor)


if valor1==0:
    print("¡el primer número intoducido es 0")
else:
    if valor1<=valor2<=valor3:
        print("valores ordenados")
    else:
         print("valores no ordenados")

import sys

valores=[]
def Evaluación_lista(valores):
    while True:

        print ("Introduzca valores")
        
        for i in range(3):
             valores.append(input("valor: "))
        
        try:
             valores[0]=int(valores[0])
             valores[1]=int(valores[1])
             valores[2]=int(valores[2])
        except:
            print("Valor no valido", file=sys.stderr)     
            pass
        else:
            if valores[0]==0:
                print("¡el primer número intoducido es 0")
                break
            else:
                if int(valores[0])<=int(valores[1])<=int(valores[2]):
                    print("valores ordenados")
                    break
                else:
                    print("valores no ordenados")
                    break
        sys.exit()  

print(Evaluación_lista(valores))        
                


inicio=print("vamos a contar el número de veces que aparece la letra A")
def letra_A(inicio):
    veces=0
    while True:
        palabra=input("Introduce palabras: ")
        for letra in palabra:
            if "a" == letra:
                veces+=1
        if "." in palabra:
            break

    return "La letra A ha aparecido "+ str(veces)+ " veces"

print(letra_A(inicio))

lista_palabras=[]
for j in range(1,4):
    lista_palabras.append(input("Palabra: "))
    
#print(lista_palabras)

def palabra_mas_larga(lista_palabras):
    longitudes=[]
    for x in lista_palabras:
        longitudes.append((len(x), x))
  
    longitudes.sort()  
    

    return 'la pabra más larga de la lista es '+str(longitudes[-1][1])+' con '+str(longitudes[-1][0])+' caracteres'
    
print(palabra_mas_larga(lista_palabras))
    
