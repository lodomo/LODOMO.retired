import pygame
from sys import exit
import palette
import fonts
from command_prompt_routes import command_prompt

# Initialize pygame. Clearly.
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

# This makes a clock so I can set the FPS to 60 in the LODOMO Loop.
clock = pygame.time.Clock()

# Style
background_color = palette.color[4]
text_color = palette.color[0]

# CMD Loop
def CMD_Loop():
    screen_padding = 10
    maximum_request = 60
    main_text = []
    main_text.append('Welcome to Lodomo')
    main_text_max_length = 23

    vertical_spacing = 8
    user_input = 'User Input Place Holder'
    blinking_cursor = '|'
    blinking_timer = 0
    valid_characters = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\' '
    cmd_running = True;

    while cmd_running:
        # Fill the screen with background color.
        screen.fill(background_color)

        # Blink Cursor
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
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    while len(main_text) >= main_text_max_length:
                        main_text.pop(0)
                    return_text = command_prompt(user_input)
                    for text in return_text:
                        main_text.append(text)
                    user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1].upper()
                elif event.unicode in valid_characters:
                    user_input += event.unicode.upper()
                elif event.key == pygame.K_ESCAPE:
                    cmd_running = not cmd_running

        ## START COMMAND PROMPT

        for i in range(len(main_text)):
            text_surface = fonts.babyblocks.render(main_text[i], True, text_color)
            screen.blit(text_surface, (screen_padding, screen_padding + (vertical_spacing * i)))

        text_input_surface = fonts.babyblocks.render(user_input + blinking_cursor, False, text_color)
        screen.blit(text_input_surface, (screen_padding, screen_padding + vertical_spacing * len(main_text)))

        ## END COMMAND PROMPT

        pygame.display.update()
        clock.tick(60)


Start_Loop = CMD_Loop()
