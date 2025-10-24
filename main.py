
import numpy as np
import random

#1a. crear tableros
from utiles import tablero


##1b.crear tableros sin verlos
tablero_jug1 = tablero()
tablero_jug2 = tablero()

#2a. colocar barcos
from utiles import colocar_barcos

#2b.colocar barcos en tableros:

barcos_jug1 = [[(0, 1),(1,1)], [(3,2), (3,3),(3,4)]]

# esto fue de manera manual. 
#barcos_jug2 = [[(2, 3),(2,4)], [(1,1), (2,1),(3,1)]]

# esto es de manera random que intentaba hacer:

from utiles import barcos_jug2

print ("jugador 1" , "--"*10)
tablero_1 = colocar_barcos(tablero_jug1,barcos_jug1)
print(tablero_1) #####

print ("ordinador" , "--"*10)
tablero_2 = barcos_jug2()
print (tablero_2)


#3a1. disparar y turnos:
from utiles import disparar


#3.a2 barcos que todavia flotan: 
from utiles import barcos_flotando
 

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