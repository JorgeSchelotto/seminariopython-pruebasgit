

#Hardcodeo para facilitar la prueba

jugadores = {}
stats = {}
stats2 = {}
stats3 = {}
stats4 = {}


jugador = 'Vincent Price'
stats = {}
stats['jugador'] = 'The Abominable Dr. Phibes'
stats['nivel'] = 10
stats['puntaje'] = 5
stats['horas'] = '10:30:02'
jugadores[jugador] = stats


jugador = 'Boris Karloff'
stats2['jugador'] = 'The Mummy'
stats2['nivel'] = 21
stats2['puntaje'] = 200
stats2['horas'] = '200:30:02'
jugadores[jugador] = stats2


jugador = 'Vela Lugosi'
stats3['jugador'] = 'Dracula'
stats3['nivel'] = 50
stats3['puntaje'] = 78000
stats3['horas'] = 'is dead'
jugadores[jugador] = stats3



#igresa datos del jugador a buscar


jugador = input('Ingrese Nombre del jugador: ')
nivel = input('Ingrese Nivel del jugador: ')
puntaje = int(input('Ingrese puntaje del jugador: '))
horasJuego = input('Ingrese horas de juego del jugador: ')
stats4['nivel'] = nivel
stats4['puntaje'] = puntaje
stats4['horas'] = horasJuego

#Si existe lo cambia. Sino no hace nada

if jugador in jugadores:
    if stats4.get('puntaje') > jugadores[jugador].get('puntaje'):
        jugadores[jugador] = stats4
    else:
        print('El usuario no esta registrado')


#Creo una lista nueva y cargo todos los puntajes de los jugadores
listaPuntos = []
for key in jugadores:
    listaPuntos.append(jugadores[key].get('puntaje'))

#Ordeno la lista de mayor a menor
listaPuntos.sort(reverse=True)

#Creo el ranking 10
print('Top 10 jugadores')

#Puse in range(3) porque hay cargados solo 3 jugadores, pero deberia decir range(10)
for i in range(3):
    #recorro el diccionario jugadores
    for key in jugadores:
        #Si el puntaje del jugador es igual al primer puntaje de la lista "con los puntos" lo imprimo sino
        #avanzo el diccionario de jugadores hasta que encuentre un jugador con ese puntaje
        if listaPuntos[i] == jugadores[key].get('puntaje'):
            print(i+1,':', key + ':', jugadores[key].get('puntaje'))
