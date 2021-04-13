"""
square.py
"""
from random import randint, shuffle
import pygame
from pygame.sprite import Sprite

class SquareFactory():

    def __init__(self):
        self.available_ids = [1,2,3,4,5,6,7,8]
        self.taken_ids = []
        shuffle(self.available_ids)
        print("array of available ids: ", end='')
        for thing in self.available_ids:
            print(f"{thing} , ",end='')
        

    def createSquare(self):
        temp_id = self.available_ids.pop()
        print(f"Giving away player_id {temp_id}")
        self.taken_ids.append(temp_id)
        return Square(temp_id)

class Square():

    def __init__(self, p_id, screen=None):
        self.screen = screen

        self.player_id = p_id
        self.position = (randint(20,780),randint(20,580))
        self.size = (randint(50,100),randint(50,100))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.center = float(self.rect.centerx)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.name = self.randomName()
     
    def randomName(self):
        with open("python\\testing\\socket_squares\\names.txt", "r") as f:
            temp_name = ""
            for x in range((randint(1,24))):
               temp_name = f.readline()
            return temp_name

    def draw(self):
        if self.screen:
            self.screen.fill(self.color,self.rect)