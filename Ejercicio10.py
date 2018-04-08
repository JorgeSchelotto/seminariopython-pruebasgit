jugadores = {}
stats = {}
stats2 = {}
stats3 = {}


#Hardcodeo para facilitar la carga
jugador = 'Vincent Price'
stats = {}
stats[jugador] = 'The Abominable Dr. Phibes'
stats['nivel'] = 10
stats['puntaje'] = 500000000
stats['horas'] = '10:30:02'
jugadores[jugador] = stats



jugador = 'Boris Karloff'
stats2[jugador] = 'The Mummy'
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


maximo= -1
for key in jugadores:
    if maximo < jugadores[key].get('puntaje'):
        maximo = jugadores[key].get('puntaje')
        maxJug = key


print('Jugador con mas puntaje: ', maxJug, maximo)
