import pygame
import constants

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.wood = 5
    
    def draw(self, screen):
        pygame.draw.rect(screen, constants.BROWN, pygame.Rect(self.x, self.y, self.size, self.size))