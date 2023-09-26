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
title_image.show()
print(pytesseract.image_to_string(title_image))