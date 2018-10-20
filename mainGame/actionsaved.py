import pygame

pygame.init()
win = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Space Settlements")
x = 150
y = 100
width1 = 400
height1 = 150
radius = 20
run = True
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800 / 2), (500 / 2))
    win.blit(TextSurf, TextRect)

def button(msg, xBut, yBut, radius1, color0, color1, color2):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if xBut +  radius1> mouse[0] > xBut - radius1 and yBut + radius1 > mouse[1] > yBut - radius1:
        pygame.draw.circle(win, color1, (xBut, yBut), radius1 + 10)
        if click[0] == 1:
            pygame.draw.circle(win, color2, (xBut, yBut), radius1)
    else:
        pygame.draw.circle(win, color0, (xBut, yBut), radius1)
    
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (xBut, yBut)
    win.blit(textSurf, textRect)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    def action(level, score):
        pass

    button("13", x, y, 20, (139, 0, 139), (255, 0, 0), (144, 56, 56))
    button("10", x + 50, y - 70, 20, (139, 0, 139), (255, 0, 0), (144, 56, 56))
    pygame.display.update()
pygame.quit()