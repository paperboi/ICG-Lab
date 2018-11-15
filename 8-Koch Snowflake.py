import pygame, math
from random import randint

pygame.init()
running = True

BGColor = (4, 15, 15)
TextColor1 = (46, 233, 131)
TextColor2 = (242, 226, 186)
TextColor3 = (252, 255, 252)
TextColor4 = (43, 168, 74)
LineColor = (255, 229, 74)

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Koch Snowflake")
screen.fill(BGColor)

Length = 400

X1 = screen.get_width() / 2
Y1 = screen.get_height() / 2 - Length*0.5
X2 = X1 + Length*(math.cos(math.radians(60)))
Y2 = Y1 + Length*(math.sin(math.radians(60)))
X3 = X1 - Length*(math.cos(math.radians(60)))
Y3 = Y1 + Length*(math.sin(math.radians(60)))

N = 0


def DisplayIntro(Text, Color, Size, XPos, YPos):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, BGColor)
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = XPos
	DisplayTextRect.centery = YPos
	screen.blit(DisplayText, DisplayTextRect)

def Intro():
	DisplayIntro("Koch Snowflake", TextColor1, 40, 1000, 30)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", TextColor2, 25, 1000, 60)
	DisplayIntro("UP/DOWN buttons to change the number of iterations", TextColor3, 22, 1000, 110)
	DisplayIntro("ESC to exit", TextColor3, 22, 1000, 130)
	DisplayIntro("Number of iterations = " + str(N), TextColor4, 22, 1000, 170)	 

def KCurve((XPos1, YPos1), (XPos2, YPos2), Iteration):
	alpha = 60
	if Iteration > 0:
		(XPos3, YPos3) = ((2*XPos1 + XPos2) / 3, (2*YPos1 + YPos2) / 3)
		(XPos5, YPos5) = ((2*XPos2 + XPos1) / 3, (2*YPos2 + YPos1) / 3)
		(XPos4, YPos4) = (XPos3 + (XPos5 - XPos3) * math.cos(math.radians(alpha)) + (YPos5 - YPos3) * math.sin(math.radians(alpha)), YPos3 - (XPos5 - XPos3) * math.sin(math.radians(alpha)) + (YPos5 - YPos3) * math.cos(math.radians(alpha)))

		KCurve((XPos1, YPos1), (XPos3, YPos3), Iteration - 1)
		KCurve((XPos3, YPos3), (XPos4, YPos4), Iteration - 1)
		KCurve((XPos4, YPos4), (XPos5, YPos5), Iteration - 1)
		KCurve((XPos5, YPos5), (XPos2, YPos2), Iteration - 1)

	else:
		pygame.draw.line(screen, LineColor, (XPos1, YPos1), (XPos2, YPos2), 2)

def KSnowflake((XPos1, YPos1), (XPos2, YPos2), (XPos3, YPos3), Iteration):
	KCurve((XPos1, YPos1), (XPos2, YPos2), Iteration)
	KCurve((XPos2, YPos2), (XPos3, YPos3), Iteration)
	KCurve((XPos3, YPos3), (XPos1, YPos1), Iteration)



clock = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_UP:
				N += 1
			if event.key == pygame.K_DOWN and N != 0:
				N -= 1

	screen.fill(BGColor)
	Intro()
	KSnowflake((X1, Y1), (X2, Y2), (X3, Y3), N)
	pygame.display.flip()
pygame.quit()