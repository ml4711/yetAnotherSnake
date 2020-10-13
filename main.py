import pygame

class cube(object):
	pass

class snake(object):
	def __init__(self, color, pos):
		pass

	def move(self):
		pass

	def reset(self, pos):
		pass

	def addCube(self):
		pass

	def draw(self, surface):
		pass

def drawGrid(w, rows, surface):
	sizeBtwn = w // rows

	x = 0
	y = 0
	for l in range(rows):
		x = x + sizeBtwn
		y = y + sizeBtwn

		pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
		pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
	global rows, width
	surface.fill((0,0,0))
	drawGrid(width, rows, surface)
	pygame.display.update()

def main():
	global width, rows
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	s = snake((255,0,0), (10,10))

	flag = True

	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(win)

	pass

main()