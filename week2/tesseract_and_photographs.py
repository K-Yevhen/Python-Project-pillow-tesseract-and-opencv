# Lets try a new example and bring together some of the things we have learned.
# Here's an image of a storefront, lets load it and try and get the name of the
# store out of the image
from PIL import Image
import pytesseract
# Lets read in the storefront image I've loaded into the course and display it
image = Image.open('storefront.jpg')
# image.show()
# Finally, lets try and run tesseract on that image and see what the results are
# print(pytesseract.image_to_string(image))

# We see at the very bottom there is just an empty string. Tesseract is unable to take
# this image and pull out the name. But we learned how to crop the images in the
# last set of lectures, so lets try and help Tesseract by cropping out certain pieces.
#
# First, lets set the bounding box. In this image the store name is in a box
# bounded by (315, 170, 700, 270)
bounding_box = (315, 170, 700, 270)

# crop the image
title_image = image.crop(bounding_box)

# display and pull out the text
# title_image.show()
# print(pytesseract.image_to_string(title_image))

# new bounding box
bounding_box = (900, 420, 940, 445)

# cropping smaller version
smaller_size = image.crop(bounding_box)

# display the image
# smaller_size.show()

# image to string with pytesseract inside function
# print(pytesseract.image_to_string(smaller_sign))

# trying to resize the image
new_size = (smaller_size.width * 10, smaller_size.height * 10)

# checking documentations for resize function
print(help(smaller_size.resize))

# We can see that there are a number of different filters for resizing the image. The
# default is Image.NEAREST. Lets see what that looks like
smaller_size.resize(new_size, Image.NEAREST).show()
