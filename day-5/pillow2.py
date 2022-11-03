from PIL import Image, ImageDraw , ImageFont

img = Image.open('./harry.jpg')

draw = ImageDraw.Draw(img)
text = "WaterMask"
width, height = img.size

font = ImageFont.truetype('', 36)

textwidth, textheight = draw.textsize(text, font)

margin = 10
x = width - textwidth - margin
y = height - textheight - margin

draw((x,y), text, font=font)

img.save()