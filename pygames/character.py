import pygame
import constants


class Character:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {"Wood" : 0}
    def draw(self, screen):
        pygame.draw.rect(screen, constants.BLUE, pygame.Rect(self.x, self.y, self.size, self.size))
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, constants.WIDHT - self.size))
        self.y = max(0, min(self.y, constants.HEIGHT - self.size))