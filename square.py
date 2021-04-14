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
        self.available_names = []
        self.taken_names = []
        self.prepareNames()
        
    def createSquare(self):
        temp_id = self.available_ids.pop()
        temp_name = self.available_names.pop()
        print(f"Giving away player_id {temp_id} and player_name {temp_name}")
        self.taken_ids.append(temp_id)
        self.taken_names.append(temp_name)
        return Square(temp_id, temp_name)

    def prepareNames(self):
        with open("python\\testing\\socket_squares\\names.txt", "r") as f:
            while True:
                f_line = f.readline()
                if not f_line:
                    break
                self.available_names.append(f_line.strip())

        # self.printArray(self.available_names)
        shuffle(self.available_names)

    def printArray(self, given_array):
        for item in given_array:
            print(f"{item} ",end='')
        print(f"Total number of items: {len(given_array)}")
            

class Square():

    def __init__(self, p_id, p_name, screen=None):
        self.screen = screen

        self.name = p_name
        self.player_id = p_id
        self.position = (randint(20,780),randint(20,580))
        self.size = (randint(50,100),randint(50,100))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.center = float(self.rect.centerx)
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def draw(self):
        if self.screen:
            self.screen.fill(self.color,self.rect)

class PlayerSquare(Square):
    def __init__(self, p_id, p_name, screen=None):
        # Implement square with controls for movement
        pass