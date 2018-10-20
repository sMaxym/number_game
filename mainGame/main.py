import pygame
import action
pygame.init()
win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Settlements")




# def drawWindow():
#     win.blit((pygame.image.load("bg.jpg")), (0, 0))
#     pygame.display.update()
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





    action.action(1, 0)








    
    pygame.display.update()
pygame.quit()