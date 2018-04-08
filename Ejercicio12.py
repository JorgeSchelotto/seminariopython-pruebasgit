anim = {'Gato Montes':2, 'Yacare overo':4, 'Boa acuática':5}

#Cargo una lista con los nombres de los animales (key de anim)
claves = []
for key in anim:
    claves.append(key)

#Pongo contador para recorrer la lista de animales en 0
animal=0

for key in anim:
    # Recorro anim y guardo clave y valor en dos variables
    string = claves[animal]
    i = anim[key]
    lista = []

    #Cargo una lista con tantos under scopes como caracteres tiene string
    for j in string:
        lista.append('_')

    #Cambio el caracter indicado
    lista[i] = string[i]

    #Transformo la lista en un string e imprimo
    final = " ".join(lista)
    print(final)
    #Incremento contador animal
    animal+=1
