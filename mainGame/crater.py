import pygame
win = pygame.display.set_mode((800, 500))
# imageCr = [pygame.image.load("right_3.png"), pygame.image.load("right_3.png"), pygame.image.load("right_3.png")]

class Crater():
    def __init__(self, msg, xBut, yBut, radius1, color0, color1, color2, radius2, whatEx):
        self.msg = msg
        self.xBut = xBut
        self.yBut = yBut
        self.radius1 = radius1
        self.color0 = color0
        self.color1 = color1
        self.color2 = color2
        self.radius2 = radius2
        self.whatEx = whatEx
    def button(self, array):
        def text_objects(text, font):
            textSurface = font.render(text, True, (0, 0, 0))
            return textSurface, textSurface.get_rect()
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.xBut +  self.radius1> mouse[0] > self.xBut - self.radius1 and self.yBut + self.radius1 > mouse[1] > self.yBut - self.radius1:
            pygame.draw.circle(win, self.color1, (self.xBut, self.yBut), self.radius2)
            array.append(self.whatEx)
            if click[0] == 1:
                pygame.draw.circle(win, self.color2, (self.xBut, self.yBut), self.radius1)
                array.append(True)
            array.append(False)
        else:
            pygame.draw.circle(win, self.color0, (self.xBut, self.yBut), self.radius1)
            array.append(False)
        
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = (self.xBut, self.yBut)
        win.blit(textSurf, textRect)