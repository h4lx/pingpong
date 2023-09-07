import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
BG_COLOR = (0, 0, 0)
BALL_COLOR = (255, 255, 255)
PAD_COLOR = (255, 255, 255)

BALL_SPEED = 0.5
PAD_SPEED = 10
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

left_pad_y = (HEIGHT - PAD_HEIGHT) // 2
right_pad_y = (HEIGHT - PAD_HEIGHT) // 2
left_pad_dy = 0
right_pad_dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_pad_dy = -PAD_SPEED
            elif event.key == pygame.K_s:
                left_pad_dy = PAD_SPEED
            elif event.key == pygame.K_UP:
                right_pad_dy = -PAD_SPEED
            elif event.key == pygame.K_DOWN:
                right_pad_dy = PAD_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_pad_dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_pad_dy = 0

    left_pad_y += left_pad_dy
    right_pad_y += right_pad_dy

    if left_pad_y < 0:
        left_pad_y = 0
    if left_pad_y > HEIGHT - PAD_HEIGHT:
        left_pad_y = HEIGHT - PAD_HEIGHT
    if right_pad_y < 0:
        right_pad_y = 0
    if right_pad_y > HEIGHT - PAD_HEIGHT:
        right_pad_y = HEIGHT - PAD_HEIGHT

    ball_x += ball_dx
    ball_y += ball_dy

    if (ball_x - BALL_RADIUS < PAD_WIDTH and left_pad_y < ball_y < left_pad_y + PAD_HEIGHT) or \
            (ball_x + BALL_RADIUS > WIDTH - PAD_WIDTH and right_pad_y < ball_y < right_pad_y + PAD_HEIGHT):
        ball_dx = -ball_dx

    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_dy = -ball_dy

    if ball_x < 0 or ball_x > WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = -ball_dx
        ball_dy = -ball_dy

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PAD_COLOR, (0, left_pad_y, PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(screen, PAD_COLOR, (WIDTH - PAD_WIDTH, right_pad_y, PAD_WIDTH, PAD_HEIGHT))

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.update()
