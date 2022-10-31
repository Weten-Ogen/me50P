from PIL import Image


pic = Image.open('/pillow/hermione.jpg')

r,g,a = pic.split()


pic = Image.merge('RGB',(r,g,a))
pic.save('new.gif')
