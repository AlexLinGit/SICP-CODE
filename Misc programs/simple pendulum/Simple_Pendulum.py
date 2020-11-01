import pygame
import sys
import math

def main_p():

	#screen properties
	pygame.init()
	screen_size = (1000, 900)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Simple Pendulum")
	color = (255,255,255)

	#pendulum settings
	pend_color = (0,0,0)
	rad = int(8)
	bob_rad = int(16)
	bob_color = (120, 125, 41)

	x, y = screen_size
	x1 = int(x/2)
	y1 = int(y*.20)

	#top of pendulum
	point1 = (x1, y1)

	#pendulum properties
	g = 0.00000001
	pi = 3.14159265358979323846264338327950288419716939937510284
	theta = pi/2
	L = 300

	#some calculations
	t = (2*pi)*math.sqrt((L/g))
	d = (2*pi*L)
	r = d/t


	#pendulum properties
	aVel = r/60
	aAcc = 9.81
#	mass = 

	

	print(str(t) + " " + str(r) + " " + str(d))


	def bob_new_pos():
		bob_x = x1 + L * math.sin(theta)
		bob_y = y1 + L * math.cos(theta)
		return bob_x, bob_y

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

		screen.fill(color)

		#top of pendulum
		pygame.draw.circle(screen, pend_color, point1, rad)

		#bob
		bob_x, bob_y = bob_new_pos()
		bob_pos = (int(bob_x), int(bob_y))
		pygame.draw.circle(screen, bob_color, bob_pos, bob_rad, 0)

		#pendulum arm
		pygame.draw.line(screen, pend_color, point1, bob_pos, int(3))


#		aAcc = -g * math.sin(theta)
		theta += aVel
		aVel += aAcc

		aVel *= 0.2

		print(aVel)
		print("BOB" + str(aAcc))


		pygame.display.flip()


main_p()