# Créé par TARS, le 18/04/2019 en Python 3.4

import pygame
from constantes import*



class SpriteSheet(object):
    # Classe qui extrait les sprites d'une feuille de sprite

    def __init__(self, file_name):


        # on charge la feuille de sprites
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        #Extrait le sprite voulue de la feuille de sprite suivant ses coordonnées et sa taille

        # Creation d'une image vierge
        image = pygame.Surface([width, height]).convert()

        # On copie le sprite extrait sur l'image vierge
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # couleur noir définie comme le 'transparent' du png
        image.set_colorkey(BLACK)

        # renvoi l'image - ou sprite -
        return image

class Player(pygame.sprite.Sprite):
    #Classe de controle du personnage

    # méthodes (fonctions de classe)
    def __init__(self):
        """ Constructor function """


        super().__init__()


        #Dimension des sprites du perso
        width = 32
        height = 32

        #tableaux des différentes frame de l'animation du perso selon droite - _l ou gauche - _ r
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Direction ou est tourné le joueur
        self.direction = "R"

        # Liste des sprite auxquelles il peut y avoir une collision
        self.level = None

        sprite_sheet = SpriteSheet(rep+"/spritebob/perso.png")
        # chargement de toutes les frames de l'animation
        image = sprite_sheet.get_image(0, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(26, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(51, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(79, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(105, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(133, 0, width, height)
        self.walking_frames_r.append(image)


        image = sprite_sheet.get_image(0, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(26, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(51, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(79, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(105, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(133, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)




        self.image = self.walking_frames_r[0]






        # référance au rect du perso
        self.rect = self.image.get_rect()

        # définition du vecteur vitesse
        self.change_x = 0
        self.change_y = 0

        # Liste des sprite auxquelles il peut y avoir une collision
        self.level = None


    def update(self):
        #Mise à jour du déplacement du perso

        # Gravité
        self.calc_grav()

        #Mouvement droite/gauche - roulements des frames selon le déplacement

        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Collision ?
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            #Mouvement à droite
            # le côté droit du perso touche le côté gauche du sprite bloc ?
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Le côté gauche du perso touche le côté droit du sprite bloc ?
                self.rect.left = block.rect.right

        #Mouvement haut/bas
        self.rect.y += self.change_y

        #Collision ?
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            #perso reste en dessus/en dessous du bloc si collision
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # arrêt du saut (collision du dessus en saut)
            self.change_y = 0

        #collision avec ennemi
        mob_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for mob in mob_hit_list:
            self.rect.x = self.startx + self.level.world_shift
            self.rect.y = self.starty

        if self.rect.y == 608:
            self.rect.x = self.startx + self.level.world_shift
            self.rect.y = self.starty

    def calc_grav(self):
        #Les effets de la gravité
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .48

        # Le person est il sur le sol ?
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        #Méthode du saut

        # On test si collision en tatonnant en bougeant de 2pix et si on peut pas -2pix, on revient avant la collision
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Si on peut sauter la vitesse est augmenté
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Contrôle du mouvement du joueur
    def go_left(self):
        #flèche de gauche
        self.change_x = -4
        self.direction = "L"


    def go_right(self):
       #flèche de droite
        self.change_x = 4
        self.direction = "R"

    def stop(self):
        #aucun évènement
        self.change_x = 0



class Mob(pygame.sprite.Sprite):
    #Classe de controle du personnage

    # méthodes (fonctions de classe)
    def __init__(self):
        """ Constructor function """


        super().__init__()


        #Dimension des sprites du perso
        width = 32
        height = 32

        #tableaux des différentes frame de l'animation du perso selon droite - _l ou gauche - _ r
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Direction ou est tourné le joueur
        self.direction = "R"

        # Liste des sprite auxquelles il peut y avoir une collision
        self.level = None




        sprite_sheet = SpriteSheet(rep+"/spritebob/spriteSheetBob.png")
        # chargement de toutes les frames de l'animation
        image = sprite_sheet.get_image(0, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(26, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(51, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(79, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(105, 0, width, height)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(133, 0, width, height)
        self.walking_frames_r.append(image)


        image = sprite_sheet.get_image(0, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(26, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(51, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(79, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(105, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(133, 0, width, height)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)



        self.image = self.walking_frames_r[0]






        # référance au rect du perso
        self.rect = self.image.get_rect()

        # définition du vecteur vitesse
        self.change_x = 1
        self.change_y = 0

        # Liste des sprite auxquelles il peut y avoir une collision
        self.level = None


    def update(self):
        #Mise à jour du déplacement du perso
        # Gravité
        self.calc_grav()

        #Mouvement droite/gauche - roulements des frames selon le déplacement

        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Collision x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            #Mouvement à droite
            # le côté droit du perso touche le côté gauche du sprite bloc ?
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Le côté gauche du perso touche le côté droit du sprite bloc ?
                self.rect.left = block.rect.right

        #Mouvement haut/bas
        self.rect.y += self.change_y

        #détection de bordures
        self.test=0
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if (block.rect.left<=self.rect.centerx<=block.rect.right and block.rect.top<=self.rect.bottom+2<=block.rect.bottom):
                self.test=1

        #changement de direction
        if self.test==0:
            self.change_x = -self.change_x
            if self.direction == "R":
                self.direction = "L"
            else:
                self.direction = "R"

        #Collision y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            #perso reste en dessus/en dessous du bloc si collision
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # arrêt du saut (collision du dessus en saut)
            self.change_y = 0

    def calc_grav(self):
        #Les effets de la gravité
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .48

        # Le person est il sur le sol ?
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height


    def stop(self):
        #aucun évènement
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    #Classes des platformes du jeu

    def __init__(self, sprite_sheet_data):
        #Constructeur de plaftorme
        super().__init__()

        sprite_sheet = SpriteSheet(rep+"/image/spriteSheet.png")
        # Données d'extraction du sprite de platforme dans la feuille de sprite
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class Portail(pygame.sprite.Sprite):
    #Classes des portails de fin de niveau

    def __init__(self):
        #Constructeur de portail
        super().__init__()

        sprite_sheet = SpriteSheet(rep+"/image/spriteSheet.png")
        # Données d'extraction du sprite de platforme dans la feuille de sprite
        self.image = sprite_sheet.get_image(70,206,32,32)

        self.rect = self.image.get_rect()





class Level(object):
    #Classe qui gère les niveaux, les niveaux étant des sous-classes, on aurait pu la nommer 'Monde' (qui gère donc les niveaux du monde)

    def __init__(self, player):
        #Gère la définition des collision selon la map

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.portail_list = pygame.sprite.Group()


        # image de fond
        self.background = None

        self.world_shift = 0
        self.level_limit = -200

        self.player = player


    def update(self):
        # Met à jour de tout ce qui existe dans le niveau
        self.platform_list.update()
        self.enemy_list.update()
        self.portail_list.update()

    def draw(self, screen):
        #Affiche tout les éléments du niveau

        # affiche le fond
        screen.blit(bg, (0,0))
        screen.blit(self.background,(self.world_shift // 3,0))
        # affiche tous les sprites des listes de sprites définit pour le niveau en question
        self.platform_list.draw(screen)

        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        #Fonction qui permet le scrolling de l'écran, mais ici utilisé pour le roulement des frames de l'anim. du perso

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for portail in self.portail_list:
            portail.rect.x += shift_x


class Level_01(Level):
    #Définition du niveau 1

    def __init__(self, player):
        #Création des plateformes

        Level.__init__(self, player)

        self.background = bg
        self.level_limit = -2560

        self.mobx = 512
        self.moby = 416

        self.playx = 32  #32
        self.playy = 480   #480

        self.portailx = 2944
        self.portaily = 544

        levelsheet=[
        [TERRE_HERBE,0,512,8,0],[TERRE, 0, 544,8,0],[TERRE, 0, 576,8,0],[TERRE, 0, 608,8,0],[PIERRE,64,352,1,0],
        [PIERRE,192,416,2,0],[PIERRE,192,256,5,0],[PIERRE,386,320,4,0],[PIERRE,386,352,4,0],[TERRE_HERBE,512,448,3,0],[TERRE,512,480,3,0],
        [TERRE,512,512,3,0],[TERRE,512,544,3,0],[TERRE,512,576,3,0],[TERRE,512,608,4,0],[TERRE_HERBE,608,576,1,0],
        [PIERRE,672,448,1,0],[PIERRE,806,448,1,0],[PIERRE,896,448,1,0],[PIERRE,992,448,1,0],
        [TERRE_HERBE, 1088,384,3,0],[PIERRE,1184,320,1,0],[TERRE,1152,416,1,0],[TERRE_HERBE,1184,416,1,0],[TERRE,1152,448,2,0],[TERRE,1152,480,2,0],[TERRE,1152,512,2,0],[TERRE,1152,544,2,0],
        [TERRE_HERBE,1120,608,6,0], [PIERRE,1088,288,2,0],[PIERRE,896,256,3,0],[PIERRE,832,160,1,0],[TERRE_HERBE,896,64,9,0],
        [TERRE,1152,96,1,0],[TERRE_HERBE,1184,96,1,0],[TERRE,1184,160,1,0],[TERRE_HERBE,1216,160,1,0],[TERRE,1184,192,2,0],[TERRE_HERBE,1248,192,2,0],[TERRE,1184,128,1,0],[PIERRE,1312,96,1,0],[PIERRE,1408,96,1,0],
        [BOIS,1504,128,5,0],[BOIS,1504,160,1,0],[BOIS,1504,192,1,0],[BOIS,1504,224,1,0],[BOIS,1504,256,1,0],[BRIQUE_BLEUE,1504,288,1,0],[BOIS,1408,320,14,0],[BOIS,1408,352,1,0],
        [BOIS,1408,384,1,0],[BRIQUE_BLEUE, 1408,416,1,0],[BRIQUE_BLEUE,1408,448,6,0],[TERRE,1472,480,4,0],[TERRE,1472,512,4,0],[TERRE,1472,544,4,0],[TERRE,1472,576,4,0],[TERRE,1472,608,5,0],
        [BOIS,1696,128,10,0],[BOIS,1920,320,6,0],[TERRE,1632,480,15,0],[TERRE,1632,512,15,0],[TERRE,1632,544,15,0],[TERRE,1632,608,15,0],[BRIQUE_BLEUE,1632,448,15,0],
        [BOIS,1984,160,1,0],[BOIS,1984,192,1,0],[BOIS,1984,224,1,0],[BOIS,1984,256,1,0],[BRIQUE_BLEUE,1984,288,1,0],[BOIS,2080,352,1,0],[BOIS,2080,384,1,0],[BRIQUE_BLEUE,2080,416,1,0],
        [TERRE_HERBE,2112,608,9,0],[TERRE_HERBE,2432,544,4,0],[TERRE_HERBE,2368,480,2,0],[TERRE_HERBE,2464,384,3,0],[TERRE_HERBE,2656,384,8,0],[TERRE_HERBE,3008,384,2,0],
        [TERRE,2848,416,2,0],[TERRE,2848,448,2,0],[TERRE,2848,480,2,0],[TERRE,2848,512,2,0],[TERRE,2848,544,2,0],[TERRE,2848,576,2,0],[TERRE,2848,608,7,0],
        [TERRE,3008,416,2,0],[TERRE,3008,448,2,0],[TERRE,3008,480,2,0],[TERRE,3008,512,2,0],[TERRE,3008,544,2,0],[TERRE,3008,576,2,0],
        [BRIQUE_BLEUE,2912,576,3,0],[BRIQUE_BLEUE,2912,544,1,0],[BRIQUE_BLEUE,2912,512,1,0],[BRIQUE_BLEUE,2976,544,1,0],[BRIQUE_BLEUE,2976,512,1,0],
        [BOIS,2848,288,7,0],[BOIS,3040,320,1,0],[BOIS,3040,352,1,0],[BOIS,1856,0,1,0],[BOIS,1856,32,2,0],[BOIS,1856,64,3,0],[BOIS,1856,96,4,0]
        ]


        level=[[TERRE_HERBE,0,800]]

        for tracing in levelsheet:
         i=0
         for i in range(0,tracing[3]):
          level = level+[[tracing[0],tracing[1]+i*32,tracing[2]+i*tracing[4]*32 ]]

        # Lis le tableau et ajoute les plateformes au groupe des plateformes
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

#Définition des platformes du niveau
class Level_02(Level):
    #Définition du niveau 1

    def __init__(self, player):
        #Création des plateformes

        Level.__init__(self, player)

        self.background = bg
        self.level_limit = -2560

        self.mobx = 400
        self.moby = 400

        self.playx = 300
        self.playy = 300

        self.portailx = 1376
        self.portaily = 384

        levelsheet=[[TERRE_HERBE,0,512,18,0],[TERRE,0,544,18,0],[TERRE,0,576,18,0],[TERRE,0,608,18,0],
        [TERRE_HERBE,704,512,14,0],[TERRE,704,544,14,0],[TERRE,704,576,14,0],[TERRE,704, 608,14,0],[PIERRE,1088,448,3,0],
        [PIERRE,1280,416,4,0], [PIERRE, 1504, 438,1,0], [TERRE_HERBE,1568,470,16,0],[TERRE,1568,502,16,0],[TERRE,1568,534,16,0],
        [TERRE_HERBE,2080,502,6,0],[TERRE,2080,534,6,0]]

        level=[[TERRE_HERBE,0,800]]

        for tracing in levelsheet:
         i=0
         for i in range(0,tracing[3]):
          level = level+[[tracing[0],tracing[1]+i*32,tracing[2]+i*tracing[4]*32 ]]

        # Lis le tableau et ajoute les plateformes au groupe des plateformes
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_03(Level):
    #Définition du niveau 1

    def __init__(self, player):
        #Création des plateformes

        Level.__init__(self, player)

        self.background = bg
        self.level_limit = -2560

        self.mobx = 300
        self.moby = 300

        self.playx = 32
        self.playy = 448

        self.portailx = 1500
        self.portaily = 480


        levelsheet=[[TERRE_HERBE,0,512,120,0],[TERRE, 0, 544,120,0],
        [TERRE, 0, 576,120,0],[TERRE, 0, 608,120,0],[TERRE_GRISE,0,448,5,0],[TERRE_GRISE,256,384,5,0],[TERRE_GRISE,512,384,3,0]]
        level=[[TERRE_HERBE,0,800]]

        for tracing in levelsheet:
         i=0
         for i in range(0,tracing[3]):
          level = level+[[tracing[0],tracing[1]+i*32,tracing[2]+i*tracing[4]*32 ]]

        # Lis le tableau et ajoute les plateformes au groupe des plateformes
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)