import pygame, time
from pygame import time

#creation classe joueur
class Player(pygame.sprite.Sprite):
    jumpCount=10
    isjumping=False
    
    def __init__(self, game):
        super().__init__()
        self.game=game
        self.health=100
        self.frame=0
        self.jump_height=5
        self.maxhealth=100
        self.attack=10
        self.xspeed=2
        self.yspeed=10
        self.isJumping=False
        imagejoueurright=pygame.image.load('assets/player_right.png')
        imagejoueurleft=pygame.image.load('assets/player_left.png')
        self.image_right=pygame.transform.scale(imagejoueurright,(100,60))
        self.image_left=pygame.transform.scale(imagejoueurleft,(100,60))
        self.rect = self.image_right.get_rect()
        self.rect.x = 260
        self.rect.y = 290
        self.gravity = (0,10)
        
    def move_right(self):
        self.rect.x += self.xspeed
        
    def move_left(self):
        self.rect.x -= self.xspeed
        
    def jump(self):
        if self.jumpCount >= -10:
            self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else: # si jump fini
            self.jumpCount = 10
            self.isjumping = False
            # reset les variables
        
    def fall(self):
        self.rect.y+=10
