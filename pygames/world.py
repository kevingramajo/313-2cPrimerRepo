import pygame
import constants

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self, screen):
        screen.fill(constants.GREEN)