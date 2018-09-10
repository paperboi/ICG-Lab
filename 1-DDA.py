# #######################################
# DDA ALGORITHM
# by Jeffrey Jacob, CED15I036
# #######################################

import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Digital Differential Algorithm")
screen.fill((0,0,0))
color = (255,167,55)

def DDA(X1, Y1, X2, Y2):
	# X1 = input("Enter the x-coordinate of the start point X1: ")
	# Y1 = input("Enter the y-coordinate of the start point Y1: ")
	# X2 = input("Enter the x-coordinate of the end point X2: ")
	# Y2 = input("Enter the y-coordinate of the end point Y2: ")

	Xk = X1
	Yk = Y1

	M = float((Y2-Y1)/(X2-X1))
	print M

	while Yk <= Y2:
		print(int(Xk), int(round(Yk)))
		gfxdraw.pixel(screen, int(round(Xk)), int(400-round(Yk)), color)
		Xk = Xk + 1
		Yk = Yk + M

	pygame.display.flip()
	
DDA(145.0,55.0,350.0,387.0)
# DDA(0.0,1.0,240.0,240.0)
# DDA(52.0,50.0,0.0,0.0)

status = True
while status:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			status = False
pygame.quit()
sys.exit()