import pygame
from game import Game
import random, os


pygame.init()

#création de la fenetre
pygame.display.set_caption("Cats & Mouses")
window = pygame.display.set_mode((720,480))

#charger jeu
game = Game()

running=True

#boucle principale
while running :
    
    #appliquer l'arriere plan
    window.blit(game.background,(game.background_x,0))
    
    #appliquer l'image du joueur
    window.blit(game.player.image, game.player.rect)

    game.game_clock.tick(game.fps)
    
    #verifier touche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 720 :
        game.player.image=game.player.image_right
        if game.player.rect.x < 400 and not game.check_collision(game.player, game.liste_obstacles):
            game.player.move_right() 
        elif game.player.rect.x >= 400 :
            game.decor_recul_right()  

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 :
        game.player.image=game.player.image_left
        if game.player.rect.x > 50 and not game.check_collision(game.player, game.liste_obstacles):
            game.player.move_left()
        elif game.player.rect.x <= 50 :
            game.decor_recul_left()
        
    if game.pressed.get(pygame.K_UP) :
        game.player.isJumping = True
        game.player.jumpCount += 1
    
    if game.ground.rect.colliderect(game.player.rect):
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
    
    
                