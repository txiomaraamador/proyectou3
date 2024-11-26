import matplotlib.pyplot as plt
import time

# Función para inicializar los postes y los discos
def inicializar_torres(n):
    return [list(range(n, 0, -1)), [], []]

# Función para graficar las torres y los discos
def graficar_torres(torres, n, movimientos_restantes, ax):
    ax.clear()  # Limpiar el gráfico actual
    ax.set_xlim(-0.5, 2.5)  # Ancho total del gráfico
    ax.set_ylim(0, n * 0.6 + 0.5)  # Ajustar la altura máxima del gráfico
    ax.axis('off')

    # Colores y estilo para las torres y los discos
    torre_color = '#8B4513'  # Color marrón para los postes
    disco_colores = ['#FF69B4', '#FF1493', '#DB7093', '#C71585', '#FFB6C1']  # Colores de los discos

    # Ajuste dinámico para el ancho y la altura de los discos
    max_ancho = 0.9  # Ancho máximo relativo de los discos
    alto_disco = 0.4  # Altura constante de los discos
    altura_poste = n * 0.5  # Ajustar la altura de los postes según el número de discos

    # Dibujar los postes
    for i in range(3):
        ax.plot([i, i], [0, altura_poste], color=torre_color, linewidth=3, solid_capstyle='round')  # Altura ajustada

    # Dibujar los discos
    for i in range(3):
        altura = 0
        for disco in torres[i]:
            ancho = disco * (max_ancho / n)  # Ajustar ancho de disco
            color = disco_colores[disco % len(disco_colores)]
            # Dibujar cada disco con borde
            rect = plt.Rectangle((i - ancho / 2, altura), ancho, alto_disco, color=color, ec='black', lw=1)
            ax.add_patch(rect)
            altura += alto_disco + 0.1  # Espaciado vertical entre discos

    # Mostrar los movimientos restantes
    ax.text(1.5, n * 0.6 + 0.2, f"Movimientos restantes: {movimientos_restantes}", 
            fontsize=12, color='black', ha='center', va='bottom', bbox=dict(boxstyle="round", facecolor="white", edgecolor="black"))

    plt.pause(0.5)  # Pausa breve para visualizar el cambio

# Función recursiva para resolver Torres de Hanoi con visualización continua
def torres_de_hanoi(n, origen, auxiliar, destino, torres, ax, movimientos):
    if n == 1:
        disco = torres[origen].pop()
        torres[destino].append(disco)
        movimientos[0] -= 1
        graficar_torres(torres, len(torres[0]) + len(torres[1]) + len(torres[2]), movimientos[0], ax)
        return
    
    torres_de_hanoi(n - 1, origen, destino, auxiliar, torres, ax, movimientos)
    disco = torres[origen].pop()
    torres[destino].append(disco)
    movimientos[0] -= 1
    graficar_torres(torres, len(torres[0]) + len(torres[1]) + len(torres[2]), movimientos[0], ax)
    torres_de_hanoi(n - 1, auxiliar, origen, destino, torres, ax, movimientos)

# Configuración inicial con interacción del usuario
while True:
    try:
        n = int(input("¿Cuántos discos quieres mover? (1 o más): "))
        if n < 1:
            print("Por favor, ingresa un número válido (1 o más).")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Calcular y mostrar el número de movimientos necesarios
movimientos_totales = 2**n - 1
print(f"Con {n} discos, necesitarás {movimientos_totales} movimientos para resolverlo.")

# Inicializar las torres y preparar la visualización
torres = inicializar_torres(n)
movimientos = [movimientos_totales]  # Usamos una lista para modificar el contador dentro de la recursión
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4))

# Graficar estado inicial y resolver el problema
graficar_torres(torres, n, movimientos[0], ax)
time.sleep(0.5)
torres_de_hanoi(n, 0, 1, 2, torres, ax, movimientos)

plt.ioff()  # Desactivar modo interactivo
plt.show()  # Mantener el gráfico abierto al final
