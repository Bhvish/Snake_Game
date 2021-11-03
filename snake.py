import pygame
import random
import math
import time

pygame.init()
height = 600
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

light = (207, 242, 252)
blue = (0, 0, 250)
clock = pygame.time.Clock()

scale = 20

player_x = random.choice(range(0, 580, 20))
player_y = random.choice(range(0, 580, 20))
player_height = 18
player_width = 18
player_x_change = 0
player_y_change = 0
player_color = (117, 65, 23)
playerx_position = []
playery_position = []

index_x = 0
index_y = 0
total = 1
score = 0

game_over = False

food_width = 17
food_height = 17
food_x = random.choice(range(0, 580, 20))
food_y = random.choice(range(0, 580, 20))
food_color = (255, 255, 255)


font = pygame.font.Font('freesansbold.ttf', 32)


def food(x, y, w, h, color):
	pygame.draw.rect(screen, color, (x, y, w, h))


def player(x, y, w, h, color):
	pygame.draw.rect(screen, color, (x, y, w, h))


def collision(x1, x2, y1, y2):
	distance = math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))
	if distance < 15:
		return True


loop = True

while loop:
	screen.fill((106, 196, 2))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and player_x_change != scale:
				player_x_change = -scale
				player_y_change = 0
			elif event.key == pygame.K_RIGHT and player_x_change != -scale:
				player_x_change = scale
				player_y_change = 0
			elif event.key == pygame.K_UP and player_y_change != scale:
				player_x_change = 0
				player_y_change = -scale
			elif event.key == pygame.K_DOWN and player_y_change != -scale:
				player_x_change = 0
				player_y_change = scale

	player_x += player_x_change
	player_y += player_y_change
	if player_x > 580:
		player_x_change = 0
		player_x = 580
		game_over = True
	elif player_x < 0:
		player_x_change = 0
		player_x = 0
		game_over = True
	if player_y > 580:
		player_y = 580
		player_y_change = 0
		game_over = True
	elif player_y < 0:
		pllayery = 0
		player_y_change = 0
		game_over = True

	if collision(player_x, food_x, player_y, food_y):
		food_x = random.choice(range(0, 580, 20))
		food_y = random.choice(range(0, 580, 20))
		total += 1
		score = total - 1
		if score % 10 == 0:
			text = font.render(f' {score}! ', True, light)
			textRect = text.get_rect()
			textRect.center = (width // 2, height // 2)
			screen.blit(text, textRect)
	if total > 1:
		for x in range(1, total):
			index_x = len(playerx_position)-x
			index_y = len(playery_position)-x
			player(playerx_position[index_x],
				playery_position[index_y], player_width, player_height, player_color)
			if collision(player_x, playerx_position[index_x], player_y, playery_position[index_y]):
				game_over = True
	
	if game_over is True:
		time.sleep(2)
		pygame.mixer.music.stop()

		text = font.render(f'GAME OVER!  SCORE: {score} ', True, blue)
		textRect = text.get_rect()
		textRect.center = (width // 2, height // 2)
		screen.blit(text, textRect)
		player_y_change = 0
		player_x_change = 0
	playerx_position.append(player_x)
	playery_position.append(player_y)

	food(food_x, food_y, food_width, food_height, food_color)
	player(player_x, player_y, player_width, player_height, player_color)
	pygame.display.update()
	clock.tick(5)
