import pygame
from sys import exit
import palette
import fonts
from create_frame import create_frame

current_version = '0.01A'

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



def command_prompt(user_input):
    input = user_input.upper()
    response = [input]
    maximum_request = 50

    # restrict request length
    while len(input) > maximum_request:
        input = input[:-1]

    # Return 0 for further input from user. Return Text for further processing from script.
    if input == 'HELP':
        remark = 'TYPE THEME TO FOR LIST OF THEMES'
        response.append(remark)
        return [response, 0]
    elif input in ['THEME', 'THEMES']:
        remark = 'THEME MENU: PLAIN, MINT, STRAWBERRY, BANANA, PEANUT'
        response.append(remark)
        return [response, 0]
    elif input in ['PLAIN', 'MINT', 'STRAWBERRY', 'BANANA', 'PEANUT']:
        remark = 'THEME CHANGED TO ' + input
        response.append(remark)
        return [response, input]
    elif input == '' or input == ' ':
        return [response, 0]
    else:
        error = '\'' + input + '\'' + ' IS NOT A COMMAND'
        response.append(error)
        return [response, 0]


# CMD Loop
def CMD_Loop():
    # Style
    background_color = palette.color[3]
    text_color = palette.color[0]
    version_text_color = palette.color[0]

    # This pads the text. This needs to be fine-tuned.
    frame_padding = 9
    text_padding_x = 20
    text_padding_y = 24
    version_position = (335,208)

    # This contains all the text displayed in CMD. TODO output to file.
    main_text = []
    
    # Boot Text - Should "type out" on the screen. TODO
    main_text.append('LOODOMO [VERSION 0.01A]')
    main_text.append('(C) L.D. MOON STUDIO. ALL RIGHTS RESERVED')

    main_text_max_lines = 20
    vertical_spacing = 8
    user_input = ''
    blinking_cursor = '|'
    blinking_timer = 0
    valid_characters = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?\' '
    cmd_running = True

    plain_frame_image = pygame.image.load('assets/images/themes/plain.png').convert_alpha()
    mint_frame_image = pygame.image.load('assets/images/themes/mint.png').convert_alpha()
    strawberry_frame_image = pygame.image.load('assets/images/themes/strawberry.png').convert_alpha()
    banana_frame_image = pygame.image.load('assets/images/themes/banana.png').convert_alpha()
    peanut_frame_image = pygame.image.load('assets/images/themes/peanut.png').convert_alpha()

    input_frame = create_frame(plain_frame_image, 366, 198, palette.color[4])

    lodomo_logo = pygame.image.load('assets/images/themes/plain_logo.png').convert_alpha()
    plain_logo = pygame.image.load('assets/images/themes/plain_logo.png').convert_alpha()
    mint_logo = pygame.image.load('assets/images/themes/mint_logo.png').convert_alpha()
    strawberry_logo = pygame.image.load('assets/images/themes/strawberry_logo.png').convert_alpha()
    banana_logo = pygame.image.load('assets/images/themes/banana_logo.png').convert_alpha()
    peanut_logo = pygame.image.load('assets/images/themes/peanut_logo.png').convert_alpha()
    lodomo_location = (15, 2)

    result = ['', 0]

    while cmd_running:
        # Fill the screen with background color.
        screen.fill(background_color)

        # Draw the Frame
        screen.blit(input_frame, (frame_padding, frame_padding))
        screen.blit(lodomo_logo, lodomo_location)

        # Draw version number
        version_number = fonts.babyblocks.render('VERSION ' + current_version, False, version_text_color)
        screen.blit(version_number, version_position)

        # Draw the Cursor
        mouse_posit = pygame.mouse.get_pos()
        screen.blit(mouse_cursor, mouse_posit)

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
                return exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    while len(main_text) >= main_text_max_lines:
                        main_text.pop(0)
                    result = command_prompt(user_input)
                    return_text = result[0]
                    for text in return_text:
                        main_text.append(text)
                    user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1].upper()

                elif event.unicode in valid_characters:
                    user_input += event.unicode.upper()

                elif event.key == pygame.K_ESCAPE:
                    cmd_running = not cmd_running

        # START COMMAND PROMPT

        for i in range(len(main_text)):
            text_surface = fonts.babyblocks.render(main_text[i], True, text_color)
            screen.blit(text_surface, (text_padding_x, text_padding_y + (vertical_spacing * i)))

        text_input_surface = fonts.babyblocks.render('> ' + user_input + blinking_cursor, False, text_color)
        screen.blit(text_input_surface, (text_padding_x, text_padding_y + vertical_spacing * len(main_text)))

        # Handle Inputs
        if result[1] != 0:
            if result[1] == 'PLAIN':
                background_color = palette.color[3]
                input_frame = create_frame(plain_frame_image, 366, 198, palette.color[4])
                text_color = palette.color[0]
                version_text_color = palette.color[0]
                lodomo_logo = plain_logo
            if result[1] == 'MINT':
                background_color = palette.color[18]
                input_frame = create_frame(mint_frame_image, 366, 198, palette.color[4])
                text_color = palette.color[10]
                version_text_color = palette.color[10]
                lodomo_logo = mint_logo
            if result[1] == 'STRAWBERRY':
                background_color = palette.color[23]
                input_frame = create_frame(strawberry_frame_image, 366, 198, palette.color[20])
                text_color = palette.color[25]
                version_text_color = palette.color[25]
                lodomo_logo = strawberry_logo
            if result[1] == 'BANANA':
                background_color = palette.color[30]
                input_frame = create_frame(banana_frame_image, 366, 198, palette.color[4])
                text_color = palette.color[25]
                version_text_color = palette.color[25]
                lodomo_logo = banana_logo
            if result[1] == 'PEANUT':
                background_color = palette.color[28]
                input_frame = create_frame(peanut_frame_image, 366, 198, palette.color[31])
                text_color = palette.color[25]
                version_text_color = palette.color[31]
                lodomo_logo = peanut_logo





        # END COMMAND PROMPT

        result[1] = 0
        pygame.display.update()
        clock.tick(60)


Start_Loop = CMD_Loop()
