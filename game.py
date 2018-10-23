import pygame
import time
import happyNumbers
import primeNumber
import ulamNumber
import estimations
import ai
import random
import numberGenerators


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
CONDITION_ULAM, CONDITION_PRIME, CONDITION_HAPPY = 0, 1, 2
friendlyColor = (11, 142, 0)
enemyColor = (250, 0, 0)

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

def generateCondition(ulam = 0, prime = 1, happy = 2):
    condMin = min([ulam, prime, happy])
    condMax = max([ulam, prime, happy])
    chooseCond = random.randint(condMin, condMax)
    return chooseCond


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
for planet in range(7):
    currentTurn = PLAYER
    currentCondition = generateCondition()
    firstPlayerCoord = None
    playerStartTime = None
    currentIter = 1
    playerIter = 1
    planetCraterValue = []
    planetCraterValue.extend(numberGenerators.generateRandomPrime(2, 100))
    planetCraterValue.extend(numberGenerators.generateRandomUlam(2, 100))
    planetCraterValue.extend(numberGenerators.generateRandomHappy(1, 100))
    planetCoords = []
    # planetCoords = [(200, 200),(500, 100), (500, 300), (310, 360), (300, 100)]
    planetRadiuses = {}
    planetValues = {}
    planetOwner = {}

    if planet == 0:
        # craterValue = [2, 5, 7, 8, 13]
        zoneColor = (11, 142, 0)
        planetCoords = [(200, 200),(500, 100), (500, 300), (310, 360), (300, 100)]
        craterLoc = "pictures/Mercury/crater.png"
        craterLocCol = "pictures/Mercury/craterColonised.png"
        backgr = "pictures/Mercury/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 1:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Venus/crater.png"
        craterLocCol = "pictures/Venus/craterColonised.png"
        backgr = "pictures/Venus/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 2:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Earth/crater.png"
        craterLocCol = "pictures/Earth/craterColonised.png"
        backgr = "pictures/Earth/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 3:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Mars/crater.png"
        craterLocCol = "pictures/Mars/craterColonised.png"
        backgr = "pictures/Mars/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 4:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Jupiter/crater.png"
        craterLocCol = "pictures/Jupiter/craterColonised.png"
        backgr = "pictures/Jupiter/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 5:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Saturn/crater.png"
        craterLocCol = "pictures/Saturn/craterColonised.png"
        backgr = "pictures/Saturn/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 
    elif planet == 6:
        planetCoords = [(100, 100),(500, 100), (500, 300), (310, 360), (300, 100)]
        zoneColor = (11, 142, 0)
        craterLoc = "pictures/Uranus/crater.png"
        craterLocCol = "pictures/Uranus/craterColonised.png"
        backgr = "pictures/Uranus/bg1.png"
        mainList = createCraters(craterLoc, \
         planetCoords, \
          craterLocCol, planetCraterValue, width, height, radius) 

    for index in range(0, len(planetCoords)):
        planetRadiuses[planetCoords[index]] = radius
        planetValues[planetCoords[index]] = planetCraterValue[index]

    #-------Variables for each level--------#

    if planet == 0:
        win.blit(textMercury, (0, 0))
    elif planet == 1:
        win.blit(textVenus, (0, 0))
    elif planet == 2:
        win.blit(textEarth, (0, 0))
    elif planet == 3:
        win.blit(textMars, (0, 0))
    elif planet == 4:
        win.blit(textJupiter, (0, 0))
    elif planet == 5:
        win.blit(textSaturn, (0, 0))
    elif planet == 6:
        win.blit(textUranus, (0, 0))

    #-----Game-----#
    playerStartTime = time.time()
    emptySpot = None
    while run:
        if time.time() - start_time > 5:
            pygame.time.delay(100)
            drawWindow(backgr)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if time.time() - playerStartTime > 5:
                playerStartTime = time.time()
                currentIter += 1
                currentTurn = AI if currentTurn == PLAYER else PLAYER

            for item in range(len(mainList)):
                win.blit(mainList[item][1], mainList[item][0])
            emptySpot = False
            for element in mainList:
                if not element[5]:
                    emptySpot = True
                if element[2].collidepoint(mouse):
                    pygame.draw.circle(win, friendlyColor, (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
                    win.blit(element[1], (element[0][0], element[0][1]))
                    element[2].x = element[0][0]
                    element[2].y = element[0][1]
                    if click[0] == 1:
                        playerPoints = ai.associatedElements(planetOwner, PLAYER, planetCoords)
                        chosenNumberProps = []
                        if ulamNumber.ulamNumbers(planetValues[element[0]]):
                            chosenNumberProps.append(CONDITION_ULAM)
                        if primeNumber.primeNumber(planetValues[element[0]]):
                            chosenNumberProps.append(CONDITION_PRIME)
                        if happyNumbers.happyNumbers(planetValues[element[0]]):
                            chosenNumberProps.append(CONDITION_HAPPY)
                        if not element[5] and currentTurn == PLAYER and (playerIter == 1 or ai.distanceAvailability(element[0], planetRadiuses[element[0]], playerPoints)) and currentCondition in chosenNumberProps:
                            if currentIter == 1:
                                firstPlayerCoord = element[0]
                            element[1] = element[3]
                            element[5] = True
                            planetOwner[element[0]] = PLAYER
                            currentTurn = AI
                            currentIter += 1
                            playerIter += 1
                            playerStartTime = time.time()
                else:
                    win.blit(element[1], (element[0][0], element[0][1]))
                    element[2].x = element[0][0]
                    element[2].y = element[0][1]
                if element[5]:
                    curColor = None
                    if planetOwner[element[0]] == PLAYER:
                        curColor = friendlyColor
                    elif planetOwner[element[0]] == AI:
                        curColor = enemyColor
                    pygame.draw.circle(win, curColor, (element[0][0] + zoneRadX, element[0][1] + zoneRadY), radius, 4)
                smallText = pygame.font.Font("freesansbold.ttf", 15)
                textSurf, textRect = text_objects(str(element[4]), smallText)
                textRect.center = element[0]
                win.blit(textSurf, textRect)

            if currentTurn == AI:
                aiTurn = None
                aiCoordsToChoose = []
                for coord in planetCoords:
                    chosenNumberProps = []
                    if ulamNumber.ulamNumbers(planetValues[coord]):
                        chosenNumberProps.append(CONDITION_ULAM)
                    if primeNumber.primeNumber(planetValues[coord]):
                        chosenNumberProps.append(CONDITION_PRIME)
                    if happyNumbers.happyNumbers(planetValues[coord]):
                        chosenNumberProps.append(CONDITION_HAPPY)
                    if currentCondition in chosenNumberProps:
                        aiCoordsToChoose.append(coord)
                if currentIter != 2:
                    aiTurn = ai.minimax(aiCoordsToChoose, planetRadiuses, planetValues, planetOwner, 5)
                    aiTurn = aiTurn[1]
                    planetOwner[aiTurn] = AI
                    currentCondition = generateCondition()
                    
                    currentTurn = PLAYER
                    playerStartTime = time.time()
                else:
                    aiTurn = ai.generateFirstStep(aiCoordsToChoose, planetRadiuses, planetValues, firstPlayerCoord)
                    aiTurn = aiTurn[1]
                    planetOwner[aiTurn] = AI
                    currentCondition = generateCondition()

                    currentTurn = PLAYER
                    playerStartTime = time.time()
                for element in mainList:
                    if element[0] == aiTurn:
                        element[1] = element[3]
                        element[5] = True
            if not emptySpot:
                break  
        else:
            playerStartTime = time.time()
        print(playerStartTime - time.time())
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