import matplotlib.pyplot as plt
import time

# Función para inicializar los postes y los discos
def inicializar_torres(n):
    return [list(range(n, 0, -1)), [], []]

# Función para graficar las torres y los discos
def graficar_torres(torres, n, ax):
    ax.clear()  # Limpiar el gráfico actual
    ax.set_xlim(-0.5, 2.5)  # Ancho total del gráfico
    ax.set_ylim(0, n * 0.6)  # Ajustar la altura máxima del gráfico
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

    plt.pause(0.3)  # Pausa breve para visualizar el cambio

# Función recursiva para resolver Torres de Hanoi con visualización continua
def torres_de_hanoi(n, origen, auxiliar, destino, torres, ax):
    if n == 1:
        disco = torres[origen].pop()
        torres[destino].append(disco)
        graficar_torres(torres, len(torres[0]) + len(torres[1]) + len(torres[2]), ax)
        return
    
    torres_de_hanoi(n - 1, origen, destino, auxiliar, torres, ax)
    disco = torres[origen].pop()
    torres[destino].append(disco)
    graficar_torres(torres, len(torres[0]) + len(torres[1]) + len(torres[2]), ax)
    torres_de_hanoi(n - 1, auxiliar, origen, destino, torres, ax)

# Configuración inicial
n = 5  # Cambia el número de discos para probar
torres = inicializar_torres(n)

# Configuración de matplotlib para la visualización continua
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4))

# Graficar estado inicial y resolver el problema
graficar_torres(torres, n, ax)
time.sleep(0.5)
torres_de_hanoi(n, 0, 1, 2, torres, ax)

plt.ioff()  # Desactivar modo interactivo
plt.show()  # Mantener el gráfico abierto al final
