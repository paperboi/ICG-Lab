import pygame, math

pygame.init()
running = True

BGColor = (4, 15, 15)
LineColor = (255, 229, 74)

LineWidth = 2

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Shapes")
screen.fill(BGColor)

Radius = 200

def DrawShapes():
	pygame.draw.circle(screen, LineColor, (screen.get_width() / 2, screen.get_height() / 2), Radius, LineWidth)

	X = screen.get_width()/2 - (2 * Radius * (1 / math.sqrt(2))) / 2
	Y = screen.get_height()/2 - (2 * Radius * (1 / math.sqrt(2))) / 2
	Rect = [X, Y, 2 * Radius * (1 / math.sqrt(2)), 2 * Radius * (1 / math.sqrt(2))]
	pygame.draw.rect(screen, LineColor, Rect, LineWidth)

	Radius2 = (2 * Radius * (1 / math.sqrt(2))) / 2
	pygame.draw.circle(screen, LineColor, (screen.get_width()/2, screen.get_height()/2), int(Radius2), LineWidth)

	Ax = screen.get_width() / 2
	Ay = screen.get_height() / 2 - Radius2
	Bx = Ax + Radius2*(math.cos(math.radians(60)))
	By = Ay + Radius2*(math.sin(math.radians(60)))
	Cx = Ax - Radius2*(math.cos(math.radians(60)))
	Cy = Ay + Radius2*(math.sin(math.radians(60)))

	print (Ax, Ay), (Bx, By), (Cx, Cy)

	pygame.draw.line(screen, LineColor, (Ax, Ay), (Bx, By), LineWidth)
	pygame.draw.line(screen, LineColor, (Bx, By), (Cx, Cy), LineWidth)
	pygame.draw.line(screen, LineColor, (Cx, Cy), (Ax, Ay), LineWidth)

	print screen.get_width()/2, screen.get_height()/2

DrawShapes()
clock = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
	pygame.display.flip()
pygame.quit()