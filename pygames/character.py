import pygame
import constants


class Character:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {}
    def draw(self, screen):
        pygame.draw.rect(screen, constants.BLUE, pygame.Rect(self.x, self.y, self.size, self.size))
    def move(self, dx, dy):
        self.x += dx
        self.y += dy