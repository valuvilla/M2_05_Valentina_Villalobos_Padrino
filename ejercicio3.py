invitación=print("vamos a contar el número de veces que aparece la letra A")
def letra_A(invitación):
    veces=0
    while True:
        palabra=input("Introduce palabras: ")
        for letra in palabra:
            if "a" == letra or "A" == letra:
                veces+=1
        if "." in palabra:
            break

    return "La letra A ha aparecido "+ str(veces)+ " veces"

print(letra_A(invitación))