invitación=print("vamos a contar el número de veces que aparece la letra A")
print("Recuerda que para salir del bucle, deberás pulsar el punto")
def letra_A(invitación):
    while True:
        #Entramos un  bucle infinto

        #Definimos una varible
        palabra=input("Introduce palabras: ")

        """
        Entramos un bucle for que cuente las letras
        Se saldrá del bucle cuando se dectecte un punto
        """
        veces=palabra.count("a")+palabra.count("A")
    

        if "." in palabra:
            break

    return "La letra A ha aparecido "+ str(veces)+ " veces"


print(letra_A(invitación))