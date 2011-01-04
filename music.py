import pygame, random, config

class Music:
	def __init__(self):
		self.c = config.Config()

	def playMusic(self, mode):
		if mode == self.c.SINGLE:
			music = "leveltheme.mid"
	#		music_list = ["leveltheme.mid"]
	#		music = music_list[random.randint(0,len(music_list)-1)]
		elif mode == self.c.MULTI:
			music = "multiplayer.mid"

		pygame.mixer.music.load(self.c.AUDIO_PATH + music)
		pygame.mixer.music.play(-1)
	
	def playSound(self, type):
		if type == "bomb":
			sound = "Blast_02.wav"
		elif type == "power up":
			sound = "Ping_01.wav"
		elif type == "victory":
			sound = "stage-clear.mid"

		pygame.mixer.music.load(self.c.AUDIO_PATH + sound)
		pygame.mixer.music.play()
