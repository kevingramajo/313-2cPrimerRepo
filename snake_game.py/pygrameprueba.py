# 🐍 Código del Snake en Pygame
import pygame
import random
import constantes

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("Snake en Python")

# Fuente
fuente = pygame.font.SysFont("Arial", 25)

# Botones de Inicio
boton_jugar = pygame.Rect(constantes.ANCHO / 2-100, constantes.ALTO / 2 - 50, 200, 50)
boton_salir = pygame.Rect(constantes.ANCHO / 2 - 100, constantes.ALTO / 2 + 50, 200, 50)
texto_boton_jugar = fuente.render("JUGAR", True, constantes.NEGRO)
texto_boton_salir = fuente.render("SALIR", True, constantes.BLANCO)

# Dibujar texto
def mostrar_mensaje(texto: str, color: tuple, pos: tuple):
    render = fuente.render(texto, True, color)
    ventana.blit(render, pos)

def pantalla_inicio():
    ventana.fill(constantes.PURPURA)
    mostrar_mensaje("Mi primer Juego", constantes.NEGRO, (constantes.ANCHO / 2 - 200, constantes.ALTO / 2 - 200))
    pygame.draw.rect(ventana, constantes.AMARILLO, boton_jugar)
    pygame.draw.rect(ventana, constantes.ROJO, boton_salir)
    ventana.blit(texto_boton_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

# Juego principal (recursivo en caso de perder)


def juego():
# posición inicial de la serpiente
    serpiente = [[100, 100]]
    direccion = "DERECHA"
    comida = [random.randrange(0, constantes.ANCHO, constantes.BLOQUE), random.randrange(0, constantes.ALTO, constantes.BLOQUE)]
    reloj = pygame.time.Clock()
    puntaje = 0
  # Eventos
    mostrar_inicio = True
    run = True
    while run:
        if mostrar_inicio:
            pantalla_inicio()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run == False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.collidepoint(event.pos):
                        mostrar_inicio = False
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direccion != "ABAJO":
                    direccion = "ARRIBA"
                elif event.key == pygame.K_DOWN and direccion != "ARRIBA":
                    direccion = "ABAJO"
                elif event.key == pygame.K_LEFT and direccion != "DERECHA":
                    direccion = "IZQUIERDA"
                elif event.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                    direccion = "DERECHA"
    # Mover serpiente
    cabeza = list(serpiente[-1])
    if direccion == "ARRIBA":
        cabeza[1] -= constantes.BLOQUE
    elif direccion == "ABAJO":
        cabeza[1] += constantes.BLOQUE
    elif direccion == "IZQUIERDA":
        cabeza[0] -= constantes.BLOQUE
    elif direccion == "DERECHA":
        cabeza[0] += constantes.BLOQUE
    serpiente.append(cabeza)
    # Comer comida
    if cabeza == comida:
        puntaje += 1
        comida = [random.randrange(0, constantes.ANCHO, constantes.BLOQUE), random.randrange(0, constantes.ALTO, constantes.BLOQUE)]
    else:
        serpiente.pop(0)  # eliminar cola
    # Revisar colisiones (paredes o cuerpo)
    if (cabeza in serpiente[:-1] or
        cabeza[0] < 0 or cabeza[0] >= constantes.ANCHO or
        cabeza[1] < 0 or cabeza[1] >= constantes.ALTO):
        # Recursividad para reiniciar
        return juego()
    # Dibujar
    ventana.fill(constantes.NEGRO)
    for x, y in serpiente:
        pygame.draw.rect(ventana, constantes.VERDE, (x, y, constantes.BLOQUE, constantes.BLOQUE))
    pygame.draw.rect(ventana, constantes.ROJO, (comida[0], comida[1], constantes.BLOQUE, constantes.BLOQUE))
    mostrar_mensaje(f"Puntos: {puntaje}", constantes.ROJO, (10, 10))
    pygame.display.flip()
    reloj.tick(10)

# Ejecutar
juego()