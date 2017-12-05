import PIL
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
cwd = os.path.dirname(os.path.realpath(__file__))

fonts_dir = cwd
img_dir = cwd

#FONT_NUMBERS:
#    0: normal
#    1: light
#    2: bold
FONTS = [
         ImageFont.truetype(fonts_dir+"/OpenSans-Regular.ttf", 25),
         ImageFont.truetype(fonts_dir+"/OpenSans-Light.ttf", 25),
         ImageFont.truetype(fonts_dir+"/OpenSans-Bold.ttf", 25)
        ]

#list of ((x,y), text, (r,g,b), font_number)
directions = [
              ((0,0), "abcdefghijklmnopQRSTUVWXYZ", (0,0,0), 0)
             ]

def create_nametag(w, h):
    img = Image.new("RGBA", (w,h), (255,255,255))
    for direction in directions:
        add_text(img, direction)
    img.save(img_dir+"/test.png")

def add_text(img, direction):
    draw = ImageDraw.Draw(img)
    draw.text(direction[0], direction[1], direction[2], FONTS[direction[3]])