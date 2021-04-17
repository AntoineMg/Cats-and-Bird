import pygame

class Foin(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.imgraw = pygame.image.load("assets/foin/foin.png")
        self.image = pygame.transform.scale(self.imgraw,(100,60))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 250