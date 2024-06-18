'''
Juego: Battle Ship
'''
import random

def inicializar_tablero():
    return [[" " for _ in range(10)] for _ in range(10)]

def colocar_barcos(tablero):
    for tamaño in [5, 4, 3, 2]:  # tamaños de los barcos
        colocado = False
        while not colocado:
            orientacion = random.choice(['horizontal', 'vertical'])
            fila_inicio = random.randint(0, 9)
            col_inicio = random.randint(0, 9)

            if orientacion == 'horizontal' and col_inicio + tamaño <= 10:
                if all(tablero[fila_inicio][col_inicio + i] == " " for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila_inicio][col_inicio + i] = "B"
                    colocado = True
            elif orientacion == 'vertical' and fila_inicio + tamaño <= 10:
                if all(tablero[fila_inicio + i][col_inicio] == " " for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila_inicio + i][col_inicio] = "B"
                    colocado = True

def imprimir_tablero(tablero, es_visible):
    print("  " + " ".join([str(i) for i in range(10)]))
    for idx, fila in enumerate(tablero):
        if es_visible:
            print(idx, " ".join(fila))
        else:
            print(idx, " ".join(['X' if c == 'B' else c for c in fila]))

def realizar_disparo(tablero, fila, col):
    if tablero[fila][col] == "B":
        tablero[fila][col] = "H"
        print("¡Acertaste!")
    elif tablero[fila][col] == " ":
        tablero[fila][col] = "F"
        print("Fallaste.")
    else:
        print("Ya disparaste a esa posición.")

def juego():
    tablero_jugador = inicializar_tablero()
    tablero_computadora = inicializar_tablero()
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_computadora)

    turno_jugador = True

    while True:
        print("Tu tablero:")
        imprimir_tablero(tablero_jugador, True)
        print("Tablero de la computadora:")
        imprimir_tablero(tablero_computadora, False)

        if turno_jugador:
            try:
                fila = int(input("Elige fila para disparar: "))
                col = int(input("Elige columna para disparar: "))
                realizar_disparo(tablero_computadora, fila, col)
            except ValueError:
                print("Por favor, introduce un número válido.")
            turno_jugador = False
        else:
            # La computadora dispara aleatoriamente
            fila, col = random.randint(0, 9), random.randint(0, 9)
            realizar_disparo(tablero_jugador, fila, col)
            turno_jugador = True

        # Comprobación de fin de juego
        if all(c != 'B' for fila in tablero_computadora for c in fila):
            print("¡Felicidades! Has ganado el juego.")
            break
        if all(c != 'B' for fila in tablero_jugador for c in fila):
            print("La computadora gana el juego.")
            break

juego()

