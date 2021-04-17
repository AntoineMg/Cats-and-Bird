import pygame

#classe sol
class Ground(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.rect = pygame.Rect(0,300,1000,150)
        #crée un rectangle de sol !attention le 3e parametre est la largeur de la fenetre
    
    def displayGround(self, surface):
        rectangle_sol = pygame.draw.rect(surface, (0,255,0), self.rect, 2)