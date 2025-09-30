import pygame
import random
from score import highestscore
pygame.init()

screen=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()
bird=pygame.image.load("Flappy-Bird-Transparent-PNG.png")
bird=pygame.transform.scale(bird,(70,70))
bg=pygame.image.load("Screenshot 2025-03-29 220711.png")
bg=pygame.transform.scale(bg,(1000,600))
bird_rect=bird.get_rect()
bird_rect.x=50
bird_rect.y=300
bird_up=10
pipes=pygame.USEREVENT+1
pipetime=3000
pygame.time.set_timer(pipes,pipetime)
score=0
pygame.font.init()
font = pygame.font.Font(None, 36)
text_surface1 = font.render((f"highest score: {highestscore}"), True, (255, 255, 255))
text_rect = text_surface1.get_rect(center=(500, 20))
text_surface2 = font.render((f"score {score}"), True, (255, 255, 255))
text_rect2 = text_surface2.get_rect(center=(500, 50))
polemove=5
gravety=5
pipess=[]
running=True
while(running):

    screen.blit(bg,(0,0))
    screen.blit(bird,bird_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pipes:
            yy=random.randint(200,500)
            # if (yy<0):
            #     yy*=-1

            react1_img=pygame.image.load("pole-up4---pole-down.png  ")
            react1_img= pygame.transform.scale(react1_img,(50,600-yy))
            react1=react1_img.get_rect()

            react1.topleft=(1020,yy)
            # react2 = pygame.Rect(1020, yy-150-400, 50, 400)


            react2_img = pygame.image.load("pole-up4---pole-up.png")
            react2_img = pygame.transform.scale(react2_img, (50, 400))
            react2 = react1_img.get_rect()

            react2.topleft = (1020, yy-150-400)
            # print(yy)
            # print(300 -yy)
            pipess.append((react1_img,react2_img,react1,react2))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bird_rect.y -= bird_up
    bird_rect.y += gravety
    for react in pipess[:]:
        react1_img,react2_img,react1,react2=react
        screen.blit(react1_img,react1)
        screen.blit(react2_img,react2)
        # pygame.draw.rect(screen, "green", react2)
        react1.x-=polemove
        react2.x-=polemove
        if(react1.x<0):
            pipess.remove(react)
            score += 1
            print(score)
            text_surface1 = font.render((f"highest score: {highestscore}"), True, (255, 255, 255))
            text_rect = text_surface1.get_rect(center=(500, 20))
            text_surface2 = font.render((f"score {score}"), True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(center=(500, 50))

            if (score%10==0):
                if (score<50):
                    polemove+=1.3
                    pipetime-=500
                    bird_up+=1
                    gravety+=0.5
                    pygame.time.set_timer(pipes, 10)

                pygame.time.set_timer(pipes, pipetime)
              



        if (react1.top <  bird_rect.y+ 50 and abs( react1.x-bird_rect.x)<50   ):
            if (highestscore<score):
                file=open("score.py","w")
                file.write("highestscore=")
                file.write(str(score))
                file.close()

            print("collision detected")
            running = False
        if bird_rect.y < react2.y + 380 and abs(react2.x - bird_rect.x) < 50:
            if (highestscore<score):
                file=open("score.py","w")
                file.write("highestscore=")
                file.write(str(score))
                file.close()
            print("collision detected (top pipe)")
            running = False



    screen.blit(text_surface1, text_rect )
    screen.blit(text_surface2, text_rect2)
    if (bird_rect.y>555):
        if (highestscore < score):
            file = open("score.py", "w")
            file.write("highestscore=")
            file.write(str(score))
            file.close()
        print("bird tuched ")
        # print(bird_rect.y)
        running = False
    if (bird_rect.y<-10):
        if (highestscore < score):
            file = open("score.py", "w")
            file.write("highestscore=")
            file.write(str(score))
            file.close()
        print("bird tuched ")
        running = False
    clock.tick(40)
    pygame.display.update()