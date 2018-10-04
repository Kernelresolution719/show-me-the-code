from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-30, 0), '1', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('test.jpg')
    add_num(image)
