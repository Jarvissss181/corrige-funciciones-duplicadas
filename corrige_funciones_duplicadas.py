# -*- coding: utf-8 -*-

# esta versión es la base para trabajar en la evaluación III
def crear_tablero():
    tablero = []
    fila = 0
    while fila < 3:
        tablero.append([" ", " ", " "])
        fila += 1
    return tablero


def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
    fila = 0
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:
            print("-" * 5)
        fila += 1

def imprimir_tablero(tablero):
        print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
        print("-----")
        print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
        print("-----")
        print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")



def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

# Agregar en juego_completo():
if tablero_lleno(tablero):
    print("¡Empate!")
    break


import random

def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"

# Modificar el turno en juego_completo():
if jugador_actual == "X":
    movimiento_jugador(tablero)
else:
    movimiento_ia(tablero)

def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        movimiento_jugador(tablero, jugador_actual)

        if hay_ganador(tablero):
            print(f"¡{jugador_actual} ha ganado!")
            break

        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"


juego_completo()

#tablero = crear_tablero()
#imprimir_tablero(tablero)
#movimiento_jugador(tablero)
#imprimir_tablero(tablero)

# prompt: Elimina las funciones innecesarias o duplicadas

import random
# esta versión es la base para trabajar en la evaluación III

def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
    print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
    print("-----")
    print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
    print("-----")
    print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")


def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True


def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"


def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")

        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero)

        if hay_ganador(tablero):
            imprimir_tablero(tablero) # Print final board
            print(f"¡{jugador_actual} ha ganado!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero) # Print final board
            print("¡Empate!")
            break

        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"


juego_completo()

#tablero = crear_tablero()
#imprimir_tablero(tablero)
#movimiento_jugador(tablero)
#imprimir_tablero(tablero)

# prompt: Asegúrate de que el juego detecte correctamente los empates

def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")

        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero)

        if hay_ganador(tablero):
            imprimir_tablero(tablero) # Print final board
            print(f"¡{jugador_actual} ha ganado!")
            break

        # Check for a draw after checking for a winner
        if tablero_lleno(tablero):
            imprimir_tablero(tablero) # Print final board
            print("¡Empate!")
            break

        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"


juego_completo()

import random

# esta versión es la base para trabajar en la evaluación III

def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
    print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
    print("-----")
    print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
    print("-----")
    print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")


def movimiento_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input("Elige fila (0, 1, 2): "))
            columna = int(input("Elige columna (0, 1, 2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("¡Casilla ocupada!")
            else:
                print("¡Entrada inválida! Por favor, elige fila y columna entre 0 y 2.")
        except ValueError:
            print("¡Entrada inválida! Por favor, ingresa números.")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True


def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"


def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")

        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero)

        if hay_ganador(tablero):
            imprimir_tablero(tablero) # Print final board
            print(f"¡{jugador_actual} ha ganado!")
            break

        # Check for a draw after checking for a winner
        if tablero_lleno(tablero):
            imprimir_tablero(tablero) # Print final board
            print("¡Empate!")
            break

        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"


juego_completo()
