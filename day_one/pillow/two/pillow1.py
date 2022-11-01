from PIL import Image

img = Image.open('./hermione.jpg')
pic = Image.open('./harry.jpg')

img = img.resize((500, 300))
img_size = img.size
pic_size = pic.size
new_pic = Image.new('RGB',(2*img_size[0], img_size[1]),(250,250,250))
new_pic.paste(img,(0,0))
new_pic.paste(pic,(img_size[0], 0))
new_pic.save('marcus.jpg','JPEG')

