"""
square.py
"""
from random import randint
import pygame
from pygame.sprite import Sprite

class Square(Sprite):

    def __init__(self, screen=None):
        self.screen = screen

        self.position = (randint(20,780),randint(20,580))
        self.size = (randint(50,100),randint(50,100))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.center = float(self.rect.centerx)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.name = self.randomName()
     
    def randomName(self):
        with open("names.txt", "r") as f:
            temp_name = ""
            for x in range((randint(1,24))):
               temp_name = f.readline()
            return temp_name

    def draw(self):
        if self.screen:
            self.screen.fill(self.color,self.rect)