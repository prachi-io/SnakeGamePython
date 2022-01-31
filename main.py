# 1) Install pygame
# 2) Import
import pygame , random

# 3) Pygame has many modules we need to initialize them
from pygame.examples.eventlist import font

pygame.init()

# 4) set width and height of the screen
w , h = 500 , 500

# 5) Set screen
screen = pygame.display.set_mode((w,h))

# 7) We need to set the caption name
pygame.display.set_caption("SNAKE GAME")

# 12) Making a snake
snake = [[300,300],[320,300],[340,300],[360,300]]
def draw_snake(screen , snake) :
    for pos in snake :
        pygame.draw.circle(screen, (240, 252, 3), pos, 10)

# 13) specifying direction for snake
step = 20
left = (-step,0)
right = (step,0)
up = (0,-step)
down = (0,+step)
direction = left

# 15) control the speed of snake
FPS = 60
clock = pygame.time.Clock()

# 17) Apple
apple = [200,200]

# 19) score , margin and radius in snake eat apple detect
score = 0
margin = 10
r = 10

# 16) timer ki loop 5 baar chale tabsnake ak baar chale
timer = 0

# 23) score on screen
font = pygame.font.SysFont("Arial", 32, True)
def display_score(screen, score):
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (15,15))

# 6) Screen ko rok ke rakhna h
run = True
while run :

    # 8) Change the color of background
    screen.fill((3, 165, 252))

    # 15) control the speed of snake
    clock.tick(FPS)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            print("QUIT")
            run = False

        # 11) control circle using keys
        # 13) specifying direction for snake
        if event.type == pygame.KEYDOWN :
            # 24) Restriction in direction
            if event.key == pygame.K_UP and direction != down:
                direction = up
            elif event.key == pygame.K_DOWN and direction != up:
                direction = down
            elif event.key == pygame.K_LEFT and direction != right:
                direction = left
            elif event.key == pygame.K_RIGHT and direction != left:
                direction = right

    # 16) timer ki loop 5 baar chale tab snake ak baar chale
    timer += 1
    if timer == 5 :
        # 14) Snake Movement
        snake = [[snake[0][0] + direction[0], snake[0][1] + direction[1]]] + snake[:-1]
        timer = 0

    # 25) snake uper se gaaya to niche se aaega
    if snake[0][1] < 0 :
        snake[0][1] = h
    if snake[0][0] < 0 :
        snake[0][0] = w
    if snake[0][1] > h :
        snake[0][1] = 0
    if snake[0][0] > w :
        snake[0][0] = 0

    # 19) Snake eats apple detect
    if snake[0] == apple :
        score = score + 1
        if score % 5 == 0 :
            FPS = FPS + 0.2 * FPS
        # 20) making apple multiple of step
        apple[0] = (random.randint(r+margin , w - r - margin) // step ) * step
        apple[1] = (random.randint(r+margin , w - r - margin) // step ) * step
        # 21) size of snake increases
        snake.append(snake[-1])
        print(score)

    # 22) game over
    for pos in snake[1:] :
        if snake[0] == pos :
            print("gameover")
            run = False

    # 12) calling draw sanke function
    draw_snake(screen , snake)

    # 18) Apple - drawing circle
    pygame.draw.circle(screen , (224, 63, 52) , apple , 10)

    # 23) Score on screen
    display_score(screen , score)

    # 9) Refresh our screen
    pygame.display.update()


