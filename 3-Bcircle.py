# #######################################
# BRESENHAM'S CIRCLE DRAWING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bresenham's Circle Drawing Algorithm")
screen.fill((0,0,0))
color = (255,167,55)

def DrawCircle(Xc, Yc, X, Y):
		gfxdraw.pixel(screen, Xc+X, Yc+Y, color)	
		gfxdraw.pixel(screen, Xc-X, Yc+Y, color)	
		gfxdraw.pixel(screen, Xc+X, Yc-Y, color)	
		gfxdraw.pixel(screen, Xc-X, Yc-Y, color)	
		gfxdraw.pixel(screen, Xc-Y, Yc+X, color)	
		gfxdraw.pixel(screen, Xc+Y, Yc+X, color)	
		gfxdraw.pixel(screen, Xc-Y, Yc-X, color)
		gfxdraw.pixel(screen, Xc+Y, Yc-X, color)

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
BCircle(200,100,50)

status = True
while status:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			status = False
pygame.quit()
sys.exit()