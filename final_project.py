import pygame
pygame.init()

#TODO:scale, priblížení na postavu

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
    #I have used AI to debug and remove the problem of world and screen coordinate,
    maze_x = int(new_x-maze_surface.get_width()/2)
    maze_y = int(new_y - maze_surface.get_height()/2)
    
    if pygame.Color(pygame.Surface.get_at(maze_surface,(maze_x,maze_y))).a <= 10:
        return new_x,new_y
    else:
        return position_x, position_y
    
window_width = 960
window_height = 540
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Šílená fantasy: Přežij knihovnu")

player_pos_x = 200
player_pos_y = 200

start_point_x = player_pos_x
start_point_y = player_pos_y

clock = pygame.time.Clock()

background_surface = pygame.image.load("undertop.png")
mazer_surface = pygame.image.load("overtop.png")
width_mz, height_mz = mazer_surface.get_size()  
mazer_surface = pygame.transform.scale(mazer_surface, (int(width_mz*1.5), int(height_mz*1.5))) 
width_bc, height_bc = background_surface.get_size() 
background_surface = pygame.transform.scale(background_surface, (int(width_bc*1.5), int(height_bc*1.5))) 
#zvaž zvětšení a scale

#GROUPS
player = pygame.sprite.GroupSingle()
player.add(Klobouk())

#vykřičník pohyb pronásledování

game_active =True
#Nepotřebuju score???

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(list)
                if game_active == False:
                    game_active = True

    if game_active:
        screen.fill((0,0,0))
        player_pos_x,player_pos_y = player_movement(player_pos_x,player_pos_y,mazer_surface)
        screen.blit(background_surface,(-player_pos_x,-player_pos_y))
        screen.blit(mazer_surface,(-player_pos_x,-player_pos_y))

        player.draw(screen)

        pygame.display.update()
        clock.tick(40)