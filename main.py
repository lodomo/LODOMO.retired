import pygame
import lodomo_cmd
import lodomo_code
import time
import functools

current_version = '0.01A.1'

# Initialize pygame.
pygame.init()

# Set the window title. This must be update-able.
window_title = 'LODOMO : ロードーモー'
pygame.display.set_caption(window_title)

# Set the window icon. This must be update-able.
window_icon = pygame.image.load('assets/images/lodomo.png')
pygame.display.set_icon(window_icon)

# Force the screen to be this resolution.
resolution = [384, 216]
screen = pygame.display.set_mode((resolution[0], resolution[1]), pygame.SCALED | pygame.FULLSCREEN)

# Hide the mouse
pygame.mouse.set_visible(False)
mouse_cursor = pygame.image.load('assets/images/mouse.png').convert_alpha()

# This makes a clock to set FPS
clock = pygame.time.Clock()

# Programs
cmd = lambda: lodomo_cmd.CMD_Loop(screen, current_version, pygame, mouse_cursor, clock)
code = lambda: lodomo_code.GAMECODE_Loop(screen, pygame, mouse_cursor, clock)
current_program = code

running = True

while running:
    next_action = current_program()
    if next_action == 2:
        running = False
        pygame.quit()
        quit()
    if next_action == 3:
        current_program = cmd
    if next_action == 4:
        current_program = code
