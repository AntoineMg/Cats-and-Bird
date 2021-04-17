import pygame
import os
from player import Player 
from ground import Ground
from foin import Foin


#creation classe game
class Game:
    
    def __init__(self):
        #generer joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group
        self.all_players.add(self.player)
        self.ground = Ground(self)
        self.pressed = {}
        self.ground_collision = False
        self.game_clock = pygame.time.Clock()
        self.fps = 30
        self.rect = pygame.Rect(0, 0, 720, 480)
        self.nb_obstacles = 0
        self.liste_obstacles = pygame.sprite.Group()
        self.spawn_foin()

        

    def spawn_foin(self):
        foin = Foin()
        self.liste_obstacles.add(foin)
        self.nb_obstacles += 1
    
    def gravity_game(self, vector1, vector2):
        self.player.rect.y += vector1[1]+vector2[1]

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)