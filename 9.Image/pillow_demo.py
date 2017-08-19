import os
from os import walk
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def scan_files():
    f = []
    mypath = os.path.dirname(__file__)
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

    print(f)


def open_image():
    im = Image.open("QR.png")
    im.show()  # 显示图片
    print(im.format, im.size, im.mode)


# sys.argv[:]
def scan_image_to_jpg():
    for infile in os.listdir(os.path.dirname(__file__)):
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print("cannot convert", infile)


def draw_image():
    from PIL import Image, ImageDraw
    sourceFileName = "jn.jpg"
    avatar = Image.open(sourceFileName)
    drawAvatar = ImageDraw.Draw(avatar)

    xSize, ySize = avatar.size
    myFont = ImageFont.truetype("/Library/Fonts/Verdana.ttf", 100)
    drawAvatar.text([50, 0.1 * ySize - drawAvatar.textsize("30")[1]], "30", fill=(0, 0, 0), font=myFont)
    del drawAvatar

    avatar.show()




import platform
import re
import sys

canvas_w = int(400)
canvas_h = int(560)
image_width = int(350)
image_height = int(350)
top = int(55)
t_i_top = int(35)


def recreate_image_text():
  
    margin = int((canvas_w - image_width) / 2)

    toImage = Image.new('RGBA', (canvas_w, canvas_h), color='#ffffff')
    fromImage = Image.open(resource_path('resources/mm.jpg')).resize((image_width, image_height), Image.ANTIALIAS)
    toImage.paste(fromImage, (margin, top))

    # font
    title_font = ImageFont.truetype("STHeiti Light.ttc", 12)

    if not re.search(r'Darwin', platform.platform()).group():
        title_font = ImageFont.truetype("symbol.ttf", 10)

    # comment text

    drawAvatar = ImageDraw.Draw(toImage)
    #rank
    text = '排名 1'
    font = ImageFont.truetype("STHeiti Light.ttc", 22)
    textsize = drawAvatar.textsize(text, font)
    x = (canvas_w - textsize[0]) * 0.5
    drawAvatar.multiline_text([x, 15],text ,
                              (0, 0, 0), font)

    
    
    texts = ['Herou Women Summer Beach \n Casual Flared Tank Dress',
             '评分:4.5', '评论数:1002', '价格: $100-$200']
    colors = [(0, 0, 0), '#ff5257', '#ff5257', '#ff5257']

    for i, t in enumerate(texts):
        extra = 0
        if i == 0:
            extra = 15
        draw_text(drawAvatar, text=t, font=title_font,
                  y=image_height + top + t_i_top + i * 25 - extra, fill=colors[i])

    # des text
    del drawAvatar
    toImage.show()
    toImage.save('thumbnail.png', 'png')


def draw_text(drawAvatar, text, font, y, fill=(0, 0, 0), align='center'):
    textsize = drawAvatar.textsize(text, font)
    x = (canvas_w - textsize[0]) * 0.5
    drawAvatar.multiline_text([x, y], text,
                              fill=fill, font=font, align=align)


def resource_path(relative_path):
    """定义一个读取相对路径的函数"""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    recreate_image_text()
