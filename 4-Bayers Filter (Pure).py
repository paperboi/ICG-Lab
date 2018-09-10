# #########################################
# BAYER'S FILTER AND DEMOSAICING ALGORITHM
# by Jeffrey Jacob, CED15I036
# #########################################

import pygame, itertools
from random import randint

def MakeBayerImage(Width, Height):
	if Width % 2 != 0:
		Width +=1

	RGRow = itertools.cycle([(255, 0, 0), (0, 255, 0)])
	GBRow = itertools.cycle([(0, 255, 0), (0, 0, 255)])
	SwapRows = [RGRow, GBRow]

	BayerImageList = []
	index = 0
	for i in range(Height):
		BayerImageListItem = list(itertools.islice(SwapRows[index], Width))
		BayerImageList.append(BayerImageListItem)
		index = (index + 1) % 2
	return BayerImageList


def MakeDemosaicedImage(BayerImage):
	DemosaicedBayerImageList = [[(0, 0, 0)] * len(BayerImage[0]) for row in range(len(BayerImage))]

	# Case 1: Red (Odd, Odd)
	for i in range(2, len(BayerImage) - 1, 2):
		for j in range(2, len(BayerImage[0]) - 1, 2):
			DemosaicedBayerImageList[i][j] = (
				BayerImage[i][j][0],
				(BayerImage[i+1][j][1] + BayerImage[i-1][j][1] + BayerImage[i][j+1][1] + BayerImage[i][j-1][1]) / 4, 
				(BayerImage[i+1][j+1][2] + BayerImage[i-1][j-1][2]) / 2
				)

	# Case 2: Blue (Even, Even)
	for i in range(1, len(BayerImage)-1, 2):
		for j in range(1, len(BayerImage[0]) - 1, 2):
			DemosaicedBayerImageList[i][j] = (
				(BayerImage[i+1][j+1][0] + BayerImage[i-1][j-1][0]) / 2,
				(BayerImage[i+1][j][1] + BayerImage[i-1][j][1] + BayerImage[i][j+1][1] + BayerImage[i][j-1][1]) / 4, 
				BayerImage[i][j][2]
				)

	# Case 3: Green (Even, Odd)
	for i in range(2, len(BayerImage) - 1, 2):
		for j in range(1, len(BayerImage[0]) - 1, 2):
			DemosaicedBayerImageList[i][j] = (
				(BayerImage[i][j+1][0] + BayerImage[i][j-1][0])/2,
				(BayerImage[i-1][j+1][1] + BayerImage[i-1][j-1][1] + BayerImage[i][j][1] + BayerImage[i+1][j+1][1] + BayerImage[i+1][j-1][1]) / 5, 
				(BayerImage[i+1][j][2] + BayerImage[i-1][j][2])/2
				)

	# Case 4: Green (Odd, Even)
	for i in range(1, len(BayerImage)-1, 2):
		for j in range(2, len(BayerImage[0]) - 1, 2):
			DemosaicedBayerImageList[i][j] = (
				(BayerImage[i+1][j][0] + BayerImage[i-1][j][0])/2,
				(BayerImage[i-1][j+1][1] + BayerImage[i-1][j-1][1] + BayerImage[i][j][1] + BayerImage[i+1][j+1][1] + BayerImage[i+1][j-1][1]) / 5, 
				(BayerImage[i][j+1][2] + BayerImage[i][j-1][2])/2
				)
	return DemosaicedBayerImageList

def DisplayIntro(Text, Color, Size, Position):
	DisplayFont = pygame.font.SysFont(None, Size)
	DisplayText = DisplayFont.render(Text, True, Color, (0, 0, 0))
	DisplayTextRect = DisplayText.get_rect()
	DisplayTextRect.centerx = screen.get_rect().centerx
	DisplayTextRect.centery = screen.get_rect().centery + Position
	screen.blit(DisplayText, DisplayTextRect)


def Intro():
	DisplayIntro("Bayer's Filter & Demosaicing Algorithm (Only 3 colors)", (0, 255, 0), 50, -100)
	DisplayIntro("Implementation by Jeffrey Jacob, CED15I036", (0, 255, 0), 35, -50)
	DisplayIntro("Controls", (255, 0, 0), 25, 0)
	DisplayIntro("LEFT/RIGHT buttons to shift between images:", (255, 255, 255), 25, 30)
	DisplayIntro("UP/DOWN buttons to zoom", (255, 255, 255), 25, 55)
	DisplayIntro("ESC to exit", (255, 255, 255), 25, 80)	 
	pygame.display.update()


def DisplayPage(Image, PixelWidth, PixelHeight):
	for i in range(len(Image)):
		for j in range(len(Image[0])):
			pygame.draw.rect(screen, Image[i][j], (i*PixelHeight, j*PixelWidth, PixelHeight, PixelWidth))


def DrawPage():
	if CurrentPage == 0:
		Intro()
	elif CurrentPage == 1:
		DisplayPage(BayerImage, PixelSize, PixelSize)
	elif CurrentPage == 2:
		DisplayPage(DemosaicedBayerImage, PixelSize, PixelSize)


pygame.init()
running = True
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Bayer's Filter & Demosaicing Algorithm (3 Colors)")
screen.fill((0, 0, 0))

PixelSize = 10
CurrentPage = 0
BayerImage = MakeBayerImage(500, 500)
DemosaicedBayerImage = MakeDemosaicedImage(BayerImage)

clock = pygame.time.Clock()
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_RIGHT and CurrentPage != 2:
					CurrentPage += 1
			if event.key == pygame.K_LEFT and CurrentPage != 0:
					CurrentPage -= 1
			if event.key == pygame.K_UP:
					PixelSize += 1
			if event.key == pygame.K_DOWN:
					PixelSize -= 1
	screen.fill((0, 0, 0))
	DrawPage()
	pygame.display.flip()
pygame.quit()