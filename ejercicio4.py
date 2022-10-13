print('Vamos a averiguar cual es la palabra más larga de nuestra lista')
print('Para ello el usuario construira su propia lista')

lista_palabras=[]
for j in range(4):
    lista_palabras.append(input("Palabra: "))
    
#print(lista_palabras)

def palabra_mas_larga(lista_palabras):
    longitudes=[]
    for x in lista_palabras:
        longitudes.append((len(x), x))
  
    longitudes.sort()  
    

    return 'la pabra más larga de la lista es '+str(longitudes[-1][1])+' con '+str(longitudes[-1][0])+' caracteres'
    
print(palabra_mas_larga(lista_palabras))
    