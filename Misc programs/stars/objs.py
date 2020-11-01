import pygame
from pygame.sprite import Sprite

class Stars(Sprite):

	def __init__(self, screen):
		"""Initializes star and staring position"""
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('images/star_two.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
