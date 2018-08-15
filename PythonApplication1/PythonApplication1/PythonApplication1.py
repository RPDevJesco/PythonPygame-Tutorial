
import pygame

pygame.init()

dWidth = 800

dHeight = 600

gameDisplay = pygame.display.set_mode((dWidth, dHeight))

pygame.display.set_caption("Game Dev Made Easy Tutorial")

gdmeLogo = pygame.image.load('Jesco.png')

def logo(x,y):
    gameDisplay.blit(gdmeLogo, (x,y))

x = 150

y = 50

closed = False

while not closed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    logo(x,y)

    pygame.display.update()

pygame.quit()
quit()