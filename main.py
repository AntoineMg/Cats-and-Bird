import pygame
from game import Game
import random, os


pygame.init()

#création de la fenetre
pygame.display.set_caption("Cats & Mouses")
window = pygame.display.set_mode((720,480))

#charger arriere plan
background=pygame.image.load('assets/background.png')

#charger jeu
game = Game()

running=True

collision_left = False

#boucle principale
while running :
    
    #appliquer l'arriere plan
    window.blit(background,(game.bg_x,0))
    
    #appliquer l'image du joueur
    window.blit(game.player.image, game.player.rect)

    game.game_clock.tick(game.fps)
    
    #verifier touche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 720 :
        if game.player.rect.x >= 500 :
            game.move_decor_left()
        else :
            for obstacle in game.liste_obstacles :
                if game.check_collision_left(game.player,obstacle) :
                    collision_left = True
                else :
                    collision_left = False
            if collision_left == False :
                game.player.move_right()
        

    elif game.pressed.get(pygame.K_LEFT) :
        if game.player.rect.x <= 50 :
            game.move_decor_right()
        else :
            for obstacle in game.liste_obstacles :
                if game.check_collision_right(game.player,obstacle):
                    collision_right = True
                else :
                    collision_right = False
            if collision_right == False :
                game.player.move_left()     

    if game.pressed.get(pygame.K_UP) :
        game.player.isJumping = True
        game.player.jumpCount += 1

    for obstacle in game.liste_obstacles :
        if game.check_collision_down(game.player,obstacle):
            game.obstacle_collision_down = True
        else :
            game.obstacle_collision_down = False

    if game.check_collision_down(game.player,game.ground) or game.obstacle_collision_down :
        game.player.resistance = (0, -10)
        game.ground_collision = True
        game.player.jumpCount = 0
    else :
        game.player.resistance = (0, 0)
    
    if game.ground_collision and game.player.isJumping :
        game.player.jumping()

    #Obstacles
    if game.nb_obstacles < 2 :
        if random.randint(0,5)==1 :
            game.spawn_foin()
    
    game.liste_obstacles.draw(window)

    #appliquer gravité
    game.gravity_game(game.player.gravity, game.player.resistance)


    #maj de l'écran
    pygame.display.flip()
    
    #boucle evenements
    for event in pygame.event.get():
        #evenement quitter
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            print("fermeture du jeu")
            
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
            
        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False
    
    
                