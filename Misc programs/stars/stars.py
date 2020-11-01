import pygame
from settings import Settings
import sys
from objs import Stars
import star_functions as sf
from pygame.sprite import Group

def run_stars():

	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(settings.screen_lw)
	pygame.display.set_caption('Stars')
	star = Stars(screen)
	stars = Group()
	sf.create_stars(screen, settings, star.rect.width, star.rect.height,
		stars)
	print(len(stars))
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
		
		screen.fill(settings.bg_color)
		stars.draw(screen)
		pygame.display.flip()


run_stars()
