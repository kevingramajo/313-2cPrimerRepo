import pygame
import sys
import constants

#Inicializar Libreria Pygame
pygame.init()
clock = pygame.time.Clock()

#Ventana
ventana= pygame.display.set_mode((constants.WIDHT, constants.HEIGHT))
pygame.display.set_caption("Simulador de Vida Salvaje")

clock.tick(60)  # limits FPS to 60

pygame.quit()