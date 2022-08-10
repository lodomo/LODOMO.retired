import fonts
import themes
from sys import exit
import math
from lodomo_classes import *


# Constants
LINE_HEIGHT = 7  # Height of each line with Pinch_Mono Font
CHAR_WIDTH = 6  # Width characters with Pinch_Mono Font
TEXT_PAD = Vector2(15, 15)  # Text padding from top left corner
VERT_SPACE = 7  # How many pixels between each line


# TODO This needs to be something that happens on a timer, not every frame.
def Save_Code(code_to_save):
    with open('games/current_game/game_code.199X', 'w') as f:
        for i in code_to_save:
            f.write(i + '\n')


def Blinking_Cursor(position, _top_line):
    cursor_width = 5
    cursor_height = 7
    new_position = Vector2(position.x, position.y)
    new_position.x = TEXT_PAD.x + (position.x * CHAR_WIDTH)
    new_position.y = (TEXT_PAD.y - 1) + ((position.y - _top_line) * VERT_SPACE)
    return [new_position.x, new_position.y, cursor_width, cursor_height]


# Coding Loop
def GAMECODE_Loop(screen, pygame, mouse_cursor, clock):
    # Theme
    frame_size = [366, 198]
    current_theme = themes.CMDTheme(themes.plain)  # TODO Make theme loadable from preferences
    frame_padding = 9
    code_text = ['']  # This will be all the code the user has input
    visible_text = ['']  # This is all the code visible at any given time

    input_location = Vector2(0, 0)
    valid_characters = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\' '
    code_running = True
    max_lines = 27
    top_line = 0

    blinking_timer = 0
    blink_speed = 15
    blink_vis = True
    # blinking_cursor = Blinking_Cursor(input_location, top_line) # X location, Y Location, Width, Height

    while code_running:
        screen.fill(current_theme.background_color)  # Create Background
        screen.blit(current_theme.input_frame, (frame_padding, frame_padding))  # Create Frame

        # Draw the Cursor
        mouse_posit = pygame.mouse.get_pos()
        screen.blit(mouse_cursor, mouse_posit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     # TODO
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return exit()
                if event.key == pygame.K_RETURN:
                    code_text.insert(input_location.y + 1, '')
                    input_location.y += 1
                    input_location.x = 0
                if event.key == pygame.K_BACKSPACE:
                    if input_location.x > 0:
                        input_location.x -= 1
                        string_as_list = list(code_text[input_location.y])
                        string_as_list.pop(input_location.x)
                        code_text[input_location.y] = ''.join(string_as_list)
                    elif input_location.y > 0:
                        above_line = code_text[input_location.y - 1]
                        this_line = code_text[input_location.y]
                        new_line = above_line + this_line
                        code_text[input_location.y - 1] = new_line
                        input_location.y -= 1
                        input_location.x = len(new_line)
                if event.unicode in valid_characters:
                    string_as_list = list(code_text[input_location.y])
                    new_char = event.unicode.upper()
                    string_as_list.insert(input_location.x, new_char)
                    code_text[input_location.y] = ''.join(string_as_list)
                    input_location.x += 1
            if input_location.x > len(code_text[input_location.y]):
                input_location.x = len(code_text[input_location.y])

        # Move Code To Display
        for i in range(max_lines):
            if i < len(code_text):
                visible_text.append(code_text[i - top_line])

        # Draw the Blinking Cursor
        blinking_cursor = Blinking_Cursor(input_location, top_line)
        if blinking_timer > blink_speed:
            blink_vis = not blink_vis
            blinking_timer = 0
        if blink_vis:
            pygame.draw.rect(screen, current_theme.background_color, blinking_cursor)
        blinking_timer += 1

        # Update all the text
        for i in range(len(visible_text)):
            text_surface = fonts.default_font.render(visible_text[i], True, current_theme.text_color)
            screen.blit(text_surface, (TEXT_PAD.x, TEXT_PAD.y + (VERT_SPACE * i)))

        visible_text.clear()

        Save_Code(code_text)
        pygame.display.update()
        clock.tick(60)
