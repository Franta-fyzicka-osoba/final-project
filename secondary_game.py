import pygame
pygame.init()
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Gamesa.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center=(window_width//2,4*window_height//5))
        self.speed = window_width//6
    
    def update(self):#movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > 5*window_width//6:
                self.rect.x -= self.speed
        if keys[pygame.K_LEFT]:
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
        self.gravity = 0

    def update(self): #apply gravity
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom == window_height:
            self.kill()
    

def is_collision():
    if pygame.sprite.spritecollide(player.sprite, worm_group, False):
        worm_group.empty()
        return False
    return True

window_width = 960
window_height = 540
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Šílená fantasy: Přežij knihočervy")

clock = pygame.time.Clock()

background = pygame.image.load("Library_background.png")
background_fin = pygame.transform.scale(background, (window_width,window_height))

player = pygame.sprite.GroupSingle()
player.add(Player())

worm_group = pygame.sprite.Group()

game_active = True
score = 0

fallist =[]
movement_counter = 0

for i in range(5):
    x=(i+1)*window_width//6
    fallist.append(x)

print(fallist)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active == False:
                    game_active = True
                    worm_group.empty()
    
    if score == 1200:
            game_active = False

    if game_active:
        score +=1

        screen.blit(background, (0,0))
    
        player.draw(screen)
        if score %4 == 0:
            player.update()

        worm_group.draw(screen)
        worm_group.update()
        if score < 1200 and score >=0:
            if score % 60 == 0:
                for i in range(5):
                    if random.randint(1,200)%2 == 1:
                        worm = Worm(fallist[i], window_height//6)
                        worm_group.add(worm)
        game_active = is_collision()
    pygame.display.update()
    clock.tick(40)