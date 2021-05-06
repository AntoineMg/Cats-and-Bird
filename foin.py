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
        foin1.rect.y = 250
        self.liste_obstacles.add(foin1)

        foin2 = pygame.sprite.Sprite()
        foin2.image = self.image
        foin2.rect = self.image.get_rect()
        foin2.rect.x = 1400
        foin2.rect.y = 250
        self.liste_obstacles.add(foin2)

        foin3 = pygame.sprite.Sprite()
        foin3.image = self.image
        foin3.rect = self.image.get_rect()
        foin3.rect.x = 500
        foin3.rect.y = 250
        self.liste_obstacles.add(foin3)
    

    def spawn_level2(self):
        
        self.imgraw = pygame.image.load("assets/foin/foin.png")
        self.image = pygame.transform.scale(self.imgraw,(100,60))
        
        #Partie du code pas optimisée mais je n'ai plus assez de temps donc je fait comme ca mode galerien
        foin1 = pygame.sprite.Sprite()
        foin1.image = self.image
        foin1.rect = self.image.get_rect()
        foin1.rect.x = 150
        foin1.rect.y = 250
        self.liste_obstacles.add(foin1)

        foin2 = pygame.sprite.Sprite()
        foin2.image = self.image
        foin2.rect = self.image.get_rect()
        foin2.rect.x = 400
        foin2.rect.y = 250
        self.liste_obstacles.add(foin2)

        foin3 = pygame.sprite.Sprite()
        foin3.image = self.image
        foin3.rect = self.image.get_rect()
        foin3.rect.x = 450
        foin3.rect.y = 190
        self.liste_obstacles.add(foin3)

        foin4 = pygame.sprite.Sprite()
        foin4.image = self.image
        foin4.rect = self.image.get_rect()
        foin4.rect.x = 500
        foin4.rect.y = 250
        self.liste_obstacles.add(foin4)

        foin5 = pygame.sprite.Sprite()
        foin5.image = self.image
        foin5.rect = self.image.get_rect()
        foin5.rect.x = 900
        foin5.rect.y = 250
        self.liste_obstacles.add(foin5)

        foin6 = pygame.sprite.Sprite()
        foin6.image = self.image
        foin6.rect = self.image.get_rect()
        foin6.rect.x = 1330
        foin6.rect.y = 250
        self.liste_obstacles.add(foin6)

        foin7 = pygame.sprite.Sprite()
        foin7.image = self.image
        foin7.rect = self.image.get_rect()
        foin7.rect.x = 1450
        foin7.rect.y = 250
        self.liste_obstacles.add(foin7)

        foin8 = pygame.sprite.Sprite()
        foin8.image = self.image
        foin8.rect = self.image.get_rect()
        foin8.rect.x = 2300
        foin8.rect.y = 250
        self.liste_obstacles.add(foin8)

    def spawn_level3(self):
        
        self.imgraw = pygame.image.load("assets/foin/foin.png")
        self.image = pygame.transform.scale(self.imgraw,(100,60))
        
        #Partie du code pas optimisée mais je n'ai plus assez de temps donc je fait comme ca mode galerien
        foin1 = pygame.sprite.Sprite()
        foin1.image = self.image
        foin1.rect = self.image.get_rect()
        foin1.rect.x = 150
        foin1.rect.y = 250
        self.liste_obstacles.add(foin1)

        foin2 = pygame.sprite.Sprite()
        foin2.image = self.image
        foin2.rect = self.image.get_rect()
        foin2.rect.x = 1400
        foin2.rect.y = 250
        self.liste_obstacles.add(foin2)

        foin3 = pygame.sprite.Sprite()
        foin3.image = self.image
        foin3.rect = self.image.get_rect()
        foin3.rect.x = 500
        foin3.rect.y = 250
        self.liste_obstacles.add(foin3)
        
        foin4 = pygame.sprite.Sprite()
        foin4.image = self.image
        foin4.rect = self.image.get_rect()
        foin4.rect.x = 1300
        foin4.rect.y = 250
        self.liste_obstacles.add(foin4)

        foin5 = pygame.sprite.Sprite()
        foin5.image = self.image
        foin5.rect = self.image.get_rect()
        foin5.rect.x = 1900
        foin5.rect.y = 250
        self.liste_obstacles.add(foin5)

        foin6 = pygame.sprite.Sprite()
        foin6.image = self.image
        foin6.rect = self.image.get_rect()
        foin6.rect.x = 2500
        foin6.rect.y = 250
        self.liste_obstacles.add(foin6)
