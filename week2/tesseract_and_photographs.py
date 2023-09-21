# Lets try a new example and bring together some of the things we have learned.
# Here's an image of a storefront, lets load it and try and get the name of the
# store out of the image
from PIL import Image
import pytesseract
# Lets read in the storefront image I've loaded into the course and display it
image=Image.open('storefront.jpg')
image.show()
# Finally, lets try and run tesseract on that image and see what the results are
print(pytesseract.image_to_string(image))
