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
        hat_1 = pygame.image.load("hat1.png")
        width_klb_1, height_klb_1 = hat_1.get_size()
        hat_1 = pygame.transform.scale(hat_1,(width_klb_1*2,height_klb_1*2))
        hat_2 = pygame.image.load("hat2.png")
        width_klb_2, height_klb_2 = hat_2.get_size()
        hat_2 = pygame.transform.scale(hat_2,(width_klb_2*2,height_klb_2*2))
        hat_3 = pygame.image.load("hat3.png")
        width_klb_3, height_klb_3 = hat_3.get_size()
        hat_3 = pygame.transform.scale(hat_3,(width_klb_3*2,height_klb_3*2))
        hat_4 = pygame.image.load("hat4.png")
        width_klb_4, height_klb_4 = hat_4.get_size()
        hat_4 = pygame.transform.scale(hat_4,(width_klb_4*2,height_klb_4*2))
        self.animaton = [hat_1,hat_2,hat_3,hat_4]
        self.anim_index = 0
        self.image = self.animaton[self.anim_index]
        self.rect = self.image.get_rect(center=(window_width/2,window_height/2))
        self.face_R = True
    def animation(self):
        self.anim_index += 0.1
        if self.anim_index >= 4:
            self.anim_index = 0
        self.image = self.animaton[int(self.anim_index)]
    def update(self):
        self.animation()

def player_movement(position_x,position_y,maze_surface, self):
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
        if self.face_R == False:
            for i in range(4):
                self.animaton[i] = pygame.transform.flip(self.animaton[i], True, False)
            self.face_R = True
    elif keys[pygame.K_a]:
        new_x -= 5
        if self.face_R == True:
            for i in range(4):
                self.animaton[i] = pygame.transform.flip(self.animaton[i], True, False)
            self.face_R = False
    
    if pygame.Color(pygame.Surface.get_at(maze_surface,(int(new_x + window_width//2),int(new_y + window_height//2)))).a == 0:
        print(new_x,new_y)
        return new_x, new_y
    else:
        return position_x, position_y

#Second Game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Gamesa.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center=(window_width//2,4*window_height//5))
        self.speed = window_width//6
        self.kouka_P = True
    
    def update(self):#movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.kouka_P == False:
                self.image = pygame.transform.flip(self.image,True,False)
                self.kouka_P = True
            if self.rect.x > 5*window_width//6:
                self.rect.x -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.kouka_P == True:
                self.image = pygame.transform.flip(self.image,True,False)
                self.kouka_P = False
            if self.rect.x < 0:
                self.rect.x += self.speed

class Worm(pygame.sprite.Sprite):
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__()
        self.image = pygame.image.load("Rapid_worm.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (25,100))
        self.rect = self.image.get_rect(center=(coordinate_x,coordinate_y))
        self.gravity = 7

    def update(self): #apply fall
        self.rect.y += self.gravity
        if self.rect.bottom == window_height:
            self.kill()

class Cil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((70,70))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=(end_point_x,end_point_y))

def is_collision():
    if cil.sprite and pygame.sprite.spritecollide(player_2.sprite, worm_group, False):
        worm_group.empty()
        return False
    return True 

def is_win():
    if pygame.sprite.spritecollide(cil.sprite, player,False):
        return True
    return False

#Úvodní představení
uvod_1 = pygame.image.load("uvod_1.png")
uvod_1 = pygame.transform.scale(uvod_1, (window_width, window_height))
uvod_2 = pygame.image.load("uvod_2.png")
uvod_2 = pygame.transform.scale(uvod_2, (window_width, window_height))
uvod_3 = pygame.image.load("uvod_3.png")
uvod_3 = pygame.transform.scale(uvod_3, (window_width, window_height))
uvod_4 = pygame.image.load("uvod_4.png")
uvod_4 = pygame.transform.scale(uvod_4, (window_width, window_height))
ahoj_1 = pygame.image.load("Aho_8.png")
ahoj_1 = pygame.transform.scale(ahoj_1, (window_width, window_height))
ahoj_2 = pygame.image.load("Aho_7.png")
ahoj_2 = pygame.transform.scale(ahoj_2, (window_width, window_height))
ahoj_3 = pygame.image.load("Aho_6.png")
ahoj_3 = pygame.transform.scale(ahoj_3, (window_width, window_height))
ahoj_4 = pygame.image.load("Aho_5.png")
ahoj_4 = pygame.transform.scale(ahoj_4, (window_width, window_height))
ahoj_5 = pygame.image.load("Aho_4.png")
ahoj_5 = pygame.transform.scale(ahoj_5, (window_width, window_height))
ahoj_6 = pygame.image.load("Aho_3.png")
ahoj_6 = pygame.transform.scale(ahoj_6, (window_width, window_height))
ahoj_7 = pygame.image.load("Aho_2.png")
ahoj_7 = pygame.transform.scale(ahoj_7, (window_width, window_height))
ahoj_8 = pygame.image.load("Aho.png")
ahoj_8 = pygame.transform.scale(ahoj_8, (window_width, window_height))
#Win and Death
win_1 = pygame.image.load("Win_1.png")
win_1 = pygame.transform.scale(win_1, (window_width, window_height))
win_2 = pygame.image.load("Win_1.png")
win_2 = pygame.transform.scale(win_2, (window_width, window_height))
fin_1 = pygame.image.load("Fin_1.png")
fin_1 = pygame.transform.scale(fin_1, (window_width, window_height))
fin_2 = pygame.image.load("Fin_2.png")
fin_2 = pygame.transform.scale(fin_2, (window_width, window_height))
fin_3 = pygame.image.load("Fin_3.png")
fin_3 = pygame.transform.scale(fin_3, (window_width, window_height))
main_maze = pygame.image.load("overtop.png")

background_2 = pygame.image.load("Library_background.png")
background_2_fin = pygame.transform.scale(background_2, (window_width,window_height))
background_1 = background_2

end_point_y = -205
end_point_x = 1980

fallist = []
for i in range(5):
    x=(i+1)*window_width//6
    fallist.append(x)

player_pos_x = -245
player_pos_y = 1320

start_point_x = player_pos_x
start_point_y = player_pos_y

clock = pygame.time.Clock()

mazer_surface = main_maze
width_mz, height_mz = mazer_surface.get_size()  
mazer_surface = pygame.transform.scale(mazer_surface, (int(width_mz*1.5), int(height_mz*1.5)))  
background_1 = pygame.transform.scale(background_1,(int(width_mz*1.5), int(height_mz*1.5)))
#zvaž zvětšení a scale

#GROUPS
player = pygame.sprite.GroupSingle()
player.add(Klobouk())

player_2 = pygame.sprite.GroupSingle()
player_2.add(Player())

worm_group = pygame.sprite.Group()

cil = pygame.sprite.GroupSingle()
cil.add(Cil())
#vykřičník pohyb pronásledování

game_1_active =False
game_2_active = False
game_active = True
tutorial = True
current_status = True
#Nepotřebuju score???
score_1 = 0
score_2 = 0
tutorial_timer = 0

tutorial_clock = pygame.time.Clock()
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
                    game_2_active = False
                    current_status = True
                    tutorial = False
                    player_pos_x = start_point_x
                    player_pos_y = start_point_y

    if game_active:
        if tutorial:
            tutorial_timer +=1
            if tutorial_timer < 10 and tutorial_timer >= 0:
                screen.blit(ahoj_1, (0,0))
            elif tutorial_timer < 20 and tutorial_timer >= 10:
                screen.blit(ahoj_2, (0,0))
            elif tutorial_timer < 30 and tutorial_timer >= 20:
                screen.blit(ahoj_3, (0,0))
            elif tutorial_timer < 40 and tutorial_timer >= 30:
                screen.blit(ahoj_4, (0,0))
            elif tutorial_timer < 50 and tutorial_timer >= 40:
                screen.blit(ahoj_5, (0,0))
            elif tutorial_timer < 60 and tutorial_timer >= 50:
                screen.blit(ahoj_6, (0,0))
            elif tutorial_timer < 70 and tutorial_timer >= 60:
                screen.blit(ahoj_7, (0,0))
            elif tutorial_timer < 80 and tutorial_timer >= 70:
                screen.blit(ahoj_8, (0,0))
            elif tutorial_timer < 140 and tutorial_timer >= 80:
                screen.blit(uvod_1, (0,0))
            elif tutorial_timer < 200 and tutorial_timer >= 140:
                screen.blit(uvod_2, (0,0))
            elif tutorial_timer < 260 and tutorial_timer >= 200:
                screen.blit(uvod_3, (0,0))
            elif tutorial_timer < 320 and tutorial_timer >= 260:
                screen.blit(uvod_4, (0,0))
            elif tutorial_timer == 320:
                game_1_active = True
                tutorial = False
        if game_1_active:
            score_1 += 1
            screen.fill((0,0,0))
            player_pos_x,player_pos_y = player_movement(player_pos_x,player_pos_y,mazer_surface,player.sprite)
            screen.blit(background_1, (-player_pos_x,-player_pos_y))
            screen.blit(mazer_surface,(-player_pos_x,-player_pos_y))
            cil.sprite.rect.center = (-player_pos_x+end_point_x+window_width//2,-player_pos_y+end_point_y+window_height//2)
            cil.draw(screen)
            player.draw(screen)
            player.update()
            if score_1 % 1200 == 0:
                game_1_active = False
                game_2_active = True
            
            super_1 = is_win()
            if super_1 == True:
                screen.fill((0,0,255))
                game_active = False

        if game_2_active:
            score_2 += 1
            if current_status == True:
                if score_2 == 400:
                    game_2_active = False
                    game_1_active = True

                screen.blit(background_2, (0,0))

                player_2.draw(screen)
                if score_2 %4 == 0:
                    player_2.update()
                current_score = score_2
                worm_group.update()
                worm_group.draw(screen)
                current_status = is_collision()
            if current_status == False:
                if (score_2 - current_score) >= 0 and (score_2 - current_score) < 80:
                    screen.blit(fin_1,(0,0))
                elif (score_2 - current_score) >= 80 and (score_2 - current_score) < 160:
                    screen.blit(fin_2,(0,0))
                elif (score_2 - current_score) >= 160 and (score_2 - current_score) < 240:
                    screen.blit(fin_3,(0,0))
                elif (score_2 - current_score) == 240:
                    game_active = False
            if score_2 < 1200 and score_2 >=0:
                if score_2 % 80 == 0:
                    for i in range(5):
                        if random.randint(1,200)%2 == 1:
                            worm = Worm(fallist[i], window_height//6)
                            worm_group.add(worm)

    print(game_active,game_1_active,game_2_active)
    pygame.display.update()
    clock.tick(40)