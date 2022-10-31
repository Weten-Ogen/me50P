from PIL import Image

pic = Image.open('/pillow/hermione.jpg')

pic.save('pic.gif')

pic1 = Image.open('pic.gif')
pic1 = pic1.rotate(185)
pic1.save('pic.gif')
