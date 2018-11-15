import pygame, math

pygame.init()
running = True

BGColor = (4, 15, 15)
TextColor1 = (46, 233, 131)
TextColor2 = (242, 226, 186)
TextColor3 = (252, 255, 252)
TextColor4 = (43, 168, 74)
LineColor = (255, 229, 74)

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Levy's C Curve")
screen.fill(BGColor)

(X, Y) = (300.0, 300.0)
L = 300
A = 45
N = 0

def DisplayIntro(Text, Color, Size, XPos, YPos):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, BGColor)
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = XPos
	DisplayTextRect.centery = YPos
	screen.blit(DisplayText, DisplayTextRect)

def Intro():
	DisplayIntro("Levy's C Curve", TextColor1, 40, 1000, 30)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", TextColor2, 25, 1000, 60)
	DisplayIntro("Drag with the left mouse button to change the start and end points", TextColor3, 22, 1000, 110)
	DisplayIntro("UP/DOWN buttons to change the number of iterations", TextColor3, 22, 1000, 130)
	DisplayIntro("ESC to exit", TextColor3, 22, 1000, 150)
	DisplayIntro("Start point = (" + str(X) + ", " + str(Y) + ")", TextColor4, 22, 1000, 190)	 
	DisplayIntro("End point = (" + str(X + L * math.cos(math.radians(A))) + ", " + str(Y + L * math.sin(math.radians(A))) + ")", TextColor4, 22, 1000, 210)	 
	DisplayIntro("Length = " + str(L), TextColor4, 22, 1000, 230)	 
	DisplayIntro("Angle = " + str(A), TextColor4, 22, 1000, 250)	 
	DisplayIntro("Number of iterations = " + str(N), TextColor4, 22, 1000, 270)	 

def CCurve((XPos, YPos), Length, Angle, Iteration):
	alpha = Angle
	if Iteration > 0:
		Length = Length / math.sqrt(2)
		CCurve((XPos, YPos), Length, alpha + 45, Iteration - 1)
		XPos += (Length * math.cos(math.radians(alpha + 45)))
		YPos += Length * math.sin(math.radians(alpha + 45))
		CCurve((XPos, YPos), Length, alpha - 45, Iteration - 1)
	else:
		pygame.draw.line(screen, LineColor, (XPos, YPos), (XPos + Length * math.cos(math.radians(alpha)), YPos + Length * math.sin(math.radians(alpha))), 2)

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
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				(X, Y) = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				(X1, Y1) = pygame.mouse.get_pos()
				L = math.sqrt((X1 - X) ** 2 + (Y1 - Y) ** 2)
				A = math.degrees(math.atan2((Y1 - Y), (X1 - X)))
	screen.fill(BGColor)
	Intro()
	CCurve((X, Y), L, A, N)
	pygame.display.flip()
pygame.quit()