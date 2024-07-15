#Image resizing

from PIL import Image
# Open an image file
image = Image.open("uni.jpg")
# Resize the image to a new width and height
new_size = (400, 600)
resized_image = image.resize(new_size)
# Save the resized image
resized_image.save("resized_image.jpg")