import pygame, time
from pygame import time

"""
ij1=pygame.image.load("assets/ij1.png")
ij2=pygame.image.load("assets/ij2.png")
ij3=pygame.image.load("assets/ij3.png")
ij4=pygame.image.load("assets/ij4.png")
ij5=pygame.image.load("assets/ij5.png")
ij6=pygame.image.load("assets/ij6.png")
ij7=pygame.image.load("assets/ij7.png")
ij8=pygame.image.load("assets/ij8.png")
ij9=pygame.image.load("assets/ij9.png")
"""


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
        imagejoueur=pygame.image.load('assets/player.png')
        self.image=pygame.transform.scale(imagejoueur,(100,60))
        self.rect = self.image.get_rect()
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
