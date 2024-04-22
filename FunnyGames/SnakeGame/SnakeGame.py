import pygame as py 
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = ( TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda : [randrange(*RANGE), randrange(*RANGE)]
snake = py.Rect([0,0, TILE_SIZE-2, TILE_SIZE-2])
snake.center = get_random_position()
screen = py.display.set_mode([WINDOW]*2)
time_clock = py.time.Clock()
time, time_step = 0, 100 # Speed control for my snake 
dirs = {py.K_w:1, py.K_a:1, py.K_d:1, py.K_s:1}
length = 1 
segments = [snake.copy()]
snake_dir = (0,0) # These values shows the snake x, y location cordinates on every movement
food = snake.copy()
food.center = get_random_position()

# Using W-A-S-D keys to change the snake direction in the screen 
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        elif event.type == py.KEYDOWN: 
             if event.key == py.K_w and dirs[py.K_w]:
                 snake_dir = (0, -TILE_SIZE)
             if event.key == py.K_s and dirs[py.K_s]:
                 snake_dir = (0, TILE_SIZE)
             if event.key == py.K_a and dirs[py.K_a]:
                 snake_dir = (-TILE_SIZE, 0)
             if event.key == py.K_d and dirs[py.K_d]:
                 snake_dir = (TILE_SIZE, 0)
            
            
    screen.fill("black")
     # Draw snake
    [py.draw.rect(screen, "green", segments) for segment in segments]
    
    # Check borders and selfeating
    self_eating = py.Rect.collidelist(snake, segments[:-1])!= -1
    if snake.right > WINDOW or snake.left < 0 or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]
    # Draw food 
    py.draw.rect(screen, "red",food) 
    # Check food position in window
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    # Move snake 
    time_now = py.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    py.display.flip()
    py.time.Clock.tick(60)
