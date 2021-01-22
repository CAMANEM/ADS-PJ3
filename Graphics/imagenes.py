import pygame, os


class Imagen(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, image, graph):
        super(Imagen, self).__init__()
        self.image = pygame.image.load(os.getcwd() + "\\Graphics\\images\\" + image).convert_alpha()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.left = False
        self.right = False
        self.id = graph

    def check_side(self):
        pos = pygame.mouse.get_pos()
        if self.rect.left < pos[0] < self.rect.left + 30:
            if self.left:
                return -1
            else:
                self.left = True
                return 0
        elif self.rect.left + 30 < pos[0] < self.rect.left + 60:
            if self.right:
                return -1
            else:
                self.right = True
                return 1

    def clear(self):
        self.left = False
        self.right = False
