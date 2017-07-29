import sys

from PIL import ImageDraw, ImageFont, Image


def input_par():
    text = input('Enter the text to insert in image: ')
    size = int(input('Enter the desired size: '))
    color_value = input('Enter the color for the text(r, g, b): ')).split()
    color_value = [int(i) for i in color_value.split()]
    
    return text, size, color_value


def main():
    assert len(sys.argv) == 2  # python3 meme_maker.py <path-to-image>
    
    image_file = Image.open("%s.jpg" % sys.argv[1])
    image_file = image_file.convert("RGBA")
    pixel_data = image_file.load()

    print(image_file.size)
    text, size, color_value = input_par()

    font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", size=size)

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in range(100):
        for x in range(100):
            pixdata[x, y] = (255, 255, 255, 255)

    # Drawing text on the picture
    draw = ImageDraw.Draw(image_file)
    draw.text((0, 2300), text, (color_value[0], color_value[1], color_value[2]), font=font)
    draw = ImageDraw.Draw(image_file)
    image_file.save("%s.jpg" % input("File Name: "))
    return True


if __name__ == '__main__':
    main()
