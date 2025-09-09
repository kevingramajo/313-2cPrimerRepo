import pygame
import sys
import constants
from character import Character
from world import World

#Inicializar Libreria Pygame
pygame.init()
#Ventana

screen= pygame.display.set_mode((constants.WIDHT, constants.HEIGHT))
pygame.display.set_caption("Simulador de Vida Salvaje")

def main():
    clock = pygame.time.Clock()
    world = World(constants.WIDHT, constants.HEIGHT)
    character = Character(constants.WIDHT// 2, constants.HEIGHT// 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move (-5,0, world)
        if keys[pygame.K_RIGHT]:
            character.move(5,0, world)
        if keys[pygame.K_UP]:
            character.move(0,-5, world)
        if keys[pygame.K_DOWN]:
            character.move(0,5, world)

        world.draw(screen)
        character.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()