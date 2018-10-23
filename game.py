import pygame
import time
import happyNumbers
import primeNumber
import ulamNumber
import estimations
import ai


start_time = time.time()
pygame.init()
win = pygame.display.set_mode((1000, 550))
pygame.display.set_caption("Space Settlements")
start = True
Mercury = False
Venus = False
Earth = False
Mars = False
Jupiter = False
Saturn = False
Uranus = False
run = False
gameOver = False

AI, PLAYER = 1, 0 

#--------Do not touch! Constants-------#
width = 80
height = 80
radius = 200
zoneRadX = int(width / 2)
zoneRadY = int(height / 2)
startPic = pygame.image.load("pictures/main/start.png")
youWin = pygame.image.load("pictures/main/youWin.png")
gameOver = pygame.image.load("pictures/main/gameOver.png")
#-------Do not touch! Constants--------#


#-----Texts-----#
textMercury = pygame.image.load("pictures/Mercury/text.png")
textVenus = pygame.image.load("pictures/Venus/text.png")
textEarth = pygame.image.load("pictures/Earth/text.png")
textMars = pygame.image.load("pictures/Mars/text.png")
textJupiter = pygame.image.load("pictures/Jupiter/text.png")
textSaturn = pygame.image.load("pictures/Saturn/text.png")
textUranus = pygame.image.load("pictures/Uranus/text.png")
#-----Texts-----#

#-----Buttons-----#

begin = pygame.transform.scale(pygame.image.load("pictures/main/begin.png"), (215, 100))
begin_r = begin.get_rect()
beginOver = pygame.transform.scale(pygame.image.load("pictures/main/beginOver.png"), (215, 100))
beginClicked = pygame.transform.scale(pygame.image.load("pictures/main/beginClicked.png"), (215, 100))

#-----Buttons-----#
#-------Functions--------#

def createCraters(picLoc, list, picLocCol, values, width, height, radius):
    mainList = []
    for item in range(len(list)):
        craterObj = pygame.transform.scale(pygame.image.load(picLoc), (width, height))
        mainList.append([list[item], craterObj, craterObj.get_rect(), \
         pygame.transform.scale(pygame.image.load(picLocCol), (width, height)), \
          values[item], False, radius, zoneColor])
    return mainList

def drawWindow(background):
    win.blit((pygame.image.load(background)), (0, 0))
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

#-------Functions--------#

#-----Start-----#

while start:
    pygame.time.delay(100)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    win.blit(startPic, (0, 0))

    begin_r.x = 393
    begin_r.y = 400
    if begin_r.collidepoint(mouse):
        win.blit(beginOver, (393, 400))
        if click[0] == 1:
            win.blit(beginClicked, (393, 400))
            start = False
            run = True
            Mercury = True
    else:
        win.blit(begin, (393, 400))

    pygame.display.update()

#-----Start-----#

#-------Variables for each level--------#

currentTurn = PLAYER
firstPlayerCoord = None
currentIter = 1
mercuryCraterValue = [2, 5, 7, 8, 13]
mercuryCoords = [(200, 200),(500, 100), (500, 300), (310, 360), (300, 100)]
mercuryRadiuses = {}
mercuryValues = {}
mercuryOwner = {}
for index in range(0, len(mercuryCoords)):
    mercuryRadiuses[mercuryCoords[index]] = radius
    mercuryValues[mercuryCoords[index]] = mercuryCraterValue[index]


if Mercury:
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Mercury/crater.png"
    craterLocCol = "pictures/Mercury/craterColonised.png"
    backgr = "pictures/Mercury/bg1.png"
    mainList = createCraters(craterLoc, \
     mercuryCoords, \
      craterLocCol, mercuryCraterValue, width, height, radius)
elif Venus:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Venus/crater.png"
    craterLocCol = "pictures/Venus/craterColonised.png"
    backgr = "pictures/Venus/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)
elif Earth:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Earth/crater.png"
    craterLocCol = "pictures/Earth/craterColonised.png"
    backgr = "pictures/Earth/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)
elif Mars:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Mars/crater.png"
    craterLocCol = "pictures/Mars/craterColonised.png"
    backgr = "pictures/Mars/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)
elif Jupiter:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Jupiter/crater.png"
    craterLocCol = "pictures/Jupiter/craterColonised.png"
    backgr = "pictures/Jupiter/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)
elif Saturn:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Saturn/crater.png"
    craterLocCol = "pictures/Saturn/craterColonised.png"
    backgr = "pictures/Saturn/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)
elif Uranus:
    craterValue = [2, 5, 7, 8, 13]
    zoneColor = (11, 142, 0)
    craterLoc = "pictures/Uranus/crater.png"
    craterLocCol = "pictures/Uranus/craterColonised.png"
    backgr = "pictures/Uranus/bg1.png"
    mainList = createCraters(craterLoc, \
     ((200, 200),(500, 100), (500, 300), (310, 360), (300, 100)), \
      craterLocCol, craterValue, width, height, radius)

#-------Variables for each level--------#

if Mercury:
    win.blit(textMercury, (0, 0))
elif Venus:
    win.blit(textVenus, (0, 0))
    time.sleep(5)
elif Earth:
    win.blit(textEarth, (0, 0))
    time.sleep(5)
elif Mars:
    win.blit(textMars, (0, 0))
    time.sleep(5)
elif Jupiter:
    win.blit(textJupiter, (0, 0))
    time.sleep(5)
elif Saturn:
    win.blit(textSaturn, (0, 0))
    time.sleep(5)
elif Uranus:
    win.blit(textUranus, (0, 0))
    time.sleep(5)

#-----Game-----#
while run:
    if time.time() - start_time > 0.6:
        pygame.time.delay(100)
        drawWindow(backgr)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for item in range(len(mainList)):
            win.blit(mainList[item][1], mainList[item][0])

        for element in mainList:
            if element[2].collidepoint(mouse):
                pygame.draw.circle(win, (11, 142, 0), (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
                win.blit(element[1], (element[0][0], element[0][1]))
                element[2].x = element[0][0]
                element[2].y = element[0][1]
                if click[0] == 1:
                    if not element[5] and currentTurn == PLAYER:
                        if currentIter == 1:
                            firstPlayerCoord = element[0]
                        element[1] = element[3]
                        element[5] = True
                        mercuryOwner[element[0]] = PLAYER
                        currentTurn = AI
                        currentIter += 1
            else:
                win.blit(element[1], (element[0][0], element[0][1]))
                element[2].x = element[0][0]
                element[2].y = element[0][1]
            if element[5]:
                pygame.draw.circle(win, (11, 142, 0), (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
            smallText = pygame.font.Font("freesansbold.ttf", 15)
            textSurf, textRect = text_objects(str(element[4]), smallText)
            textRect.center = element[0]
            win.blit(textSurf, textRect)

        if currentTurn == AI:
            aiTurn = None
            if currentIter != 2:
                aiTurn = ai.minimax(mercuryCoords, mercuryRadiuses, mercuryValues, mercuryOwner, 5)
                aiTurn = aiTurn[1]
            else:
                aiTurn = ai.generateFirstStep(mercuryCoords, mercuryRadiuses, mercuryValues, firstPlayerCoord)
                aiTurn = aiTurn[1]
                mercuryOwner[aiTurn] = AI
            for element in mainList:
                if element[0] == aiTurn:
                    element[1] = element[3]
                    element[5] = True
            currentTurn = PLAYER 
    pygame.display.update()
pygame.quit()

#-----End-----#

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


    # for element in range(len(mainList)):
    #     if mainList[element][2].collidepoint(mouse):
    #         pygame.draw.circle(win, (11, 142, 0), ((mainList[element][0][0] + 75), \
    #          (mainList[element][0][1] + 75)), mainList[element][6], 4)
    #         win.blit(mainList[item][1], mainList[item][0])
    #         (pygame.transform.scale(pygame.image.load("crater.png").get_rect(), (150, 150)).get_rect()).x = mainList[element][0][0]
    #         (pygame.transform.scale(pygame.image.load("crater.png").get_rect(), (150, 150)).get_rect()).y = mainList[element][0][1]
    #     if clic

    
    # if isClicked:
    #     pygame.draw.circle(win, (11, 142, 0), (craterXCord[0] + 75, craterYCord[0] + 75), 150, 4)