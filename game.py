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
        self.bg_x = 0

    def move_decor_left(self):
        self.bg_x -= self.player.xspeed
        for element in self.liste_obstacles :
            element.rect.x -= self.player.xspeed
    
    def move_decor_right(self):
        self.bg_x += self.player.xspeed
        for element in self.liste_obstacles :
            element.rect.x += self.player.xspeed

    def spawn_foin(self):
        foin = Foin()
        self.liste_obstacles.add(foin)
        self.nb_obstacles += 1
    
    def gravity_game(self, vector1, vector2):
        self.player.rect.y += vector1[1]+vector2[1]

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def check_collision_down(self, player, objet):
        if player.rect.bottom > objet.rect.top :
            if player.rect.right-20 > objet.rect.left and player.rect.left+20 < objet.rect.right :
                return True
            else :
                return False
        else :
            return False
    #Test des collisions gauche droite, ajout de marges pour eviter pb de blocage

    def check_collision_left(self, player, objet):
        #debug : 
        #print("pb=",player.rect.bottom,"     ot=", objet.rect.top,"      pr=",player.rect.right,"      ol=",objet.rect.left)
        if player.rect.bottom-15 > objet.rect.top :
            if player.rect.right+10 > objet.rect.left and player.rect.left+30 < objet.rect.right :
                return True
            else :
                return False
        else :
            return False
    
    def check_collision_right(self, player, objet):
        #debug :
        #print("pb=",player.rect.bottom,"     ot=", objet.rect.top,"      pr=",player.rect.right,"      pl=",player.rect.left,"       or=",objet.rect.right,"       ol=",objet.rect.left)
        if player.rect.bottom-15 > objet.rect.top :
            if player.rect.left-10 < objet.rect.right and player.rect.right-30 > objet.rect.left :
                #print("collision right")
                return True
            else :
                return False
        else :
            return False
        
        