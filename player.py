import pygame, time
from pygame import time

#creation classe joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.frame = 0
        self.xspeed = 10
        imagejoueurright = pygame.image.load('assets/player_right.png')
        imagejoueurleft = pygame.image.load('assets/player_left.png')
        self.image_right = pygame.transform.scale(imagejoueurright,(100,60))
        self.image_left = pygame.transform.scale(imagejoueurleft,(100,60))
        self.image = self.image_right
        self.rect = self.image_right.get_rect()
        self.rect.x = 260
        self.rect.y = 200
        self.jump = 0
        self.jump_up = 0
        self.jump_down = 5
        self.jumpCount = 0
        self.isJumping = False
        self.gravity = (0,10)
        self.resistance = (0,0)
        
    def move_right(self) :
        self.rect.x += self.xspeed
        self.image = self.image_right
        
    def move_left(self):
        self.rect.x -= self.xspeed
        self.image = self.image_left
        
    def jumping(self):
        if self.isJumping == True : 
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