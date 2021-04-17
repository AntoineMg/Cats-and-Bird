import pygame
from player import Player 


#creation classe game
class Game:
    
    def __init__(self):
        #generer joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group
        self.all_players.add(self.player)
        self.ground = Ground(self)
        self.background = pygame.image.load("assets/background.png")
        self.background_x = 0
        self.pressed = {}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
