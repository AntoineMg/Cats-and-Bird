import pygame
from player import Player
from ground import Ground 


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
        self.game_clock = pygame.time.Clock()
        self.fps = 30
        self.rect = pygame.Rect(0, 0, 720, 480)
        self.nb_obstacles = 0
        self.liste_obstacles = pygame.sprite.Group()
    
    def gravity_game(self, vector1, vector2):
        self.player.rect.y += vector1[1]+vector2[1]

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
