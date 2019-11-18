import pygame
from constantes import*
from classes import *
import webbrowser

#aide commande de parametrage du son
"""
<Sound>.play(loop = 10, time = 0, fadein = 0)
        .stop()
        .fadeout(ms)
        .set_volume(0.0 -> 1.0)
        .get_volume()
        .get_length()
"""

def main():
    playing = True
    while playing:
        #fréquence, format, buffer (mémoire tampon pour le son)
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Dead Kernel")
        screen.fill(BLACK)

        nbrson = 2
        countSound = 2

        screen.blit(bgmenu, (0, 0))
        screen.blit(button_levelmenu, (500,400))
        screen.blit(quit1, (75,400))
        screen.blit(button_son, (87, 350))
        pygame.display.flip()


        musiqueMenu = pygame.mixer.Sound(rep+"/sound/menu2.wav")
        sonClic = pygame.mixer.Sound(rep+"/sound/place4.ogg")
        musiqueLevel2 = pygame.mixer.Sound(rep+"/sound/fairy.wav")
        sonSaut = pygame.mixer.Sound(rep+"/sound/saut.wav")

        musiqueMenu.play()
        musiqueLevel2.stop()

        police = pygame.font.Font("Venice.ttf",25)
        police2 = pygame.font.Font("Venice.ttf",40)
        texte1 = police.render("About DeadKernel",1, YELLOW)
        texte2 = police2.render("Loading...", 1, YELLOW)

        mainmenu_trough_pause = False

        def Chargement():
            screen.fill(BLACK)
            screen.blit(bgmenu, (0, 0))
            screen.blit(texte2, (780,600))
            pygame.display.flip()

        def DispSon(nbr1):
            if nbr1 == 1:
                screen.blit(button_sonb, (87, 350))
            if nbr1 == 2:
                screen.blit(button_son, (87,350))


        def DispBgMenu():
            screen.blit(bgmenu, (0, 0))
            screen.blit(button_levelmenu, (500,400))
            screen.blit(quit1, (75,400))
            screen.blit(button_info, (145, 350))
            DispSon(nbrson)

            pygame.display.flip()
            running = True

        def DispMenuPause():
            screen.blit(bgPause, (75,50))
            pygame.display.flip()

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer3 = False
                else:
                    continuer3 = True

        def DispBgLevelMenu():
            screen.blit(bgmenu, (0, 0))
            screen.blit(button_level1, (130, 80))
            screen.blit(button_level2, (425, 80))
            screen.blit(button_level3, (130, 160 ))
            screen.blit(button_comingsoon, (425, 160))
            screen.blit(button_back, (210, 500))
            pygame.display.flip()
            running2 = True

        def PauseMenu():
                pause = True
                screen.blit(bg_pause, (200,155))
                pygame.display.flip()
                while pause:

                    event = pygame.event.wait()

                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pause = False
                        elif event.key == pygame.K_x:
                            done = True
                            finished = True
                            mainmenu_trough_pause = True
                            pause = False
                        elif event.key == pygame.K_a:
                            pygame.quit()
                        else:
                            pass

                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 2 : # on revient au menu
                            done = True
                            finished = True
                            mainmenu_trough_pause = True
                            pause = False
                        elif event.button == 1: #on revient au jeu
                            pause = False
                        elif event.button == 3: #on quitte le jeu
                            pygame.quit()
                        else:
                            pass





        running = True
        loading = False

    ###################### MENU ###################

        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    pygame.quit()

                if event.type == pygame.MOUSEMOTION :
                    posSouris = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:



                    if posSouris[0] > 500 and posSouris[0] < 893: #Level menu
                        if posSouris[1] > 400 and posSouris[1] < 484:
                            sonClic.play()
                            DispBgLevelMenu()


                            running2 = True

                            while running2:


                                for event in pygame.event.get():

                                    if event.type == pygame.QUIT:
                                        running2 = False
                                        done = True
                                        pygame.quit()

                                    if event.type == pygame.MOUSEMOTION:
                                        posSouris = pygame.mouse.get_pos()



                                    if event.type == pygame.MOUSEBUTTONDOWN:

                                        if posSouris[0] > 200 and posSouris[0] < 483: #bouton 1
                                            if posSouris[1] > 80 and posSouris[1] < 164:
                                                Chargement()

                                                sonClic.play()
                                                current_level_no = 0
                                                running = False
                                                running2 = False
                                                musiqueMenu.stop()
                                                loading = True





                                            elif posSouris[1] > 165 and posSouris[1] < 249 : #bouton 3
                                                Chargement()
                                                sonClic.play()
                                                current_level_no = 2
                                                running = False
                                                running2 = False
                                                musiqueMenu.stop()
                                                loading = True


                                            elif posSouris[0] > 210 and posSouris[0] < 354:
                                                if posSouris[1] > 500 and posSouris[1] < 551:
                                                    sonClic.play()
                                                    running = True
                                                    running2 = False
                                                    musiqueMenu.stop()





                                        elif posSouris[0] > 425 and posSouris[0] < 718: #bouton 2
                                            if posSouris[1] > 80 and posSouris[1] < 164:
                                                Chargement()
                                                sonClic.play()
                                                current_level_no = 1
                                                running = False
                                                running2 = False
                                                musiqueMenu.stop()
                                                loading = True


                                if loading:
                                    break

                                elif posSouris[0] > 200 and posSouris[0] < 483:
                                    if posSouris[1] > 80 and posSouris[1] < 164:
                                        screen.blit(bgmenu, (0, 0))
                                        screen.blit(button_level1, (130, 80))
                                        screen.blit(button_level1b, (130,70))
                                        screen.blit(button_level2, (425, 80))
                                        screen.blit(button_level3, (130, 160 ))
                                        screen.blit(button_back, (210, 500))
                                        screen.blit(button_comingsoon, (425, 160))

                                        pygame.display.flip()

                                    elif posSouris[1] > 165 and posSouris[1] < 249 :
                                        screen.blit(bgmenu, (0, 0))
                                        screen.blit(button_level1, (130, 80))
                                        screen.blit(button_level2, (425, 80))
                                        screen.blit(button_level3, (130, 160 ))
                                        screen.blit(button_level3b, (130, 150))
                                        screen.blit(button_back, (210, 500))
                                        screen.blit(button_comingsoon, (425, 160))

                                        pygame.display.flip()

                                    elif posSouris[0] > 210 and posSouris[0] < 354:
                                        if posSouris[1] > 500 and posSouris[1] < 551:
                                            screen.blit(bgmenu, (0, 0))
                                            screen.blit(button_level1, (130, 80))
                                            screen.blit(button_level2, (425, 80))
                                            screen.blit(button_level3, (130, 160 ))
                                            screen.blit(button_back, (210, 500))
                                            screen.blit(button_backb, (210, 490))
                                            screen.blit(button_comingsoon, (425, 160))

                                            pygame.display.flip()

                                    else:
                                        DispBgLevelMenu()

                                elif posSouris[0] > 425 and posSouris[0] < 718:
                                    if posSouris[1] > 80 and posSouris[1] < 164:
                                        screen.blit(bgmenu, (0, 0))
                                        screen.blit(button_level1, (130, 80))
                                        screen.blit(button_level2, (425, 80))
                                        screen.blit(button_level2b, (425, 70))
                                        screen.blit(button_level3, (130, 160 ))
                                        screen.blit(button_back, (210, 500))
                                        screen.blit(button_comingsoon, (425, 160))

                                        pygame.display.flip()

                                    else:
                                        DispBgLevelMenu()

                                else:
                                    DispBgLevelMenu()

                    if loading:
                        break
                    elif posSouris[0] > 75 and posSouris[0] < 468:  # quit game
                        if posSouris[1] > 400 and posSouris[1] < 484:
                            sonClic.play()
                            running = False
                            pygame.quit()

                        elif posSouris[0] > 145 and posSouris[0] < 198: # Info menu
                            if posSouris[1] > 350 and posSouris[1] < 399:
                                sonClic.play()

                                running_info = True

                                while running_info:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:

                                                pygame.quit()

                                            if event.type == pygame.MOUSEMOTION:
                                                posSouris = pygame.mouse.get_pos()

                                            if event.type == pygame.MOUSEBUTTONDOWN:

                                                if posSouris[0] > 210 and posSouris[0] < 354:
                                                    if posSouris[1] > 500 and posSouris[1] < 551:
                                                        sonClic.play()
                                                        running_info = False
                                                        running = True

                                                    else:
                                                        pass
                                                elif posSouris[0] > 365 and posSouris[0] < 630:
                                                    if posSouris[1] > 200 and posSouris[1] < 268:
                                                        sonClic.play()
                                                        webbrowser.open('https://kernelts2.wixsite.com/deadkernel')
                                                    else:
                                                        pass
                                                else:
                                                    pass





                                        if posSouris[0] > 210 and posSouris[0] < 354:
                                            if posSouris[1] > 500 and posSouris[1] < 551:
                                                screen.blit(bgmenu, (0, 0))
                                                screen.blit(texte1, (410,100))
                                                screen.blit(button_back, (210, 500))
                                                screen.blit(button_backb, (210, 490))
                                                screen.blit(button_link, (365,200))
                                                pygame.display.flip()

                                            else:
                                                screen.blit(bgmenu, (0, 0))
                                                screen.blit(texte1, (410,100))
                                                screen.blit(button_back, (210, 500))
                                                screen.blit(button_link, (365,200))
                                                pygame.display.flip()


                                        elif posSouris[0] > 365 and posSouris[0] < 630:
                                            if posSouris[1] > 200 and posSouris[1] < 268:
                                                screen.blit(bgmenu, (0, 0))
                                                screen.blit(texte1, (410,100))
                                                screen.blit(button_back, (210, 500))
                                                screen.blit(button_link, (365,200))
                                                screen.blit(button_linkb, (365,190))
                                                pygame.display.flip()

                                            else:
                                                screen.blit(bgmenu, (0, 0))
                                                screen.blit(texte1, (410,100))
                                                screen.blit(button_back, (210, 500))
                                                screen.blit(button_link, (365,200))
                                                pygame.display.flip()

                                        else:
                                            screen.blit(bgmenu, (0, 0))
                                            screen.blit(button_back, (210, 500))
                                            screen.blit(texte1, (410,100))
                                            screen.blit(button_link, (365,200))
                                            pygame.display.flip()




                            else:
                                pass

                    if loading:
                        break
                    else :
                        if posSouris[0] > 84 and posSouris[0] < 137:
                            if posSouris[1] > 350 and posSouris[1] < 400: # Bouton volume
                                sonClic.play()
                                if countSound % 2 == 0:
                                    musiqueMenu.set_volume(0.0)
                                    sonClic.set_volume(0.0)
                                    screen.blit(button_sonb, (87, 350))
                                    screen.blit(button_info, (145, 350))
                                    pygame.display.flip()
                                    nbrson = 1
                                    countSound = 3

                                elif countSound % 2 != 0:
                                    musiqueMenu.set_volume(1.0)
                                    sonClic.set_volume(1.0)
                                    screen.blit(button_son, (87, 350))
                                    screen.blit(button_info, (145, 350))
                                    pygame.display.flip()
                                    nbrson = 2
                                    countSound = 2

                                else:
                                    pass

            if loading:
                break
            elif posSouris[0] > 500 and posSouris[0] < 893:
                if posSouris[1] > 400 and posSouris[1] < 484:
                            screen.blit(bgmenu, (0, 0))
                            screen.blit(button_levelmenu, (500,400))
                            screen.blit(button_levelmenub, (500,390))
                            screen.blit(button_info, (145, 350))
                            screen.blit(quit1, (75,400))
                            DispSon(nbrson)
                            pygame.display.flip()
                else:
                        DispBgMenu()

            elif posSouris[0] > 75 and posSouris[0] < 468:
                if posSouris[1] > 400 and posSouris[1] < 484:
                            screen.blit(bgmenu, (0, 0))
                            screen.blit(quit1, (75,400))
                            screen.blit(quit2, (75,390))
                            screen.blit(button_levelmenu, (500,400))
                            screen.blit(button_info, (145, 350))
                            DispSon(nbrson)
                            pygame.display.flip()
                            running = True
                elif posSouris[0] > 145 and posSouris[0] < 198:
                    if posSouris[1] > 350 and posSouris[1] < 399:
                            screen.blit(bgmenu, (0, 0))
                            screen.blit(quit1, (75,400))
                            screen.blit(button_levelmenu, (500,400))
                            screen.blit(button_info, (145, 350))
                            screen.blit(button_infob, (145, 340))
                            DispSon(nbrson)
                            pygame.display.flip()
                            running = True
                else:
                    DispBgMenu()

        #On compte les joysticks
        nb_joysticks = pygame.joystick.get_count()
        #Et on en crée un s'il y a en au moins un
        if nb_joysticks ==1:

            mon_joystick = pygame.joystick.Joystick(0)
            mon_joystick.init() #Initialisation


        finished = False

        while not finished and mainmenu_trough_pause == False:

            # Créé le joueur et l'ennemi
            player = Player()
            mob=Mob()
            portail=Portail()


            # Créé les niveaux
            level_list = [Level_01(player),Level_02(player),Level_03(player)]

            # Initialiser le niveau
            current_level = level_list[current_level_no]

            active_sprite_list = pygame.sprite.Group()

            player.level = current_level
            mob.level = current_level

            player.rect.x = current_level.playx
            player.rect.y = current_level.playy
            player.startx = current_level.playx
            player.starty =  current_level.playy

            active_sprite_list.add(player)

            mob.rect.x = current_level.mobx
            mob.rect.y = current_level.moby

            portail.rect.x = current_level.portailx
            portail.rect.y = current_level.portaily

            current_level.enemy_list.add(mob)
            active_sprite_list.add(mob)

            current_level.portail_list.add(portail)
            active_sprite_list.add(portail)

            sonSaut.set_volume(1.0)

            # Boucle jusqu'à fermeture
            done = False
            if current_level_no == 0:
                    musiqueLevel2.play()
                    musiqueLevel2.set_volume(0.4)
            elif current_level_no == 1:
                musiqueLevel2.set_volume(0.4)
                pass
            elif current_level_no == 2:
                musiqueLevel2.set_volume(0.4)
                pass
            else:
                    pass




            # Horloge de rafraîchissement
            clock = pygame.time.Clock()

            ########## Boucle de jeu ##########
            while not done and mainmenu_trough_pause == False:



                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        musiqueLevel2.stop()

                    if event.type == pygame.JOYAXISMOTION:

                        if event.axis == 0:
                            if event.value < -0.1:
                                player.go_left()
                            elif event.value > 0.1:
                                player.go_right()
                            elif event.value > -0.1 and event.value < 0.1:
                                player.stop()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.go_left()
                        if event.key == pygame.K_RIGHT:
                            player.go_right()
                        if event.key == pygame.K_UP:
                            sonSaut.play()
                            player.jump()
                        if event.key == pygame.K_ESCAPE:
                            PauseMenu()
                    else:
                        pass

                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            sonSaut.play()
                            player.jump()
                        if event.button == 7:
                            PauseMenu()

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and player.change_x < 0:
                            player.stop()
                        if event.key == pygame.K_RIGHT and player.change_x > 0:
                            player.stop()



                #maj du perso
                active_sprite_list.update()

                # maj des sprites
                current_level.update()

                # If the player gets near the right side, shift the world left (-x)
                if (player.rect.right >= 500)and(current_level.world_shift>current_level.level_limit):
                    diff = player.rect.right - 500
                    player.rect.right = 500
                    current_level.shift_world(-diff)

                    # If the player gets near the left side, shift the world right (+x)
                if (player.rect.left <= 500)and(current_level.world_shift<0):
                    diff = 500 - player.rect.left
                    player.rect.left = 500
                    current_level.shift_world(diff)

                portail_hit_list = pygame.sprite.spritecollide(current_level.player, current_level.portail_list, False)
                for portail in portail_hit_list:
                    current_level_no += 1
                    if current_level_no > len(level_list)-1:
                        finished = True
                    done = True


                # potentielle utilité pour le scrolling mais pas dans notre cas
                if player.rect.right > SCREEN_WIDTH:
                    player.rect.right = SCREEN_WIDTH

                # potentielle utilité pour le scrolling mais pas dans notre cas
                if player.rect.left < 0:
                    player.rect.left = 0

                # affichage des objets
                current_level.draw(screen)
                active_sprite_list.draw(screen)

                # fps
                clock.tick(60)

                # maj de l'écran avec se qu'on à affiché
                pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()