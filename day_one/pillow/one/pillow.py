from PIL import Image

hermione = Image.open('/pillow/hermione.jpg')
hogwarts = Image.open('/pillow/hogwarts.jpg')
donknow = Image.open('/pillow/donknow.jpg')
# Returns the filename
print(hermione.filename)

# Returns the format type
print(hermione.format)

# Returns the mode of the image
print(hermione.mode)

# Returns the actual size of image
print(hermione.size)

# Returns a dict holding image info
print(hermione.info)

# Returns the color palette
print(hermione.palette)
