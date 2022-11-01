from PIL import Image

image = Image.open('./hermione.jpg')

r, g, b = image.split()

image = Image.merge('RGB', (g, b, r))
image.save('hermy.jpg')
