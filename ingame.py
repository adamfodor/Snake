import pygame
import random

class apple:
    def __init__(self, scr_w, scr_h, scr):
        self.scr = scr
        self.x = random.randint(50,620)
        self.y = random.randint(50,520)
        self.color = (255, 0, 0)
        self.width = 20
        self.height = 20

    def draw(self):
        self.food = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.scr, self.color, self.food)

class Square:

    def __init__(self, x, y, color, width,screen):
        self.x = x
        self.y = y
        self.screnn  = screen
        self.color = color
        self.width = width

    def draw_it(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.width), 0)

