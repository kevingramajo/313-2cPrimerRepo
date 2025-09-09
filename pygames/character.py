import pygame
import constants
import os


class Character:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.inventory = {"Wood" : 0}
        image_path = os.path.join("C:\\Users\\Kevin\\OneDrive\\Escritorio\\Repositorio\\pygames\\assets\\images\\character\\character.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size=(constants.PLAYER, constants.PLAYER))
        self.size = self.image.get_width()


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, dx, dy, world):
        new_x = self.x + dx
        new_y = self.y + dy

        for tree in world.trees:
            if self.check_collision(new_x, new_y, tree):
                return
        
        self.x = new_x
        self.y = new_y
        self.x = max(0, min(self.x, constants.WIDHT - self.size))
        self.y = max(0, min(self.y, constants.HEIGHT - self.size))
    
    def check_collision(self, x, y, obj):
        return (x < obj.x + obj.size and x + self.size > obj.x and y < obj.y + obj.size and y + self.size > obj.y)
