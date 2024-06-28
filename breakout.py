import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
ROWS, COLS = 5, 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)

def main():
    paddle = pygame.Rect(SCREEN_WIDTH//2 - PADDLE_WIDTH//2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, BALL_RADIUS, BALL_RADIUS)
    ball_vel = [5, -5]

    bricks = []
    for row in range(ROWS):
        for col in range(COLS):
            brick = pygame.Rect(col * (BRICK_WIDTH + 10) + 35, row * (BRICK_HEIGHT + 10) + 35, BRICK_WIDTH,
                                BRICK_HEIGHT)
            bricks.append(brick)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= 6
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.right += 6

        ball.left += ball_vel[0]
        ball.top += ball_vel[1]

        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_vel[0] = -ball_vel[0]
        if ball.top <= 0:
            ball_vel[1] = -ball_vel[1]
        if ball.colliderect(paddle):
            ball_vel[1] = -ball_vel[1]

        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_vel[1] = -ball_vel[1]
                break

        if ball.top >= SCREEN_HEIGHT:
            running = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), paddle)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        draw_bricks(bricks)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
