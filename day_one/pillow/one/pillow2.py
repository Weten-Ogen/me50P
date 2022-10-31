from PIL import Image

pic = Image.open('/pillow/hermione.jpg')

pic.thumbnail((100,90),resample=1)

pic.save('tnail.jpg')