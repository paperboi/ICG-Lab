# #######################################
# BRESENHAM'S LINE DRAWING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

pygame.init()
running = True
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

BGColor = (4, 15, 15)
TextColor1 = (46, 233, 131)
TextColor2 = (242, 226, 186)
TextColor3 = (252, 255, 252)
TextColor4 = (43, 168, 74)
LineColor = (255, 229, 74)

(X1, Y1) = (350, 350)
(X2, Y2) = (650, 750)
M = (Y2-Y1)/(X2-X1)


def DisplayIntro(Text, Color, Size, XPos, YPos):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, BGColor)
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = XPos
	DisplayTextRect.centery = YPos
	screen.blit(DisplayText, DisplayTextRect)

def Intro():
	DisplayIntro("Bresenham's Line Drawing Algorithm", TextColor1, 40, 750, 30)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", TextColor2, 25, 750, 60)
	DisplayIntro("ESC to exit", TextColor3, 22, 750, 100)
	DisplayIntro("Start point = (" + str(X1) + ", " + str(Y1) + ")", TextColor4, 22, 750, 130)	 
	DisplayIntro("End point = (" + str(X2) + ", " + str(Y2) + ")", TextColor4, 22, 750, 150)	 


def BLine((X1, Y1), (X2, Y2)):
	dX = X2-X1
	dY = Y2-Y1
	P0 = 2*dY-dX
	Pk = P0
	(Xk, Yk) = (X1, Y1)

	while Xk <= X2:
		print(Xk, Yk)
		gfxdraw.pixel(screen, Xk, screen.get_width() - Yk, LineColor)
		Xk = Xk+1
		if Pk < 0:
			Yk = Yk
			Pk = Pk + 2*dY
		elif Pk>0:
			Yk = Yk+1
			Pk = Pk + 2*dY -2*dX

screen.fill(BGColor)
Intro()
BLine((X1, Y1), (X2, Y2))


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
	pygame.display.flip()
pygame.quit()