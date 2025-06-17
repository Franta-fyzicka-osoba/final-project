import pygame
pygame.init()
import random

#Global stuff
window_width = 960
window_height = 540
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Šílená fantasy: Přežij knihovnu")

#TODO:scale, priblížení na postavu
#First Game
class Klobouk(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hat4.png")
        width_klb, height_klb = self.image.get_size()
        self.image = pygame.transform.scale(self.image,(width_klb*2,height_klb*2))
        self.rect = self.image.get_rect(center=(window_width/2,window_height/2))

def player_movement(position_x,position_y,maze_surface):
    keys = pygame.key.get_pressed()
    #TODO: neprocházet stěnami,udělej skrze kolizi, stun(2s)
    new_x = position_x
    new_y =position_y
    if keys[pygame.K_w]:
        new_y -= 5
    elif keys[pygame.K_s]:
        new_y += 5
    elif keys[pygame.K_d]:
        new_x += 5
    elif keys[pygame.K_a]:
        new_x -= 5
    
    if pygame.Color(pygame.Surface.get_at(maze_surface,(int(new_x + window_width//2),int(new_y + window_height//2)))).r == 0 and pygame.Color(pygame.Surface.get_at(maze_surface,(int(new_x + window_width//2),int(new_y + window_height//2)))).g == 0 and pygame.Color(pygame.Surface.get_at(maze_surface,(int(new_x + window_width//2),int(new_y + window_height//2)))).b == 0:
        return new_x,new_y
    else:
        return position_x, position_y
    #return new_x, new_y

class Drobek(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.surface.Surface((200,50))
        self.image.fill((255,255,0))
        self.rect =self.image.get_rect(center=pos)

#Second Game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Gamesa.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center=(window_width//2,4*window_height//5))
        self.speed = window_width//6
    
    def update(self):#movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.rect.x > 5*window_width//6:
                self.rect.x -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x += self.speed

class Worm(pygame.sprite.Sprite):
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__()
        self.image = pygame.image.load("Rapid_worm.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (25,100))
        self.rect = self.image.get_rect(center=(coordinate_x,coordinate_y))
        self.gravity = 5

    def update(self): #apply fall
        self.rect.y += self.gravity
        if self.rect.bottom == window_height:
            self.kill()

def is_collision():
    if pygame.sprite.spritecollide(player.sprite, worm_group, False):
        worm_group.empty()
        return False
    return True 

background_2 = pygame.image.load("Library_background.png")
background_2_fin = pygame.transform.scale(background_2, (window_width,window_height))
    
fallist = []
for i in range(5):
    x=(i+1)*window_width//6
    fallist.append(x)

player_pos_x = -245
player_pos_y = 1320

start_point_x = player_pos_x
start_point_y = player_pos_y

clock = pygame.time.Clock()

mazer_surface = pygame.image.load("new_try.png")
width_mz, height_mz = mazer_surface.get_size()  
mazer_surface = pygame.transform.scale(mazer_surface, (int(width_mz*1.5), int(height_mz*1.5)))  
#zvaž zvětšení a scale

#GROUPS
player = pygame.sprite.GroupSingle()
player.add(Klobouk())

player_2 = pygame.sprite.GroupSingle()
player_2.add(Player())

worm_group = pygame.sprite.Group()

Jenicek_a_Marenka = pygame.sprite.Group()
#vykřičník pohyb pronásledování

game_1_active =True
game_2_active = False
game_active = True
#Nepotřebuju score???
score_1 = 0
score_2 = 0

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active == False:
                    game_active = True
                    game_1_active = True
                    player_pos_x = start_point_x
                    player_pos_y = start_point_y
    
    if game_active:
        if game_1_active:
            score_1 += 1
            screen.fill((0,0,0))
            player_pos_x,player_pos_y = player_movement(player_pos_x,player_pos_y,mazer_surface)
            drobecek = Drobek((int(player_pos_x + window_width//2),int(player_pos_y + window_height//2)))
            Jenicek_a_Marenka.add(drobecek)

            screen.blit(mazer_surface,(-player_pos_x,-player_pos_y))
            player.draw(screen)
            Jenicek_a_Marenka.draw(screen)
            if score_1 % 300 == 0:
                game_1_active = False
                game_2_active = True
        if game_2_active:
            score_2 += 1

            if score_2 == 1200:
                game_2_active = False
                game_1_active = True

            screen.blit(background_2, (0,0))

            player_2.draw(screen)
            if score_2 %4 == 0:
                player_2.update()


            worm_group.update()
            worm_group.draw(screen)
            game_active = is_collision()
            if score_2 < 1200 and score_2 >=0:
                if score_2 % 60 == 0:
                    for i in range(5):
                        if random.randint(1,200)%2 == 1:
                            worm = Worm(fallist[i], window_height//6)
                            worm_group.add(worm)

            
    pygame.display.update()
    clock.tick(40)