from PIL import Image
import log


#  Returns the hex code of a single pixel
def create_hex_color(pixel_info):
    new_color = '#'
    for rgb in range(3):
        value = hex(pixel_info[rgb])
        new_color += value[2:]
    return new_color


color = ['LIMPID']  # LIMPID free of anything that darkens; completely clear.
open_image = Image.open('assets/images/colorpalette.png')  # Open the Palette

if open_image.size == (31, 1):
    log.info("Palette Image Loaded")
else:
    log.error("Palette Image Error. Ensure image is 31x1 pixels")

loaded_image = open_image.load()
for i in range(31):
    pixel = loaded_image[i, 0]
    import_color = create_hex_color(pixel)
    color.append(import_color)

if len(color) != 32:
    log.error("Error Loading Palette to Memory")
else:
    log.info("Palette Image Converted to List")
    for i in color:
        print(i)
