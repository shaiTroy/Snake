import pygame
import time
from classes import Snake, Apple
import csv


snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Custom Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

fruit_spawn = True
apple = Apple(window_x, window_y)

#create the snake
snake = Snake()
change_to = snake.direction

score = 0

def print_score_to_csv(score):
    with open('leaderboard.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ai', score])

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    print_score_to_csv(score)
    quit()

def calculate_distance(snake_position, food_position):
    return abs(snake_position[0] - food_position[0]) + abs(snake_position[1] - food_position[1])

def is_valid_move(snake, direction, window_x, window_y):
    new_position = list(snake.position)
    if direction == 'UP':
        new_position[1] -= 10
    elif direction == 'DOWN':
        new_position[1] += 10
    elif direction == 'LEFT':
        new_position[0] -= 10
    elif direction == 'RIGHT':
        new_position[0] += 10
    
    if new_position[0] < 0 or new_position[0] >= window_x or new_position[1] < 0 or new_position[1] >= window_y:
        return False
    if new_position in snake.body:
        return False
    return True

def get_best_direction(snake, food_position, window_x, window_y):
    directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    best_direction = None
    min_distance = float('inf')
    
    for direction in directions:
        if is_valid_move(snake, direction, window_x, window_y):
            new_position = list(snake.position)
            if direction == 'UP':
                new_position[1] -= 10
            elif direction == 'DOWN':
                new_position[1] += 10
            elif direction == 'LEFT':
                new_position[0] -= 10
            elif direction == 'RIGHT':
                new_position[0] += 10
            
            distance = calculate_distance(new_position, food_position)
            if distance < min_distance:
                min_distance = distance
                best_direction = direction
    return best_direction

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    change_to = get_best_direction(snake, apple.position, window_x, window_y)
    if change_to == 'UP' and snake.direction != 'DOWN':
        snake.direction = 'UP'
    if change_to == 'DOWN' and snake.direction != 'UP':
        snake.direction = 'DOWN'
    if change_to == 'LEFT' and snake.direction != 'RIGHT':
        snake.direction = 'LEFT'
    if change_to == 'RIGHT' and snake.direction != 'LEFT':
        snake.direction = 'RIGHT'

    # Moving the snake
    if snake.direction == 'UP':
        snake.position[1] -= 10
    if snake.direction == 'DOWN':
        snake.position[1] += 10
    if snake.direction == 'LEFT':
        snake.position[0] -= 10
    if snake.direction == 'RIGHT':
        snake.position[0] += 10

    # Snake body growing mechanism
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == apple.position[0] and snake.position[1] == apple.position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake.body.pop()
        
    if not fruit_spawn:
        apple.randomApple()
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake.body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(apple.position[0], apple.position[1], 10, 10))

    # Game Over conditions
    if snake.position[0] < 0 or snake.position[0] > window_x-10:
        game_over()
    if snake.position[1] < 0 or snake.position[1] > window_y-10:
        game_over()

    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            game_over()

    # display score
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)