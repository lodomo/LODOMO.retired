import pygame.font

pygame.font.init()

pinch_mono = pygame.font.Font("assets/fonts/pinch_mono.ttf", 7)
baby_blocks = pygame.font.Font("assets/fonts/baby_blocks.ttf", 8)

default_font = pinch_mono


def type(string, color, loc_x, loc_y, display):
    surface = default_font.render(string, True, color)
    return display.blit(surface, (loc_x, loc_y))