import numpy as np
import random


#1a. crear tableros
def tablero(): 
    tablero = np.full((5,5), " ")
    return tablero

##1b.crear tableros sin verlos
tablero_jug1 = tablero()
tablero_jug2 = tablero()

#2a. colocar barcos
def colocar_barcos(tablero, lista):
    for barco in lista:
        for posicion in barco:
           tablero[posicion] = "O"  
    return tablero

def barcos_jug2():
    barcos = [2, 3]
    for length in barcos:
        placed = False
        while not placed:
            orientation = random.choice(["H", "V"])
            if orientation == "H":
                fila = random.randint(0, 4)
                col = random.randint(0, 5 - length)
                if np.all(tablero_jug2[fila, col:col+length] == " "):
                    tablero_jug2[fila, col:col+length] = "O"
                    placed = True
            else:  # Vertical
                fila = random.randint(0, 5 - length)
                col = random.randint(0, 4)
                if np.all(tablero_jug2[fila:fila+length, col] == " "):
                    tablero_jug2[fila:fila+length, col] = "O"
                    placed = True

    return tablero_jug2 


#3a1. disparar y turnos:

def disparar(tablero, fila, columna):
    resultado = None 
    if tablero[fila, columna]== "O":
        print ("¡¡tocado!!")
        tablero[fila, columna] = "X"
        resultado = True
    elif tablero[fila, columna]== " ":
        print ("¡agua!")
        tablero[fila, columna] = "#"
        resultado = False

    else:
        print("Ya disparaste allí. Intenta otra vez.")
        resultado = None

    return tablero, resultado

#3.a2 barcos que todavia flotan:  
def barcos_flotando(tablero):
    return np.any(tablero == "O")

#3b. disparar y turnos:

turno = 1  #  por defecto de Jugador 1

while barcos_flotando(tablero_1) and barcos_flotando(tablero_2):
    print(f"Turno del Jugador {turno}")
    
    if turno == 1:
        fila = int(input("Fila: (0:4)"))
        col = int(input("Columna: (0:4)"))
        tablero2, acierto = disparar(tablero_2, fila, col)

        print("\nTu tablero:") # Mostrar tablero1 despues de cada tiro
        print(tablero_1)
        
        # Mostrar tablero2 con niebla (solo X y # visibles)
        print("\nTablero2  (lo que has descubierto):")
        tablero2_visible = np.where(tablero_2 == "O", " ", tablero_2)
        print(tablero2_visible)
        if acierto is False: # if miss, change turn
            turno = 2 
    else:
        fila = random.randint(0, 4)
        col = random.randint(0, 4)
        tabero1, acierto = disparar(tablero_1, fila, col)
        if acierto is False:
            turno = 1

#4. Determinar el ganador

if barcos_flotando(tablero_1):
    print("¡Jugador 1 gana!")
else:
    print("¡El ordenador gana!")