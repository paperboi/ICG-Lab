# #######################################
# DDA ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

pygame.init()
running = True
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Digital Differential Algorithm")

BGColor = (4, 15, 15)
TextColor1 = (46, 233, 131)
TextColor2 = (242, 226, 186)
TextColor3 = (252, 255, 252)
TextColor4 = (43, 168, 74)
LineColor = (255, 229, 74)

(X1, Y1) = (350, 350)
(X2, Y2) = (650, 750)
M = float((Y2-Y1)/(X2-X1))

def DisplayIntro(Text, Color, Size, XPos, YPos):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, BGColor)
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = XPos
	DisplayTextRect.centery = YPos
	screen.blit(DisplayText, DisplayTextRect)

def Intro():
	DisplayIntro("Digital Differential Algorithm", TextColor1, 40, 750, 30)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", TextColor2, 25, 750, 60)
	DisplayIntro("ESC to exit", TextColor3, 22, 750, 100)
	DisplayIntro("Start point = (" + str(X1) + ", " + str(Y1) + ")", TextColor4, 22, 750, 130)	 
	DisplayIntro("End point = (" + str(X2) + ", " + str(Y2) + ")", TextColor4, 22, 750, 150)	 

def DDA((X1, Y1), (X2, Y2)):
	Xk = X1
	Yk = Y1

	M = float((Y2-Y1)/(X2-X1))
	print M

	while Yk <= Y2:
		print(int(Xk), int(round(Yk)))
		gfxdraw.pixel(screen, int(round(Xk)), int(screen.get_width() - round(Yk)), LineColor)
		Xk = Xk + 1
		Yk = Yk + M
	pygame.display.flip()

screen.fill(BGColor)
Intro()
DDA((X1, Y1), (X2, Y2))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
	pygame.display.flip()
pygame.quit()