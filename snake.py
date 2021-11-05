import pygame
import random
import math
import time
import sys

# difficulty levels
easy = 5
medium = 8
hard = 13
very_hard = 18
impossible = 25
difficulty = easy

pygame.init()
height = 600
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

light_blue = (207, 242, 252)
blue = (0, 0, 250)
black = pygame.Color(0, 0, 0)
green = (106, 196, 2)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
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

	
def gameOver():
    font = pygame.font.Font('freesansbold.ttf', 90)
    game_over_surface = font.render('YOU DIED!', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    showScore(0, red, 'times', 30)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def showScore(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)
    screen.blit(score_surface, score_rect)



loop = True

while loop:
	screen.fill((106, 196, 2))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a') and player_x_change != scale:
				player_x_change = -scale
				player_y_change = 0
			elif event.key == pygame.K_RIGHT or event.key == ord('d') and player_x_change != -scale:
				player_x_change = scale
				player_y_change = 0
			elif event.key == pygame.K_UP or event.key == ord('w') and player_y_change != scale:
				player_x_change = 0
				player_y_change = -scale
			elif event.key == pygame.K_DOWN or event.key == ord('s') and player_y_change != -scale:
				player_x_change = 0
				player_y_change = scale
			 elif event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

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
		showScore(1, white, 'consolas', 20)
	if total > 1:
		for x in range(1, total):
			index_x = len(playerx_position)-x
			index_y = len(playery_position)-x
			player(playerx_position[index_x],
				playery_position[index_y], player_width, player_height, player_color)
			if collision(player_x, playerx_position[index_x], player_y, playery_position[index_y]):
				gameOver()
	
	playerx_position.append(player_x)
	playery_position.append(player_y)

	food(food_x, food_y, food_width, food_height, food_color)
	player(player_x, player_y, player_width, player_height, player_color)
	pygame.display.update()
	clock.tick(difficulty)
