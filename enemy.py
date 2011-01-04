import pygame, character, random

# RFCT NEEDED
class Enemy(character.Character):
	def __init__(self, name, imageName, point):
		character.Character.__init__(self, name, "enemies/"+imageName, point)
		self.instance_of = 'enemy'

	def nextMove(self):
		ary = [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]
		return self.movement(ary[int(random.randrange(0,4))])
