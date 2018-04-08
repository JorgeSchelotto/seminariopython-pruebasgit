jugadores = {}
stats = {}

jugador = input('Ingrese Nombre del jugador. Ingrese cancelar para cortar la carga: ')

while(jugador != 'cancelar'):
    nivel = input('Ingrese Nivel del jugador: ')
    puntaje = int(input('Ingrese puntaje del jugador: '))
    horasJuego = input('Ingrese horas de juego del jugador: ')

    stats['nivel'] = nivel
    stats['puntaje'] = puntaje
    stats['horas'] = horasJuego
    jugadores[jugador] = stats

    jugador = input('Ingrese Nombre del jugador: ')

print(jugadores['123'])