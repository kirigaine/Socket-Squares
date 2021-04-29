"""
square.py
"""
from random import randint, shuffle
import pygame

class SquareFactory():
    """Create distinct squares with distinct names and ids for players"""
    def __init__(self):
        self.available_ids = [1,2,3,4,5,6,7,8]
        self.available_names = []
        self.prepareLists()
        
    def createSquare(self):
        temp_id = self.available_ids.pop()
        temp_name = self.available_names.pop()
        print(f"[SERVER] Giving away player_id {temp_id} and name {temp_name}")
        return MySquare(temp_id, temp_name)

    def prepareLists(self):
        with open("data/names.txt", "r") as f:
            while True:
                f_line = f.readline()
                if not f_line:
                    break
                self.available_names.append(f_line.strip())

        self.shuffleLists()

    def shuffleLists(self):
        shuffle(self.available_ids)
        shuffle(self.available_names)

    def printArray(self, given_array):
        for item in given_array:
            print(f"{item} ",end='')
        print(f"Total number of items: {len(given_array)}")
            

class MySquare():

    def __init__(self, p_id, p_name, screen=None):
        self.screen = screen

        self.name = p_name
        self.player_id = p_id
        self.size = (randint(50,100),randint(50,100))
        self.rect = pygame.Rect(randint(20,780), randint(20,580), self.size[0], self.size[1])
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def update(self):
        self.rect.center = (self.center_x, self.center_y)


    def draw(self):
        if self.screen:
            self.screen.fill(self.color,self.rect)

class PlayerSquare(MySquare):
    def __init__(self, MySquare, p_screen):
        super(PlayerSquare).__init__()
        self.name = MySquare.name
        self.player_id = MySquare.player_id
        self.size = MySquare.size
        self.rect = MySquare.rect
        self.center_x = MySquare.center_x
        self.center_y = MySquare.center_y
        self.color = MySquare.color
        self.screen = p_screen
        self.screen_rect = self.screen.get_rect()
        self.h_velocity = 0
        self.y_velocity = 0

    def update(self):
        """Update the player's square position based on movement flags"""
        # Restrict square from moving off screen
        # Move Right
        if self.h_velocity == 3:
            if self.rect.right < self.screen_rect.right:
                self.center_x += self.h_velocity
        # Move Left
        elif self.h_velocity == -3:
            if self.rect.left > self.screen_rect.left:
                self.center_x += self.h_velocity
        # Move Down
        if self.y_velocity == 3:
            if self.rect.bottom < self.screen_rect.bottom:
                self.center_y += self.y_velocity
        # Move Up
        elif self.y_velocity == -3:
            if self.rect.top > self.screen_rect.top:
                self.center_y += self.y_velocity

        self.rect.center = (self.center_x, self.center_y)
        