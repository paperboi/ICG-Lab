# #########################################
# BAYER'S FILTER AND DEMOSAICING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #########################################

import pygame

pygame.init()
running = True

SkyBlue = (181, 216, 255)
White = (255, 255, 255)
DBrown = (150, 120, 96)
LBrown = (224, 180, 119)
Grey = (142, 145, 150)

screen = pygame.display.set_mode((660, 330))

pygame.display.set_caption("IIITDM Gate")

screen.fill(SkyBlue)

pygame.draw.rect(screen, LBrown, (0, 250, 660, 130))

pygame.draw.rect(screen, White, (30, 100, 600, 30))

pygame.draw.rect(screen, DBrown, (315, 130, 30, 180))

pygame.draw.rect(screen, White, (315, 200, 30, 15))

pygame.draw.rect(screen, White, (50, 130, 15, 180))

pygame.draw.rect(screen, White, (595, 130, 15, 180))

pygame.draw.rect(screen, White, (100, 130, 35, 180))

pygame.draw.rect(screen, White, (525, 130, 35, 180))

pygame.draw.rect(screen, White, (0, 200, 150, 110))

pygame.draw.rect(screen, White, (510, 200, 150, 110))

pygame.draw.rect(screen, DBrown, (0, 205, 75, 95))

pygame.draw.rect(screen, DBrown, (585, 205, 75, 95))

# pygame.draw.rect(screen, SkyBlue, (70, 220, 50, 80))

pygame.draw.rect(screen, SkyBlue, (525, 220, 30, 80))

pygame.draw.rect(screen, SkyBlue, (105, 220, 30, 80))

Font = pygame.font.SysFont(None, 21)
Text = Font.render('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY DESIGN AND MANUFACTURING', True, (0, 0, 0))
RectText = Text.get_rect()
RectText.centerx = screen.get_rect().centerx
RectText.centery = 115
screen.blit(Text, RectText)

# pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
	pygame.display.flip()
pygame.quit()