import pygame
import random

pygame.init()
win = pygame.display.set_mode((800, 500))



def action(level, score):

    cratersNum = 4 + level

    # randomX = random.randint(70, 400)
    # randomY = random.randint(100, 700)

    # zoneRange = [70, 80, 90]
    zoneForEach = [120, 120, 120, 120, 120]

    xForEach = [200, 220, 350, 370, 380]
    yForEach = [80, 220, 70, 250, 400]
    craterDigit = [13, 7, 9, 12, 5]
    
    
        #def ranger(exOry, xRange, zRange):
        # var = -10
        # if exOry == "x":
        #     mini = 100
        #     maxi = 700
        # else:
        #     mini = 70
        #     maxi = 400
        # while (var + 30) > maxi or (var - 30) < mini:
        #     oneZero = random.randint(0, 1)
        #     if oneZero == 0:
        #         var = random.randint((xRange - zRange), (xRange - 30))
        #     else:
        #         var = random.randint((xRange + 30), (xRange + zRange))
        # return var
    
    def text_objects(text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((800 / 2), (500 / 2))
        win.blit(TextSurf, TextRect)

    def button(msg, xBut, yBut, radius1, color0, color1, color2, radius2):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if xBut +  radius1> mouse[0] > xBut - radius1 and yBut + radius1 > mouse[1] > yBut - radius1:
            pygame.draw.circle(win, color1, (xBut, yBut), radius2)
            if click[0] == 1:
                pygame.draw.circle(win, color2, (xBut, yBut), radius1)
        else:
            pygame.draw.circle(win, color0, (xBut, yBut), radius1)
        
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = (xBut, yBut)
        win.blit(textSurf, textRect)
    
    # for item in range(cratersNum - 1):
    #     zoneForEach.append(zoneRange[random.randint(0, (len(zoneRange) - 1))])
    #     xForEach.append(ranger("x", xForEach[item], zoneForEach[item]))
    #     yForEach.append(ranger("y", yForEach[item], zoneForEach[item]))
  
    for item in range(cratersNum):

        button("13", xForEach[item], yForEach[item], 50, (139, 0, 139), (255, 0, 0), (144, 56, 56), zoneForEach[item])
