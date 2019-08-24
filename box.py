import pygame
from constants import *


class Box:
    def __init__(self):
        self.width = W
        self.height = H
        self.options = [["Check", "Act1"],
                        ["Act2", "Act3"]]
        self.active_option = [0, 0]

    def choose_option(self, key):
        if key == pygame.K_RIGHT:
            if self.active_option[1] < 1:
                self.active_option[1] += 1

        elif key == pygame.K_LEFT:
            if self.active_option[1] > 0:
                self.active_option[1] -= 1

        elif key == pygame.K_UP:
            if self.active_option[0] > 0:
                self.active_option[0] -= 1

        elif key == pygame.K_DOWN:
            if self.active_option[0] < 1:
                self.active_option[0] += 1
        print(self.options[self.active_option[0]][self.active_option[0]])

    def draw(self):
        pass


