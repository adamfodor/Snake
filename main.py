import functions

import pygame

pygame.init()

screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
inactive_button_colour = (234, 214, 94)
active_button_colour = (235, 190, 32)


def main():
    run = False
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

        functions.menu(0, 0)
        functions.buttons(screen, 80, 350, 150, 30, active_button_colour, inactive_button_colour,"1 játékos","solo")
        functions.buttons(screen, 80, 390, 150, 30, active_button_colour, inactive_button_colour, "2 játékos","multi")
        #functions.buttons(screen, 80, 430, 150, 30, active_button_colour, inactive_button_colour, "Pontok","scores")
        functions.buttons(screen, 80, 430, 150, 30, active_button_colour, inactive_button_colour, "Kilépés","quit")#(80,470,150,30)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

main()
