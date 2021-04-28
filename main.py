import pygame
from game import Game
import random, os

pygame.init()

#création de la fenetre
pygame.display.set_caption("Cats & Mouses")
window = pygame.display.set_mode((720,480))

#importer images
imgmenu = pygame.image.load('assets/imgmenu.png')
bouton_niveau1 = pygame.image.load('assets/bouton_level1.png')
bouton_niveau2 = pygame.image.load('assets/bouton_level2.png')
bouton_niveau3 = pygame.image.load('assets/bouton_level3.png')
imgwin = pygame.image.load('assets/imgwin.png')
imglose = pygame.image.load('assets/imglose.png')
background=pygame.image.load('assets/background.png')

#charger jeu
game = Game()

playing = False
menu_affiche = True
ecran_fin = False

temps_partie=0

while True :
    if menu_affiche == True :
        window.blit(imgmenu,(0,0))
        window.blit(bouton_niveau1,(90,300))
        window.blit(bouton_niveau2,(290,300))
        window.blit(bouton_niveau3,(490,300))
        pygame.display.flip()

    #boucle jeu
    if playing==True :
        
        #appliquer l'arriere plan
        window.blit(background,(game.bg_x,0))
        
        #appliquer l'image du joueur
        window.blit(game.player.image, game.player.rect)

        game.game_clock.tick(game.fps)
        temps_partie+=1
        
        #verifier touche
        if game.pressed.get(pygame.K_RIGHT) :
            if game.player.rect.x >= 500 :
                game.move_decor_left()
            else :
                for obstacle in game.foin.liste_obstacles :
                    if game.check_collision_left(game.player,obstacle) :
                        collision_left = True
                    else :
                        collision_left = False
                if not collision_left :
                    game.player.move_right()
            

        elif game.pressed.get(pygame.K_LEFT) :
            if game.player.rect.x <= 50 :
                game.move_decor_right()
            else :
                for obstacle in game.foin.liste_obstacles :
                    if game.check_collision_right(game.player,obstacle):
                        collision_right = True
                    else :
                        collision_right = False
                if not collision_right :
                    game.player.move_left()     

        if game.pressed.get(pygame.K_UP) :
            game.player.isJumping = True
            game.player.jumpCount += 1

        for obstacle in game.foin.liste_obstacles :
            if game.check_collision_down(game.player,obstacle):
                game.obstacle_collision_down = True
            else :
                game.obstacle_collision_down = False

        if game.check_collision_down(game.player,game.ground) or game.check_collision_down :
            game.player.resistance = (0, -10)
            game.ground_collision = True
            game.player.jumpCount = 0
        else :
            game.player.resistance = (0, 0)
        
        if game.ground_collision and game.player.isJumping :
            game.player.jumping()
        
        if game.bg_x <= -1500 :
            #fin de partie
            print("fin de la game")
            playing=False
            if temps_partie < 1000 :
                gagne = True
            else :
                gagne = False
            ecran_fin=True
        
        print(temps_partie)

        game.foin.liste_obstacles.draw(window)
            
        #appliquer gravité
        game.gravity_game(game.player.gravity, game.player.resistance)


        #maj de l'écran
        pygame.display.flip()
        
        

    if ecran_fin==True :
        if gagne == True :
            window.blit(imgwin,(0,0))
        else :
            window.blit(imglose,(0,0))
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
        
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if menu_affiche == True :
                mouse=pygame.mouse.get_pos()
                if mouse[1]<400 and mouse[1]>300 :
                    if mouse[0]>90 and mouse[0]<240 :
                        menu_affiche = False
                        playing=True
                        game.foin.spawn_level1()
                        
                    elif mouse[0]>290 and mouse[0]<440 :
                        menu_affiche = False
                        playing=True
                        game.foin.spawn_level2()

                    elif mouse[0]>490 and mouse[0]<640 :
                        menu_affiche = False
                        playing=True
                        game.foin.spawn_level3()
                    