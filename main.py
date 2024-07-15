import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("Snake")

head = [300, 300]
body = [[300, 300], [280, 300], [260, 300], [240, 300], [220, 300]]


direction = "RIGHT"

fruit = []
def spawn_fruit():
    while True:
        fruit_position = [random.randrange(1, (WIDTH // 20)) * 20, random.randrange(1, (HEIGHT // 20)) * 20]
        if fruit_position not in body:
            fruit = fruit_position
            return fruit

running = True
while running:
    while fruit == []:
        fruit = spawn_fruit()

    change_to = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        head[1] -= 20
    if direction == 'DOWN':
        head[1] += 20
    if direction == 'LEFT':
        head[0] -= 20
    if direction == 'RIGHT':
        head[0] += 20

    body.insert(0, list(head))

    screen.fill((0,0,0))

    if head[0] < 0 or head[0] > WIDTH - 20:
        running = False
    if head[1] < 0 or head[1] > HEIGHT - 20:
        running = False

    if fruit == head:
        fruit = []
    elif fruit != []:
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(fruit[0], fruit[1], 20, 20))
        body.pop()


    if head in body[1:]:
        running = False


    for pos in body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(head[0], head[1], 20, 20))




    pygame.display.flip()
    pygame.time.Clock().tick(8)