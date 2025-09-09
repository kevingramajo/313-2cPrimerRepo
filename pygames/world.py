import pygame
import constants
from elements import Tree, SmallStone
import random
import os

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.trees = [Tree(random.randint(0, width-constants.TREE),random.randint(0, height-constants.TREE)) for _ in range(10)]
        self.small_stones = [SmallStone(random.randint(0, width-constants.SMALL_STONE),random.randint(0, height-constants.SMALL_STONE)) for _ in range(15)]


        grass_path = os.path.join("C:\\Users\\Kevin\\OneDrive\\Escritorio\\Repositorio\\pygames\\assets\\images\\objects\\grass.png")
        self.grass_image = pygame.image.load(grass_path).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constants.GRASS, constants.GRASS))

    def draw(self, screen):
        for y in range(0, self.height, constants.GRASS):
            for x in range(0, self.width, constants.GRASS):
                screen.blit(self.grass_image, (x, y))

        for tree in self.trees:
            tree.draw(screen)

        for stone in self.small_stones:
            stone.draw(screen)