import pygame as pg
import sys

# pygame initalizing
pg.init()

# screen size
screenInfo = pg.display.Info()
screenDim = [int(screenInfo.current_w*0.5), int(screenInfo.current_h*0.5)]

# create screen
window = pg.display.set_mode(screenDim)
pg.display.set_caption("Prueba")

# refresh rate (in frames per second)
FPS = pg.time.Clock()

# mouse variables
mousePos = []
click = []

# colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkRed = (100,0,0)

def TextObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def TextCentered(text,x,y,fontsize, colour):
    largeText = pg.font.Font(None, fontsize)
    TextSurf, TextRect = TextObjects(text, largeText, colour)
    TextRect.center = (x, y)
    window.blit(TextSurf, TextRect)

def TextLeft(text,x,y,fontsize, colour):
    largeText = pg.font.Font(None, fontsize)
    TextSurf, TextRect = TextObjects(text, largeText, colour)
    TextRect.left = (x, y)
    window.blit(TextSurf, TextRect)

def TextRight(text,x,y,fontsize, colour):
    largeText = pg.font.Font(None, fontsize)
    TextSurf, TextRect = TextObjects(text, largeText, colour)
    TextRect.right = (x, y)
    window.blit(TextSurf, TextRect)

class Button:
    def __init__(self, x, y, width, height, colour, textColour, text = "", OnClick = lambda: None, buttype = "normal", fontSize = 0):
        # mouse
        self.clicked = False
        self.mouseOn = False

        # attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.textColour = textColour
        self.text = text
        self.OnClick = OnClick
        self.buttype = buttype
        if (fontSize != 0):
            self.fontSize = fontSize
        else:
            self.fontSize = height

        # rect
        self.rect = pg.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

    def Print(self):

        self.Draw()

        if (self.rect.collidepoint(mousePos)):
                self.mouseOn = True
                
                self.OnClick()
        else:
            self.clicked = False
            self.mouseOn = False
        
        print(self.clicked)

    def Draw(self):
        if (self.buttype == "normal"):
            self.rect = pg.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

        elif (self.buttype == "centered"):
            self.rect = pg.draw.rect(self.window, self.colour, (self.x, self.y, self.width, self.height)).center(self.x, self.y)

        TextCentered(self.text, self.rect.center[0], self.rect.center[1], self.height, self.textColour)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    #                                                                   getters and setters
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def GetRect(self):
        return self.rect

    def SetPos(self, x, y):
        self.x = x
        self.y = y

    def SetDimensions(self, width, height):
        self.width = width
        self.height = height

    def SetTextColour(self, colour):
        self.textColour = colour
    
    def SetColour(self, colour):
        self.colour = colour

    def SetText(self, text):
        self.text = text



class Screen:
    def __init__(self):
        # buttons
        self.testButton = Button(screenDim[0]//2, screenDim[1] - 100, 100, 50, black, white, "Aa")
        pass

    def Start(self):
        global mousePos, click

        while True:
            # mouse variables
            mousePos = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()


            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
        
            self.MainScreen()

            pg.display.update()
    
    def MainScreen(self):
        # fill with dark red
        window.fill(white)

        # add texts
        TextCentered("Saludos, camaradas!", screenDim[0]//2, screenDim[1]//2, 40, black)
        TextCentered("Ratón en posición: " + str(mousePos[0]) + ", " + str(mousePos[1]), screenDim[0]//2,screenDim[1]//3, 25, green)

        self.testButton.Print()

        FPS.tick(30)


if __name__ == "__main__":
    Screen().Start()