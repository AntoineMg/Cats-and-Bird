import pygame

class Foin(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.imgraw = pygame.image.load("assets/foin/foin.png")
        self.image = pygame.transform.scale(self.imgraw,(100,60))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 250
        self.liste_obstacles = pygame.sprite.Group()
    
    def spawn_level1(self):
        self.imgraw = pygame.image.load("assets/foin/foin.png")
        self.image = pygame.transform.scale(self.imgraw,(100,60))
        
        #Partie du code pas optimisée mais je n'ai plus assez de temps donc je fait comme ca mode galerien
        foin1 = pygame.sprite.Sprite()
        foin1.image = self.image
        foin1.rect = self.image.get_rect()
        foin1.rect.x = 150
        foin1.rect.y = 280
        self.liste_obstacles.add(foin1)

        foin2 = pygame.sprite.Sprite()
        foin2.image = self.image
        foin2.rect = self.image.get_rect()
        foin2.rect.x = 1400
        foin2.rect.y = 280
        self.liste_obstacles.add(foin2)

        foin3 = pygame.sprite.Sprite()
        foin3.image = self.image
        foin3.rect = self.image.get_rect()
        foin3.rect.x = 500
        foin3.rect.y = 280
        self.liste_obstacles.add(foin3)
