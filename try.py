# # # import pygame
# # # pygame.init()
# # # screen=pygame.display.set_mode((1000,500))
# # # player=pygame.Rect(250,200,50,50)
# # # player2=pygame.Rect(250,151,50,50)
# # # # open("abc.py","x")
# # # runing=True
# # # clock=pygame.time.Clock()
# # # while(runing):
# # #     for event in pygame.event.get():
# # #         if event.type==pygame.QUIT:
# # #             runing=False
# # #     pygame.draw.rect(screen,(0,255,0),player)
# # #     pygame.draw.rect(screen,"white",player2)
# # #     keys=pygame.key.get_pressed()
# # #     if keys[pygame.K_LEFT]:
# # #         player.x-=5
# # #
# # #     if (keys[pygame.K_RIGHT]):
# # #         player2.x+=5
# # #     if (player.colliderect(player2)):
# # #         print("detected")
# # #         running=False
# # #
# # #     clock.tick(30)
# # #
# # #     pygame.display.update()
# # #     screen.fill("black")
# # #
# # #
# #
# #
# # import pygame
# # import random
# #
# # pygame.init()
# # screen = pygame.display.set_mode((500, 500))
# # clock = pygame.time.Clock()
# #
# # # Define Timer Event for 3 seconds (3000 ms)
# # DRAW_EVENT = pygame.USEREVENT + 1
# # pygame.time.set_timer(DRAW_EVENT, 3000)
# #
# # rectangles = []  # List to store rectangle objects
# #
# # running = True
# # while running:
# #     screen.fill((0, 0, 0))  # Clear screen
# #
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #
# #         # When 3 seconds pass, add a new rectangle
# #         if event.type == DRAW_EVENT:
# #             x = random.randint(50, 450)
# #             y = random.randint(50, 450)
# #             rect = pygame.Rect(x, y, 50, 50)  # Create a rectangle
# #             rectangles.append(rect)  # Store in the list
# #
# #     # Move all rectangles left if LEFT key is pressed
# #     keys = pygame.key.get_pressed()
# #     if keys[pygame.K_LEFT]:
# #         for rect in rectangles:
# #             rect.x -= 5  # Move left
# #
# #     # Draw all rectangles
# #     for rect in rectangles:
# #         pygame.draw.rect(screen, (0, 255, 0), rect)
# #
# #     pygame.display.update()
# #     clock.tick(30)
# #
# # pygame.quit()
#
#
# #
# #
# # import pygame
# # import random
# # pygame.init()
# # screen=pygame.display.set_mode((1000,600))
# # clock=pygame.time.Clock()
# #
# # pipes=pygame.USEREVENT+1
# # pygame.time.set_timer(pipes,3000)
# #
# # pipess=[]
# # running=True
# # while(running):
# #     screen.fill("black")
# #     for event in pygame.event.get():
# #         if event.type==pygame.QUIT:
# #             running=False
# #         if event.type==pipes:
# #             yy=random.randint(200,500)
# #             # if (yy<0):
# #             #     yy*=-1
# #
# #             react1=pygame.Rect(1020,yy,50,600-yy)
# #             react2 = pygame.Rect(1020, yy-150-400, 50, 400)
# #             print(yy)
# #             print(300-yy)
# #             pipess.append((react1,react2))
# #     for react in pipess[:]:
# #         react1,react2=react
# #         pygame.draw.rect(screen,"green",react1)
# #         pygame.draw.rect(screen, "green", react2)
# #         react1.x-=5
# #         react2.x-=5
# #         if(react1.x<0):
# #             pipess.remove(react)
# #         if (react.colli)
# #
# #
# #     clock.tick(30)
# #     pygame.display.update()
#
#
#
# import pygame
# import random
# pygame.init()
#
# screen=pygame.display.set_mode((1000,600))
# clock=pygame.time.Clock()
# bird=pygame.image.load("Flappy-Bird-Transparent-PNG")
# bird=pygame.transform.scale(bird,(50,50))
# running=True
# gravety=2
#
#
# while(running):
#     screen.fill("black")
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#     keys = pygame.key.get_pressed()
#     pygame.draw.rect(screen, "green", bird)
#     if keys[pygame.K_SPACE]:
#         bird.y-=7
#     bird.y+=gravety
#     pygame.display.update()
#     clock.tick(60)



import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Load bird image
bird_img = pygame.image.load("Flappy-Bird-Transparent-PNG.png")
bird_img = pygame.transform.scale(bird_img, (50, 50))  # Resize image

# Create a Rect for bird to track position
bird_rect = bird_img.get_rect()
bird_rect.topleft = (50, 300)  # Set initial position

# Pipe settings
pipes = pygame.USEREVENT + 1
pygame.time.set_timer(pipes, 3000)
gravity = 3
pipess = []

running = True
while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pipes:
            yy = random.randint(200, 500)
            react1 = pygame.Rect(1020, yy, 50, 600 - yy)
            react2 = pygame.Rect(1020, yy - 150 - 400, 50, 400)
            pipess.append((react1, react2))

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_rect.y -= 10  # Move up on space press

    # Apply gravity
    bird_rect.y += gravity

    # Draw pipes and move them
    for react1, react2 in pipess[:]:
        pygame.draw.rect(screen, "green", react1)
        pygame.draw.rect(screen, "green", react2)
        react1.x -= 5
        react2.x -= 5

        # Remove pipes if off-screen
        if react1.x < -50:
            pipess.remove((react1, react2))

        # Collision detection
        if react1.colliderect(bird_rect) or react2.colliderect(bird_rect):
            print("Collision detected!")
            running = False

    # Draw bird
    screen.blit(bird_img, bird_rect)

    clock.tick(40)
    pygame.display.update()

pygame.quit()
