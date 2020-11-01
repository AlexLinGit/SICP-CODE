import pygame
from objs import Stars
from random import randint


def create_stars(screen, settings, star_w, star_h, stars):
	"""Creates stars"""
	star = Stars(screen)
	
	num_stars = int(1000/star_w)
	num_rows = int(1000/star_h)
	
	one = randint(0, num_rows)
	two = randint(0, num_stars)
	
	for on in range(one):
		for tw in range(two):
			star = Stars(screen)
			star_w = star.rect.width
			star.x = (randint(-100, 100) * star_w) 
			star.rect.x = star.x
			star.rect.y = (randint(-100, 100) * star.rect.height)
			
			star.add(stars)
	
