import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font = ImageFont.truetype("NanumPen.ttf", 50)
img = Image.open('back.jpg')
draw = ImageDraw.Draw(img)
draw.text((50, 50), '이미지 테스트~', fill=(255,255,255), font=font)
img.save("test.png")
