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
# print(help(smaller_size.resize))

# We can see that there are a number of different filters for resizing the image. The
# default is Image.NEAREST. Lets see what that looks like
# smaller_size.resize(new_size, Image.NEAREST).show()


# really pixelated. Lets see what all the different resize options look like
options = [Image.Resampling.NEAREST, Image.Resampling.BOX, Image.Resampling.BILINEAR, Image.Resampling.HAMMING, Image.Resampling.BICUBIC, Image.Resampling.LANCZOS]
# for option in options:
#     print(option)
#     smaller_size.resize(new_size, option).show()

# From this we can notice two things. First, when we print out one of the resampling
# values it actually just prints an integer! This is really common: that the
# API developer writes a property, such as Image.BICUBIC, and then assigns it to an
# integer value to pass it around. Some languages use enumerations of values, which is
# common in say, Java, but in python this is a pretty normal way of doing things.
# The second thing we learned is that there are a number of different algorithms for
# image resampling. In this case, the Image.LANCZOS and Image.BICUBIC filters do a good
# job. Lets see if we are able to recognize the text off of this resized image

# First lets resize to the larger size
bigger_sign = smaller_size.resize(new_size, Image.Resampling.BICUBIC)
# Lets print out the text
pytesseract.image_to_string(bigger_sign)

# Well, no text there. Lets try and binarize this. First, let me just bring in the
# binarization code we did earlier
def binarize(image_to_transform, threshold):
    output_image = image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x, y)) < threshold:
                output_image.putpixel((x, y), 0)
            else:
                output_image.putpixel((x, y), 255)
    return output_image


# Now, lets apply binarizations with, say, a threshold of 190, and try and display that
# as well as do the OCR work
# binarized_bigger_sign = binarize(bigger_sign, 190)
# binarized_bigger_sign.show()
# print(pytesseract.image_to_string(binarized_bigger_sign))


# Ok, that text is pretty useless. How should we pick the best binarization
# to use? Well, there are some methods, but lets just try something very simple to
# show how well this can work. We have an english word we are trying to detect, "FOSSIL".
# If we tried all binarizations, from 0 through 255, and looked to see if there were
# any english words in that list, this might be one way. So lets see if we can
# write a routine to do this.
#
# First, lets load a list of english words into a list. I put a copy in the readonly
# directory for you to work with
eng_dict = []
with open("words_alpha.txt", "r") as f:
    data = f.read()
    # now we want to split this into a list based on the new line characters
    eng_dict = data.split("\n")

for i in range(150, 170):
    strng = pytesseract.image_to_string(binarize(bigger_sign, i))
    # We want to remove non alphabetical characters, like ([%$]) from the text, here's
    # a short method to do that
    # first, lets convert our string to lower case only
    strng = strng.lower()
    import string
    comparison = ''
    for character in strng:
        if character in string.ascii_lowercase:
            comparison = comparison + character
    # finally, lets search for comparison in the dictionary file
    if comparison in eng_dict:
        # and print it if we find it
        print(comparison)
