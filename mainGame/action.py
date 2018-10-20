import pygame
import random
import crater
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
    craterDigit = ["13", "7", "9", "12", "5"]
    
    what = ["prime", "", ]

    craters = []
    isClicked = []
    
    # for item in range(cratersNum - 1):
    #     zoneForEach.append(zoneRange[random.randint(0, (len(zoneRange) - 1))])
    #     xForEach.append(ranger("x", xForEach[item], zoneForEach[item]))
    #     yForEach.append(ranger("y", yForEach[item], zoneForEach[item]))
  
    for item in range(cratersNum):
        craters.append(crater.Crater(craterDigit[item], xForEach[item], yForEach[item], \
            50, (139, 0, 139), (255, 0, 0), (144, 56, 56), zoneForEach[item], item))
    for item in craters:
        item.button(isClicked)
    
    for item in range(cratersNum):
        if isClicked[item] == True and what[item] == what[item + 1]:
            score += 5
        elif isClicked[item] == True and what[item] != what[item + 1]:
            score -= 5