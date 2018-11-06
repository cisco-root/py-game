import pygame
import time
import random


pygame.init()

crash_sound = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")

display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
blue = (0,0,255)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)

pygame.display.set_caption('car race')

clock = pygame.time.Clock()

carimg = pygame.image.load ("Bug.png")

car_width = 48

def button(msg,x,y,w,h,ia,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(gameDisplay,ia,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)
            

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Let's play game",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("Play!!",150,450,100,50,green,bright_green,"Play")
        button("Quit",550,450,100,50,red,bright_red,"Quit")

        pygame.display.update()


def stuff_dodged (count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+str(count) , True , blue)
    gameDisplay.blit(text,(0,0))


def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])


def car(x,y):
    gameDisplay.blit(carimg,(x,y))


def text_objects(text,font):
    textSurface = font.render(text, True , black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep (2)
    game_loop()


def crash ():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects("You crashd",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Try agian",150,450,100,50,green,bright_green,"Play")
        button("Quit",550,450,100,50,red,bright_red,"quit")

        pygame.display.update()


def game_loop():

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    X_change = 0


    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100

    dodged = 0

    gameexit = False

    while not gameexit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_change = -5
                elif event.key == pygame.K_RIGHT:
                    X_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    X_change = 0

        x += X_change
        gameDisplay.fill(white)

        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,red)
        stuff_starty += stuff_speed

        stuff_dodged(dodged)

        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()
        
        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_width)
            dodged += 1
            stuff_speed += 1



            
        if y < stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                crash()


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()