nombre_jugador = input("¡Bienvenido al Juego de Laberinto de Texto!\nPor favor, introduce tu nombre: ")

print(f"Bienvenido, {nombre_jugador}! ¡Vamos a empezar a explorar el laberinto!")


laberinto = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", "#", ".", ".", ".", "#", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

# Función para imprimir el mapa del laberinto
def imprimir_laberinto():
    for fila in laberinto:
        print("".join(fila))

# Inicializa la posición del personaje
fila_personaje = 1
columna_personaje = 2

# Bucle principal del juego
while True:
    
    # Imprime el mapa del laberinto
    imprimir_laberinto()

    movimiento = input("Mueve al personaje con las teclas w s a d (q para salir): ")

    # Procesa la entrada del jugador
    if movimiento == "q":
        break  # Salir del juego
    elif movimiento == "w" and laberinto[fila_personaje - 1][columna_personaje] != "#":
        fila_personaje -= 1
    elif movimiento == "s" and laberinto[fila_personaje + 1][columna_personaje] != "#":
        fila_personaje += 1
    elif movimiento == "a" and laberinto[fila_personaje][columna_personaje - 1] != "#":
        columna_personaje -= 1
    elif movimiento == "d" and laberinto[fila_personaje][columna_personaje + 1] != "#":
        columna_personaje += 1

# Mensaje de despedida
print("¡Gracias por jugar!")