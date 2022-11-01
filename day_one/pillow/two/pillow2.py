from PIL import Image, ImageFilter

img = Image.open('./harry.jpg')

img = img.filter(ImageFilter.GaussianBlur(radius=2))


img.save('hurry.jpg')