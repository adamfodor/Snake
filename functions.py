import pygame
import solo_1
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
run = False


def menu(x, y):
    menu_bg = pygame.image.load("menu_bg.png")
    screen.blit(menu_bg, (x, y))


def game_bg(x, y):
    bg = pygame.image.load("bg.png")
    screen.blit(bg, (x, y))


def label(label, label_color, x, y, w, h):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(label, True, label_color, )
    textrect = text.get_rect()
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text, textrect)


def buttons(where, x, y, w, h, acitve_colour, inactive_colour, text, function=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
        pygame.draw.rect(where, acitve_colour, (x, y, w, h), )
        if function == "solo" and click[0] == 1:
            solo_1.game()
        if function == "quit" and click[0] == 1:
            quit()



    else:
        pygame.draw.rect(where, inactive_colour, (x, y, w, h), )
    label(text, (0, 0, 0), x, y, w, h)








