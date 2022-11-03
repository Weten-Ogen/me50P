from PIL import Image


img = Image.open('harry.jpg')

img = img.transpose(Image.FLIP_LEFT_RIGHT)

img.save('blimey.jpg')