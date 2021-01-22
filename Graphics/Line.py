import pygame

pygame.init()

class Line():
    def __init__(self, xpos1, xpos2, ypos1, ypos2):
        self.x1 = xpos1
        self.x2 = xpos2
        self.y1 = ypos1
        self.y2 = ypos2

    def Draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 5)