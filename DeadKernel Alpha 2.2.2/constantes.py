# Créé par TARS, le 18/04/2019 en Python 3.4
import pygame

#répertoire
rep = "C:/Users/TARS/Desktop/DeadKernel Alpha 2.0.2"

#couleurs utiles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# dimension de l'écran
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
bg = pygame.image.load(rep+'/image/levels/test3level1.jpg')
bgmenu = pygame.image.load(rep+'/image/nomff2.jpg')


#bouton du menu principal
quit1 = pygame.image.load(rep+'/image/quit1.png')
quit2 = pygame.image.load(rep+'/image/quit2.png')
button_levelmenu = pygame.image.load(rep+'/image/boutons1.png') # 393 x 84
button_levelmenub = pygame.image.load(rep+'/image/boutons1b.png')
button_son = pygame.image.load(rep+'/image/boutonson.png')
button_sonb = pygame.image.load(rep+'/image/boutonsonb.png')
button_info = pygame.image.load(rep+ '/image/boutoninfo.png')
button_infob = pygame.image.load(rep+ '/image/boutoninfob.png')

#chargement image boutons menu des levels
button_level1 = pygame.image.load(rep+'/image/level1.png')
button_level1b = pygame.image.load(rep+'/image/level1b.png')
button_level2 = pygame.image.load(rep+'/image/level2.png')
button_level2b = pygame.image.load(rep+'/image/level2b.png')
button_level3 = pygame.image.load(rep+'/image/level3.png')
button_level3b = pygame.image.load(rep+'/image/level3b.png')
button_comingsoon = pygame.image.load(rep+'/image/comingsoon.png')
button_back = pygame.image.load(rep+'/image/back.png')
button_backb = pygame.image.load(rep+'/image/backb.png')

#menu info
button_link = pygame.image.load(rep+'/image/link.png')
button_linkb = pygame.image.load(rep+'/image/linkb.png')


#Menu pause
bg_pause = pygame.image.load(rep+'/image/MenuPause/pausemenu1.jpg')






TERRE_GRISE = (70, 70, 32,32)
TERRE_HERBE = (206, 2, 32, 32)
TERRE = (36, 70, 32, 32)
PIERRE = (70, 104, 32, 32)
BOIS = (70,172,32,32)
PIERRE_TAILLE = (70, 138, 32, 32)
PETIT_CARRE = (104,104,32,32)
BRIQUE_BLEUE = (104,70,32,32)
