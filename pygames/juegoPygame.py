import pygame
import sys
import constants

#Inicializar Libreria Pygame
pygame.init()

#Ventana
ventana= pygame.display.set_mode((constants.WIDHT, constants.HEIGHT))
pygame.display.set_caption("Simulador de Vida Salvaje")