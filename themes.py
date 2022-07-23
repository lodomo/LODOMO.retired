import pygame
import palette
import create_frame


class Theme:
    def __init__(self, theme_name, bg_color, frame_color, text_color, version_text_color):
        self.theme_name = theme_name
        self.bg_color = palette.color[bg_color]
        self.frame_image = 'assets/images/themes/' + theme_name + '.png'
        self.frame_color = palette.color[frame_color]
        self.text_color = palette.color[text_color]
        self.version_text_color = palette.color[version_text_color]
        self.theme_logo = 'assets/images/themes/' + theme_name + '_logo.png'


class CMDTheme:
    def __init__(self, theme):
        frame_size = [366, 198]
        self.theme_frame = Load_Image(theme.frame_image)
        self.theme_logo = Load_Image(theme.theme_logo)
        self.background_color = theme.bg_color
        self.input_frame = create_frame.create_frame(self.theme_frame, frame_size[0], frame_size[1], theme.frame_color)
        self.text_color = theme.text_color
        self.version_text_color = theme.version_text_color
        self.lodomo_logo = self.theme_logo


def Load_Image(image_file):
    image_file = pygame.image.load(image_file).convert_alpha()
    return image_file


def Get_Names(input_list):
    new_list = []
    for list_items in input_list:
        new_list.append(list_items.theme_name)
    return new_list


plain = Theme('PLAIN', 3, 4, 0, 0)
mint = Theme('MINT', 18, 4, 10, 10)
strawberry = Theme('STRAWBERRY', 23, 20, 25, 25)
banana = Theme('BANANA', 30, 4, 25, 25)
peanut = Theme('PEANUT', 28, 31, 25, 31)
theme_list = [plain, mint, strawberry, banana, peanut]
theme_names = Get_Names(theme_list)


def Load_Theme(user_input):
    for i in range(len(theme_list)):
        if user_input == theme_list[i].theme_name:
            return theme_list[i]
