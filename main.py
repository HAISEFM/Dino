from doctest import FAIL_FAST
from pickle import FALSE
import pygame 
import random

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1280, 640))

pygame.display.set_caption("Game")

icon = pygame.image.load("assets/Icons/main_icon.png")
pygame.display.set_icon(icon)

running = True
checker = False

myfont = pygame.font.Font("assets/Font/RubikDoodleShadow-Regular.ttf", 25)

skin = "Dino"

skins = ["Dino", "DinoGirl", "DinoBoy", "Horsi"]

dino_run = [ 
    pygame.image.load("assets/Skins/" + skin + "/DinoRun1.png"),
    pygame.image.load("assets/Skins/" + skin + "/DinoRun1.png"), 
    pygame.image.load("assets/Skins/" + skin + "/DinoRun2.png")
    ]

Cactus = [
    pygame.image.load("assets/Cactus/LargeCactus1.png"),
    pygame.image.load("assets/Cactus/LargeCactus2.png"), 
    pygame.image.load("assets/Cactus/LargeCactus3.png"), 
    pygame.image.load("assets/Cactus/SmallCactus1.png"), 
    pygame.image.load("assets/Cactus/SmallCactus2.png"), 
    pygame.image.load("assets/Cactus/SmallCactus3.png")
]

cactus_count = 5

cactus_x = 1440

cactus_y = 420

dino_anim_count = 0

track_x = 0

is_jump = False

jump_count = 10

dodge_count = 10

dino_x = 30

dino_y = 420

is_dodge = False

cactus_here = False

gameplay = True

i = 0

speed = 0



label = pygame.font.Font("assets/Font/RubikDoodleShadow-Regular.ttf", 25)

lose_label = label.render("Вы проиграли!", False, '#F7f7f7')

res_label = label.render("Начать заново!", False, '#F3f3f3')

res_label_rect = res_label.get_rect(topleft = (500, 320))

def death(a):
    return(dino_rect.colliderect(a))

while running:

    pygame.display.update()
    

    if gameplay == True:
        
        #screen.blit(point, (1200, 120), 12)
        #point += 1

        #image
        screen.fill("#f8f8f8")
        screen.blit(pygame.image.load("assets/Other/Track.png"), (track_x, 500))
        screen.blit(pygame.image.load("assets/Other/Track.png"), (track_x + 1280, 500))
        screen.blit(dino_run[dino_anim_count], (30, dino_y))
        screen.blit(Cactus[cactus_count % 5], (cactus_x, cactus_y))
        
        #rect

        dino_rect = dino_run[1].get_rect(topleft = (dino_x, dino_y))
        cactus_rect = Cactus[cactus_count].get_rect(topleft = (cactus_x, cactus_y))
        


        #animation
        track_x -= 20 + speed
        if track_x <= -1280: 
            track_x = 0
        
        if cactus_here:
            if cactus_x <= -30:
                cactus_count = random.randrange(0, 6)
                cactus_x = 1440
                cactus_here = False
        else:
            if cactus_count >= 3:
                cactus_y = 440
            else:
                cactus_y = 420

            screen.blit(Cactus[cactus_count], (cactus_x, cactus_y))
            cactus_here = True


        if dino_anim_count == 2 and dino_anim_count != 0:
            dino_anim_count = 1
        else:
            dino_anim_count += 1
        
        cactus_x -= 20 + speed
        
        #keys
            
        keys = pygame.key.get_pressed()
        #jump
        if not is_jump:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                screen.blit(pygame.image.load("assets/Skins/" + skin + "/DinoJump.png"), (30, dino_y))
                if jump_count > 0:
                    dino_y -= (jump_count ** 2) / 2
                else:
                    dino_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10
        
        if death(cactus_rect):
            gameplay = False
        i += 1
        if (i % 100 == 0):
            speed += 1
    else:
        screen.fill("#000000")
        screen.blit(lose_label, (500, 220))
        screen.blit(res_label, res_label_rect)
        mouse = pygame.mouse.get_pos()
        if res_label_rect.collidepoint(mouse):
            cactus_x -= 100
            gameplay = True
            
    #exit
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(20)
