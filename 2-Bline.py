# #######################################
# BRESENHAM'S LINE DRAWING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")
screen.fill((0,0,0))
color = (255,167,55)

def BLine(X1, Y1, X2, Y2):
	# X1 = input("Enter the x-coordinate of the start point X1: ")
	# Y1 = input("Enter the y-coordinate of the start point Y1: ")
	# X2 = input("Enter the x-coordinate of the end point X2: ")
	# Y2 = input("Enter the y-coordinate of the end point Y2: ")

	dX = X2-X1
	dY = Y2-Y1
	P0 = 2*dY-dX
	Pk = P0
	Xk = X1
	Yk = Y1

	while Xk <= X2:
		print(Xk, Yk)
		gfxdraw.pixel(screen, Xk, 400-Yk, color)
		Xk = Xk+1
		if Pk < 0:
			Yk = Yk
			Pk = Pk + 2*dY
		elif Pk>0:
			Yk = Yk+1
			Pk = Pk + 2*dY -2*dX

	pygame.display.flip()

BLine(145,55,350,387)

status = True
while status:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			status = False
pygame.quit()
sys.exit()