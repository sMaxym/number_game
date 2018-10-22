import pygame
pygame.init()
win = pygame.display.set_mode((1000, 550))
pygame.display.set_caption("Space Settlements")



def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

width = 50
height = 50
radius = 200
zoneRadX = int(width / 2)
zoneRadY = int(height / 2)
def createCraters(list, values, width, height, radius):
    mainList = []
    for item in range(len(list)):
        craterObj = pygame.transform.scale(pygame.image.load("crater.png"), (width, height))
        mainList.append([list[item], craterObj, craterObj.get_rect(), \
         pygame.transform.scale(pygame.image.load("craterColonised.png"), (width, height)), \
          values[item], False, radius, True])
    return mainList



craterValue = [2, 5, 7, 8, 13]
mainList = createCraters(((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), craterValue, width, height, radius)


# def createCraters(list):
#     global craterValue
#     global mainList
#     for item in range(len(list)):
#         mainList.append((list[item], "crater.png", craterValue, "craterColonised.png", False, 150))



# for item in range(len(mainList)):
#     crater1 = pygame.transform.scale(pygame.image.load(), (150, 150))
#     crater_r = crater1.get_rect()
#     crater1Colon = pygame.transform.scale(pygame.image.load("craterColonised.png"), (150, 150))







# craterXCord = [300]
# craterYCord = [125]

def drawWindow():
    win.blit((pygame.image.load("bg.png")), (0, 0))
    pygame.display.update()


isClicked = False

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawWindow()


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    # if isClicked:
    #     pygame.draw.circle(win, (11, 142, 0), (craterXCord[0] + 75, craterYCord[0] + 75), 150, 4)

    for item in range(len(mainList)):
        win.blit(mainList[item][1], mainList[item][0])








    # for element in range(len(mainList)):
    #     if mainList[element][2].collidepoint(mouse):
    #         pygame.draw.circle(win, (11, 142, 0), ((mainList[element][0][0] + 75), \
    #          (mainList[element][0][1] + 75)), mainList[element][6], 4)
    #         win.blit(mainList[item][1], mainList[item][0])
    #         (pygame.transform.scale(pygame.image.load("crater.png").get_rect(), (150, 150)).get_rect()).x = mainList[element][0][0]
    #         (pygame.transform.scale(pygame.image.load("crater.png").get_rect(), (150, 150)).get_rect()).y = mainList[element][0][1]
    #     if clic

    for element in mainList:
        if element[2].collidepoint(mouse):
            pygame.draw.circle(win, (11, 142, 0), (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
            win.blit(element[1], (element[0][0], element[0][1]))
            element[2].x = element[0][0]
            element[2].y = element[0][1]
            if click[0] == 1:
                element[1] = element[3]
                element[5] = True
                element[7] = False
        else:
            win.blit(element[1], (element[0][0], element[0][1]))
            element[2].x = element[0][0]
            element[2].y = element[0][1]
        if element[5]:
            pygame.draw.circle(win, (11, 142, 0), (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
        if element[7]:
            smallText = pygame.font.Font("freesansbold.ttf", 15)
            textSurf, textRect = text_objects(str(element[4]), smallText)
            textRect.center = element[0]
            win.blit(textSurf, textRect)




    # if crater_r.collidepoint(mouse):
    #     pygame.draw.circle(win, (11, 142, 0), (craterXCord[0] + 75, craterYCord[0] + 75), 150, 4)
    #     win.blit(crater1, (craterXCord[0], craterYCord[0]))
    #     crater_r.x = craterXCord[0]
    #     crater_r.y = craterYCord[0]
    #     if click[0] == 1:
    #         crater1 = crater1Colon
    #         isClicked = True
    # else:
    #     win.blit(crater1, (craterXCord[0], craterYCord[0]))
    #     crater_r.x = craterXCord[0]
    #     crater_r.y = craterYCord[0]











    
    pygame.display.update()
pygame.quit()

    # win.blit(craterOver1, (craterXCord[0] - 75, craterYCord[0] - 75))

    # if craterXCord[0] +  75> mouse[0] > craterXCord[0] - 75 and craterYCord[0] + 75 > mouse[1] > craterYCord[0] - 75:
    #     win.blit(craterOver1, (craterXCord[0], craterYCord[0]))
    # else:
    #     win.blit(crater1, (craterXCord[0], craterYCord[0]))


    # if crater1.get_rect().collidepoint(mouse):
    #     print("z")
    # print(mouse)
    # win.blit(crater1, (craterXCord[0], craterYCord[0]))


    # if crater_r.collidepoint(mouse):
    #     # win.blit(craterOver1, (craterXCord[0] - 75, craterYCord[0] - 75))
    #     pygame.draw.circle(win, (11, 142, 0), (craterXCord[0] + 75, craterYCord[0] + 75), 150, 4)
    #     win.blit(crater1, (craterXCord[0], craterYCord[0]))
    #     crater_r.x = craterXCord[0]
    #     crater_r.y = craterYCord[0]
    #     if click[0] == 1:
    #         crater1 = crater1Colon
    # else:
    #     win.blit(crater1, (craterXCord[0], craterYCord[0]))
    #     crater_r.x = craterXCord[0]
    #     crater_r.y = craterYCord[0]
