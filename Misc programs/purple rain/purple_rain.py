import pygame
import sys
from rain_obj import Rain
from pygame.sprite import Group


def run_sim():
	
	pygame.init()
	screen = pygame.display.set_mode((900,900))
	pygame.display.set_caption = ('Purple Rain')
	
	rain_drops = []
	for num in range(1300):
		rain = Rain(screen)
		rain_drops.append(rain)

	song_end = pygame.USEREVENT + 1
	pygame.mixer.music.set_endevent(song_end)
	pygame.mixer.music.load('purple_rain_audio.wav')
	pygame.mixer.music.play()
	
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
			elif event.type == song_end:
				sys.exit()
				print('R.I.P. Prince - 2017')
		
		screen.fill((230,230,250))
		
		for rain in rain_drops:
			rain.fall()
			rain.draw()
		
		
		pygame.display.flip()
		
		
run_sim()
					
	
