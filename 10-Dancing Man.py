import sys, pygame, random as rndm, time
import numpy as np
import math

pygame.init()
pygame.font.init()

BGColor = (4, 15, 15)
LineColor = (255, 229, 74)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((0,0))
surf=pygame.display.get_surface()
screen.fill(BGColor)

y = 0
dire = 1
running = 1
HandLeftX = 170
HandRighttX = 330

LegLeftY = 500
LegRighttY = 500

Leg = 0
LegLeft = 0
LegRight = 0

shy = 350

pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
	screen.fill(BGColor)
	
	# Face
	pygame.draw.circle(screen, LineColor, (250,250), 50, 1)
	
	# Body
	pygame.draw.line(screen, LineColor, (250, 300),(250, 450))

	# Arms
	pygame.draw.line(screen, LineColor, (250, shy),(HandLeftX, 300))
	pygame.draw.line(screen, LineColor, (250, shy),(HandRighttX, 300))

	# Hands
	pygame.draw.line(screen, LineColor,(HandLeftX, 300),(HandLeftX - 30, 300))
	pygame.draw.line(screen, LineColor,(HandRighttX, 300),(HandRighttX + 30, 300))

	# Legs
	pygame.draw.line(screen, LineColor, (250, 450),(200, LegLeftY))
	pygame.draw.line(screen, LineColor, (250, 450),(300, LegRighttY))

	if dire == 1:
		HandLeftX +=0.5
		HandRighttX +=0.5
	elif dire == 0:
		HandLeftX -= 0.5
		HandRighttX -=0.5

	if HandLeftX > 200:
		dire = 0
	elif HandLeftX < 140:
		dire = 1
	
	if Leg == 0:
		if LegLeft == 1:
			LegLeftY += 0.5
		elif LegLeft == 0:
			LegLeftY -= 0.5
		if LegLeftY > 510:
			LegLeft = 0
			Leg = 1			
		elif LegLeftY < 470:
			LegLeft = 1
	elif Leg == 1:
		if LegRight == 1:
			LegRighttY += 0.5
		elif LegRight == 0:
			LegRighttY -= 0.5
		if LegRighttY > 510:
			LegRight = 0
			Leg = 0
		elif LegRighttY < 470:
			LegRight = 1
	pygame.display.flip()