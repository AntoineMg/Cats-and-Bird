import pygame

#classe sol
class Ground(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.rect = pygame.Rect(0,300,720,200)
        #crée un rectangle de sol !attention le 3e parametre est la largeur de la fenetre