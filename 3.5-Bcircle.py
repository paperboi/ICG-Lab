# #######################################
# BRESENHAM'S CIRCLE DRAWING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

BGColor = (4, 15, 15)
TextColor1 = (46, 233, 131)
TextColor2 = (242, 226, 186)
TextColor3 = (252, 255, 252)
TextColor4 = (43, 168, 74)
LineColor = (255, 229, 74)

(X, Y) = (350, 350)
R = 250

pygame.init()
screen = pygame.display.set_mode((0,0))
pygame.display.set_caption("Bresenham's Circle Drawing Algorithm")
screen.fill(BGColor)

def DisplayIntro(Text, Color, Size, XPos, YPos):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, BGColor)
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = XPos
	DisplayTextRect.centery = YPos
	screen.blit(DisplayText, DisplayTextRect)

def Intro():
	DisplayIntro("Bresenham's Circle Drawing Algorithm", TextColor1, 40, 1000, 30)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", TextColor2, 25, 1000, 60)
	DisplayIntro("Use the left mouse button to change the center of the circle", TextColor3, 22, 1000, 110)
	DisplayIntro("Use the mousewheel to change the radius of the circle", TextColor3, 22, 1000, 130)
	DisplayIntro("ESC to exit", TextColor3, 22, 1000, 150)
	DisplayIntro("Center = (" + str(X) + ", " + str(Y) + ")", TextColor4, 22, 1000, 190)	 
	# DisplayIntro("End point = (" + str(X + L * math.cos(math.radians(A))) + ", " + str(Y + L * math.sin(math.radians(A))) + ")", TextColor4, 22, 1000, 210)	 
	DisplayIntro("Radius = " + str(R), TextColor4, 22, 1000, 210)	 
	# DisplayIntro("Angle = " + str(A), TextColor4, 22, 1000, 250)	 
	# DisplayIntro("Number of iterations = " + str(N), TextColor4, 22, 1000, 270)	 

def DrawCircle(Xc, Yc, X, Y):
		gfxdraw.pixel(screen, Xc+X, Yc+Y, LineColor)	
		gfxdraw.pixel(screen, Xc-X, Yc+Y, LineColor)	
		gfxdraw.pixel(screen, Xc+X, Yc-Y, LineColor)	
		gfxdraw.pixel(screen, Xc-X, Yc-Y, LineColor)	
		gfxdraw.pixel(screen, Xc-Y, Yc+X, LineColor)	
		gfxdraw.pixel(screen, Xc+Y, Yc+X, LineColor)	
		gfxdraw.pixel(screen, Xc-Y, Yc-X, LineColor)
		gfxdraw.pixel(screen, Xc+Y, Yc-X, LineColor)

def BCircle(Xc, Yc, R):
	X = 0
	Y = R
	D = 3 - 2*R

	while Y >= X:
		X = X+1
		if D > 0:
			Y = Y-1
			D = D + 4*(X-Y) + 10
		else:
			D = D + 4*X + 6
		DrawCircle(Xc, Yc, X, Y)

	pygame.display.flip()

# Xc = input("Enter the x-coordinate of the origin Xc: ")
# Yc = input("Enter the y-coordinate of the origin Yc: ")
# R = input("Enter the radius of the circle: ")

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				(X, Y) = pygame.mouse.get_pos()
			if event.button == 4:
					R += 1
			if event.button == 5:
					R -= 1
	screen.fill(BGColor)
	Intro()
	BCircle(X, Y, R)
	pygame.display.flip()
pygame.quit()
sys.exit()