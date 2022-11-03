from PIL import Image



img = Image.open('./harry.jpg')

img = img.crop((1,2,300,300))
img.save('croped.jpg')
