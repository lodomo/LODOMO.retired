import fonts
import themes
from sys import exit

code_text = []

# Coding Loop
def GAMECODE_Loop(screen, pygame, mouse_cursor, clock):
    # Theme
    frame_size = [366, 198]
    current_theme = themes.CMDTheme(themes.plain)

    # This pads the text. This needs to be fine-tuned.
    frame_padding = 9
    text_padding_x = 15
    text_padding_y = 15

    vertical_spacing = 7
    user_input = ''
    blinking_cursor = '|'
    blinking_timer = 0
    valid_characters = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\' '
    code_running = True

    result = ['', 0]

    max_lines = 27
    cursor_line = 0
    cursor_char = 0

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return exit()
                if event.key == pygame.K_RETURN:
                    code_text.append(user_input)
                    user_input = ''
                if event.unicode in valid_characters:
                    user_input += event.unicode.upper()

        # Update all the text not being used.
        for i in range(len(code_text)):
            text_surface = fonts.default_font.render(code_text[i], True, current_theme.text_color)
            screen.blit(text_surface, (text_padding_x, text_padding_y + (vertical_spacing * i)))

        # Put user inputs on the screen
        display_input = user_input + blinking_cursor
        text_input_surface = fonts.default_font.render(display_input, False, current_theme.text_color)
        screen.blit(text_input_surface, (text_padding_x, text_padding_y + vertical_spacing * len(code_text)))


        pygame.display.update()
        clock.tick(60)