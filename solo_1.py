import pygame
import elements

pygame.init()

screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def game():
    run = False
    snake = elements.snake_one()
    food = elements.food()
    while not run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
        clock.tick(10)
        snake.handle_keys()
        elements.drawGrid(screen)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(screen)
        food.draw(screen)
        screen.blit(screen, (0, 0))
        pygame.display.update()

    pygame.quit()
    quit()
