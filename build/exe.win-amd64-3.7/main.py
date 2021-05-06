import pygame, random, os, sys
from game import Game

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
imgbird1=pygame.image.load('assets/imgbird1.png')
imgbird1 = pygame.transform.smoothscale(imgbird1, (60, 50))
imgbird2=pygame.image.load('assets/imgbird2.png')
imgbird2 = pygame.transform.smoothscale(imgbird2, (50, 50))

#charger jeu
game = Game()

bird_finish = False
bird=1
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
        
        #afficher l'arriere plan
        window.blit(background,(game.bg_x,0))
        
        #afficher l'image du joueur
        window.blit(game.player.image, game.player.rect)

        game.game_clock.tick(game.fps)
        temps_partie+=1

        #afficher image oiseau
        game.oiseau_x+=7

        if temps_partie%14 == 0 :
            bird=1
        elif temps_partie%7 == 0 :
            bird=2

        if not bird_finish :
            if bird==1 :
                window.blit(imgbird1,(game.oiseau_x,80))
            elif bird==2 :
                window.blit(imgbird2,(game.oiseau_x,80))
            
        #verifier touche
        if game.pressed.get(pygame.K_RIGHT) :
            if game.player.rect.x >= 500 :
                game.move_decor_left()
            else :
                collision_left = False
                for obstacle in game.foin.liste_obstacles :
                    if game.check_collision_left(game.player,obstacle) :
                        collision_left = True
                        
                if not collision_left :
                    game.player.move_right()
            

        elif game.pressed.get(pygame.K_LEFT) :
            if game.player.rect.x <= 50 :
                game.move_decor_right()
            else :
                collision_right = False
                for obstacle in game.foin.liste_obstacles :
                    if game.check_collision_right(game.player,obstacle):
                        collision_right = True
                        
                if not collision_right :
                    game.player.move_left()     

        if game.pressed.get(pygame.K_UP) :
            game.player.isJumping = True
            game.player.jumpCount += 1

        game.obstacle_collision_down = False
        for obstacle in game.foin.liste_obstacles :
            if game.check_collision_down(game.player,obstacle):
                game.obstacle_collision_down = True

        if game.check_collision_down(game.player,game.ground) or game.obstacle_collision_down :
            game.player.resistance = (0, -10)
            game.ground_collision = True
            game.player.jumpCount = 0
        else :
            game.player.resistance = (0, 0)
        
        if game.ground_collision and game.player.isJumping :
            game.player.jumping()
        
        if game.bg_x <= -3000 :
            #fin de partie
            print("fin de la game")
            playing=False
            bird_finish=True
            if temps_partie < 428 :
                gagne = True
            else :
                gagne = False
            ecran_fin=True
        
        #print(temps_partie)

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

            if ecran_fin == True :
                #commande trouvée sur un forum
                os.execv(sys.executable, ['python'] + sys.argv)
                    