#import pygame,random,time
import pygame as p
import random
import time

p.init()
clock = p.time.Clock()

#set up display
WIDTH = 600
HEIGHT = 600
screen = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("snake game")

#score and function
score = 0
def score_leval():
    global score
    font = p.font.SysFont(None,36)
    text = font.render(f'Score : {score}',True,(255,255,255))
    screen.blit(text,(10,10))

#load snake head
head_image = p.image.load("pygame/snakegame/pngwing.com (8).png")
head_image = p.transform.scale(head_image,(20,20))
head_x = 300
head_y = 300
speed = 10

#load snake body part image
body = []
part_img = p.image.load("pygame/snakegame/pngwing.com (8).png")
part_img = p.transform.scale(part_img,(20,20))

#load food
food_img = p.image.load("pygame/snakegame/pngwing.com (5).png")
food_img = p.transform.scale(food_img,(20,20))
food_x = random.randint(0,WIDTH-20)
food_y = random.randint(0,HEIGHT-20)

#move function
def head_movement():
    global head_x,head_y
    keys = p.key.get_pressed()
    if keys[p.K_RIGHT]:
        head_x += speed

    elif keys[p.K_LEFT]:
        head_x -= speed
    
    elif keys[p.K_DOWN]:
        head_y += speed

    elif keys[p.K_UP]:
        head_y -= speed



#main loop
running = True
while running:
    #FPS
    clock.tick(8)

    #Quit
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    #player movement & save privious location
    old_x = head_x
    old_y = head_y
    head_movement()

    #body part movement
    if len(body) > 0:
        for i in range(len(body)-1,0,-1):
            body[i] = body[i-1][:]
        body[0] = [old_x,old_y]


    #player and food add to rectangle
    head_rec = p.Rect(head_x,head_y,20,20)
    food_rec = p.Rect(food_x,food_y,20,20)

    #player and food colision
    if head_rec.colliderect(food_rec):
        score += 10
        food_x = random.randint(0,WIDTH-20)
        food_y = random.randint(0,HEIGHT-20)
        
        if len(body) > 0:
            body.append(body[-1][:])
        else:
            body.append([old_x,old_y])


    #player and body colision
    for part in body[5:]:
        body_rec = p.Rect(part[0],part[1],20,20)
        if head_rec.colliderect(body_rec):
            running = False

    #player and border colision
    if (0 > head_x or head_x > (WIDTH - 20) or 0 > head_y or head_y > (HEIGHT-20)):
        running = False 

    #draw all --------------------------------------/
    #screen fill
    screen.fill((0,0,0))

    #food draw
    screen.blit(food_img,(food_x,food_y))

    #body draw
    for part in body:
        screen.blit(part_img,(part[0],part[1]))

    #head draw
    screen.blit(head_image,(head_x,head_y))

    #update score and screen
    score_leval()
    p.display.update()

#pygame quit
p.quit()