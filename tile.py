import config, pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self,type):
		pygame.sprite.Sprite.__init__(self)
		self.c = config.Config()
		self.type = type

		self.bomb = None
		self.powerup = None

		self.setPowerup()
		self.setAttributes()
	
	# RFCT
	def setPowerup(self):
		if self.type == self.c.BOMB_UP:
			self.powerup = self.c.BOMB_UP
			self.type = self.c.BRICK
		elif self.type == self.c.POWER_UP:
			self.powerup = self.c.POWER_UP
			self.type = self.c.BRICK

	def isPowerUp(self):
		return self.type == self.c.POWER_UP or self.type == self.c.BOMB_UP
		return self.type != self.c.GROUND & self.type != self.c.BRICK & self.type != self.c.WALL

	def setAttributes(self):
		if self.type == self.c.GROUND:
			self.passable = True 
			self.destroyable = False
		elif self.type == self.c.BRICK:
			self.passable = False
			self.destroyable = True
		elif self.type == self.c.WALL:
			self.passable = False
			self.destroyable = False
		elif self.type == self.c.BOMB_UP or self.type == self.c.POWER_UP:
			self.passable = True
			self.destroyable = True

		self.image = pygame.image.load(self.c.IMAGE_PATH + "tiles/" + str(self.type) + ".png").convert()
	
	def destroy(self):
		if self.powerup != None:
			self.type = self.powerup
			self.powerup = None
		else:
			self.type = self.c.GROUND
		self.setAttributes()
	
	# RFCT
	def canBombPass(self):
		if self.type == self.c.BOMB_UP or self.type == self.c.POWER_UP:
			return False
		return self.passable & (self.bomb == None)

	def canPass(self):
		return self.passable & (self.bomb == None)

	def getBackground(self):
		return self.image

	def getImage(self):
		if self.bomb != None:
			return self.bomb.image
		return self.image

	def __str__(self):
		return str(self.type)
