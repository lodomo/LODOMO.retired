import pygame


pygame.init()

def create_frame(frame_image, width, height, color):
    thick = 7

    # Creates the frame Object. Does not display it.
    frame_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    pygame.draw.rect(frame_surface, color, (thick, thick, width - 2 * thick, height - 2 * thick))

    # top-left corner
    frame_surface.blit(frame_image, (0, 0), (0, 0, thick, thick))

    # top-right corner
    frame_surface.blit(frame_image, (width - thick, 0), ((thick + 1), 0, thick, thick))

    # bottom-left corner
    frame_surface.blit(frame_image, (0, height - thick), (0, thick + 1, thick, thick))

    # bottom-right corner
    frame_surface.blit(frame_image, (width - thick, height - thick), ((thick + 1), thick + 1, thick, thick))

    # top of frame
    for pixels in range(width - (2 * thick)):
        frame_surface.blit(frame_image, (thick + pixels, 0), (thick, 0, 1, thick))

    # bottom of frame
    for pixels in range(width - (2 * thick)):
        frame_surface.blit(frame_image, (thick + pixels, height - thick), (thick, thick + 1, 1, thick))

    # left of frame
    for pixels in range(height - (2 * thick)):
        frame_surface.blit(frame_image, (0, thick + pixels), (0, thick, thick, 1))

    # right of frame
    for pixels in range(height - (2 * thick)):
        frame_surface.blit(frame_image, (width - thick, thick + pixels), (thick + 1, thick, thick, 1))

    return frame_surface