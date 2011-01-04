import sys, pygame, config

class Highscore:
	def __init__(self):
		self.c = config.Config()
		self.reloadScoreData()
	
	def reloadScoreData(self):
		file = open(self.c.HIGHSCORES_PATH,"r").readlines()
		
		self.scores = []
		row = 0
		for line in file:
			self.scores.append(int(line))
	
		# sort scores
		self.scores.sort()
		self.scores.reverse()
	
	def addScore(self,score):
		file = open(self.c.HIGHSCORES_PATH,"a")
		file.write(str(score)+"\n")
	
	def displayScore(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.c.WIDTH,self.c.HEIGHT))
		self.clearBackground()

		indx = 1
		self.printText("Highscores",(375,40))
		for score in self.scores:
			self.printText("%d) %d" % (indx,score),(40,75+25*indx))
			indx += 1
		pygame.display.flip()
		
		exit = False
		while not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
				elif event.type == pygame.MOUSEBUTTONDOWN:
					exit = True

	# RFCT - this method is in every class, make it a global
	def clearBackground(self):
		bg = pygame.Surface(self.screen.get_size())
		bg = bg.convert()
		bg.fill((0,0,0))
		self.screen.blit(bg,(0,0))

	# RFCT - this method is also in Game.py, make it global
	def printText(self,text,point):
	#	font = pygame.font.SysFont("resources/fonts/Lucida Console",26)
		font = pygame.font.Font("lucida.ttf",20)
	#	font = pygame.font.SysFont(pygame.font.get_default_font(),26)
		#font = pygame.font.Font(None,24)
		label = font.render(str(text)+'  ', True, (255,255, 255), (0, 0, 0))
		textRect = label.get_rect()
		textRect.x = point[0] 
		textRect.y = point[1]
		self.screen.blit(label, textRect)
				
	def printScores(self):
		indx = 1
		for score in self.scores:
			print "%d) %d" % (indx,score)
			indx += 1

# DEBUG Purposes
if __name__ == "__main__":
	h = Highscore()
	#h.addScore(1000)
	#h.reloadScoreData()
	#h.printScores()
	h.displayScore()
	raw_input("quit")
