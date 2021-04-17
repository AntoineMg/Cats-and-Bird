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
    
    def __init__(self, game):
        super().__init__()
        self.game=game
        self.frame=0
        self.xspeed=10
        imagejoueur=pygame.image.load('assets/player.png')
        self.image=pygame.transform.scale(imagejoueur,(100,60))
        self.rect = self.image.get_rect()
        self.rect.x = 260
        self.rect.y = 30
        self.jump = 0
        self.jump_up = 0
        self.jump_down = 5
        self.jumpCount = 0
        self.isJumping = False
        self.gravity = (0,10)
        self.resistance = (0,0)

        
    def move_right(self):
        self.rect.x += self.xspeed
        
    def move_left(self):
        self.rect.x -= self.xspeed
        
    def jumping(self):
        if self.isJumping is True : 
            if self.jump_up >= 10:
                self.jump_down -= 1
                self.jump = self.jump_down
            
            else :
                self.jump_up += 1
                self.jump = self.jump_up
                self.jumpCount+=1
            
            if self.jump_down < 0 :
                self.jump_up = 0
                self.jump_down = 5
                self.isJumping = False
                self.jumpCount = 0
          
        self.rect.y = self.rect.y - (5*(self.jump/2))