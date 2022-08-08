import fonts
import themes
from sys import exit
import math

code_text = ['']

text_padding_x = 15
text_padding_y = 15

def Save_Code(code_to_save):
        with open('games/current_game/game_code.199X', 'w') as f:
            for i in code_to_save:
                f.write(i + '\n')


def Mouse_Cursor_Move(position):
    line_height = 7
    char_width = 6
    x = position[0]
    y = position[1]
    x -= text_padding_x
    y -= text_padding_y

    if x < 0 or y < 0:
        return 0

    x = math.ceil(x/char_width) - 1  # Decides Line
    y = math.ceil(y/line_height) - 1  # Decides Char
    return x, y


# Coding Loop
def GAMECODE_Loop(screen, pygame, mouse_cursor, clock):
    # Theme
    frame_size = [366, 198]
    current_theme = themes.CMDTheme(themes.plain)
    frame_padding = 9

    vertical_spacing = 7
    current_line = 0
    blinking_cursor = '|'
    blinking_timer = 0
    valid_characters = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\' '
    code_running = True

    result = ['', 0]

    max_lines = 27
    top_line = 0


    while code_running:
        # Fill the screen with background color.
        screen.fill(current_theme.background_color)

        # Draw the Frame
        screen.blit(current_theme.input_frame, (frame_padding, frame_padding))

        # Draw the Cursor
        mouse_posit = pygame.mouse.get_pos()
        screen.blit(mouse_cursor, mouse_posit)

        # Blinking Cursor
        if blinking_timer < 30:
            blinking_timer += 1
        else:
            blinking_timer = 0
            if blinking_cursor == '|':
                blinking_cursor = ' '
            else:
                blinking_cursor = '|'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                move_cursor = Mouse_Cursor_Move(pygame.mouse.get_pos())
                print(move_cursor)
                if move_cursor != 0:
                    blinking_cursor_position = move_cursor
                    current_line = blinking_cursor_position[1]
                    if current_line > len(code_text):
                        current_line = len(code_text) - 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return exit()
                if event.key == pygame.K_RETURN:
                    code_text.insert(current_line+1, '')
                    current_line += 1
                if event.unicode in valid_characters:
                    code_text[current_line] += event.unicode.upper()
                if event.key == pygame.K_BACKSPACE:
                    if len(code_text[current_line]) <= 0:
                        current_line -= 1
                    code_text[current_line] = code_text[current_line][:-1]

        visible_text = []

        # Move Code To Display
        for i in range(max_lines):
            if i < len(code_text):
                visible_text.append(code_text[i - top_line])

        # Update all the text
        for i in range(len(visible_text)):
            text_surface = fonts.default_font.render(visible_text[i], True, current_theme.text_color)
            screen.blit(text_surface, (text_padding_x, text_padding_y + (vertical_spacing * i)))

        visible_text.clear()

        pygame.display.update()
        clock.tick(60)
        Save_Code(code_text)
