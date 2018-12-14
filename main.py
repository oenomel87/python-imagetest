import os
from PIL import ImageFont, Image, ImageDraw

font = ImageFont.truetype("NanumPen.ttf", 15)

def main():
    for file_name in os.listdir('./coupon_qr'):
        img = Image.open('./coupon_qr/' + file_name)
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(1, 1), text=file_name[:-4], fill=(0,0,0), font=font)
        img.save('./results/' + file_name)

main()