# 🐍 Código del Snake en Pygame con Game Over
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
fuente_oughter = pygame.font.Font("C:\\Users\\Kevin\\OneDrive\\Escritorio\\Repositorio\\snake_game.py\\assets\\fonts\\Oughter.otf", (50))
#fuente_Urban = pygame.font.Font("C:\\Users\\Kevin\\OneDrive\\Escritorio\\Repositorio\\snake_game.py\\assets\\fonts\\Urban Shadow Sans Serif", (50))

# Botones de Inicio
boton_jugar = pygame.Rect(constantes.ANCHO / 2-100, constantes.ALTO / 2 - 50, 200, 50)
boton_salir = pygame.Rect(constantes.ANCHO / 2 - 100, constantes.ALTO / 2 + 50, 200, 50)
boton_dificultad = pygame.Rect(constantes.ANCHO / 2 - 100, constantes.ALTO / 2 + 150, 200, 50)
boton_reinicio = pygame.Rect(constantes.ANCHO / 2 - 100, constantes.ALTO / 2, 200, 50)

# Textos
texto_boton_jugar = fuente.render("JUGAR", True, constantes.NEGRO)
texto_boton_salir = fuente.render("SALIR", True, constantes.BLANCO)
texto_boton_dificultad = fuente.render("HARDCORE", True, constantes.NARANJA)
texto_boton_reinicio = fuente.render("REINICIAR", True, constantes.BLANCO)

# Dibujar texto
def mostrar_mensaje(texto: str, color: tuple, pos: tuple):
    render = fuente.render(texto, True, color)
    ventana.blit(render, pos)

def mostrar_game_over(texto: str, color: tuple, pos: tuple):
    render = fuente_oughter.render(texto, True, color)
    ventana.blit(render, pos)

def pantalla_inicio():
    ventana.fill(constantes.PURPURA)
    mostrar_mensaje("Mi primer Juego", constantes.NEGRO, (constantes.ANCHO / 2 - 100, constantes.ALTO / 2 - 200))
    pygame.draw.rect(ventana, constantes.AMARILLO, boton_jugar)
    pygame.draw.rect(ventana, constantes.ROJO, boton_salir)
    pygame.draw.rect(ventana, constantes.NEGRO, boton_dificultad)
    ventana.blit(texto_boton_jugar, (boton_jugar.x + 55, boton_jugar.y + 10))
    ventana.blit(texto_boton_dificultad, (boton_dificultad.x + 30, boton_dificultad.y + 10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 60, boton_salir.y + 10))
    pygame.display.update()

def pantalla_game_over(puntaje):
    ventana.fill(constantes.NEGRO)
    mostrar_game_over("GAME OVER", constantes.ROJO, (constantes.ANCHO / 2 - 180, constantes.ALTO / 2 - 250))
    mostrar_mensaje(f"Puntaje: {puntaje}", constantes.BLANCO, (constantes.ANCHO / 2 - 60, constantes.ALTO / 2 - 100))
    
    # Botones
    pygame.draw.rect(ventana, constantes.VERDE, boton_reinicio)
    pygame.draw.rect(ventana, constantes.ROJO, boton_salir)
    ventana.blit(texto_boton_reinicio, (boton_reinicio.x + 40, boton_reinicio.y + 10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 60, boton_salir.y + 10))
    pygame.display.update()

    # Esperar acción del jugador
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_reinicio.collidepoint(event.pos):
                    esperando = False  # vuelve a iniciar el juego
                elif boton_salir.collidepoint(event.pos):
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # tecla R para reiniciar
                    esperando = False
                elif event.key == pygame.K_ESCAPE:  # ESC para salir
                    pygame.quit()
                    quit()

def juego():
    # posición inicial de la serpiente
    serpiente = [[100, 100]]
    direccion = "DERECHA"
    comida = [random.randrange(0, constantes.ANCHO, constantes.BLOQUE), random.randrange(0, constantes.ALTO, constantes.BLOQUE)]
    reloj = pygame.time.Clock()
    puntaje = 0
    mostrar_inicio = True
    run = True
    dificil = 15

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mostrar_inicio:
                    if boton_jugar.collidepoint(event.pos):
                        mostrar_inicio = False
                    if boton_salir.collidepoint(event.pos):
                        run = False
                    if boton_dificultad.collidepoint(event.pos):
                        dificil = 30
                        mostrar_inicio = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direccion != "ABAJO":
                    direccion = "ARRIBA"
                elif event.key == pygame.K_DOWN and direccion != "ARRIBA":
                    direccion = "ABAJO"
                elif event.key == pygame.K_LEFT and direccion != "DERECHA":
                    direccion = "IZQUIERDA"
                elif event.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                    direccion = "DERECHA"

        if mostrar_inicio:
            pantalla_inicio()
        else:
            # Movimiento
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
                serpiente.pop(0)

            # Colisiones
            if (cabeza in serpiente[:-1] or
                cabeza[0] < 0 or cabeza[0] >= constantes.ANCHO or
                cabeza[1] < 0 or cabeza[1] >= constantes.ALTO):
                pantalla_game_over(puntaje)
                return juego()  # Reinicia desde 0

            # Dibujar
            ventana.fill(constantes.NEGRO)
            for x, y in serpiente:
                pygame.draw.rect(ventana, constantes.VERDE, (x, y, constantes.BLOQUE, constantes.BLOQUE))
            pygame.draw.rect(ventana, constantes.ROJO, (comida[0], comida[1], constantes.BLOQUE, constantes.BLOQUE))
            mostrar_mensaje(f"Puntos: {puntaje}", constantes.ROJO, (10, 10))
            pygame.display.flip()
            reloj.tick(dificil)

# Ejecutar
juego()
