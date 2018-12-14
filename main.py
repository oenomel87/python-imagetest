import os
from PIL import ImageFont, Image, ImageDraw

font_size = 15
font = ImageFont.truetype("NanumSquareRegular.ttf", font_size)

def create_canvas(image_size):
    size = (image_size[0], image_size[1] + 20)
    canvas = Image.new(mode='RGB', size=size, color=(255,255,255))
    return canvas

def main():
    for file_name in os.listdir('./coupon_qr/coupon_qr-1050'):
        img = Image.open('./coupon_qr/coupon_qr-1050/' + file_name)
        img = img.convert('RGB')
        canvas = create_canvas(img.size)
        canvas.paste(img, (0,0))
        draw = ImageDraw.Draw(canvas)
        draw.text(xy=(15, canvas.size[0] - 5), text=file_name[:-4], fill=(0,0,0), font=font)
        canvas.save('./results/results-1050/' + file_name)

main()