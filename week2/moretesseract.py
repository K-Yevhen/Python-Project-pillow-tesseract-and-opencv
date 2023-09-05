# In the previous example, we were using a clear, unambiguous image for conversion. Sometimes there will
# be noise in images you want to OCR, making it difficult to extract the text. Luckily, there are
# techniques we can use to increase the efficacy of OCR with pytesseract and Pillow.
#
# Let's use a different image this time, with the same text as before but with added noise in the picture.
# We can view this image using the following code.
from PIL import Image
import PIL
import pytesseract
from IPython.display import display_png

img = Image.open("Noisy_OCR.PNG")
# img.show()

# text = pytesseract.image_to_string(img)
# print(text)

basewidth = 600

# We want to get the correct aspect ratio, so we can do this by taking the base width and dividing
# it by the actual width of the image
wpercent = (basewidth / float(img.size[0]))
# With that ratio we can just get the appropriate height of the image.
hsize = int((float(img.size[1]) * float(wpercent)))
# Finally, lets resize the image. antialiasing is a specific way of resizing lines to try and make them
# appear smooth
img = img.resize((basewidth, hsize), PIL.Image.Resampling.LANCZOS)
# img.save("resized_Noisy_OCR.png")
# img.show()

new_image = Image.open("resized_Noisy_OCR.png")
text = pytesseract.image_to_string(new_image)
# print(text)

# hrm, no improvement for resizing the image. Let's convert the image to greyscale. Converting images
# can be done in many different ways. If we poke around in the PILLOW documentation we find that one of
# the easiest ways to do this is to use the convert() function and pass in the string 'L'
img = img.convert('L')
# Now lets save that image
# img.save('greyscale_noise.jpg')
# And run OCR on the greyscale image
text = pytesseract.image_to_string(Image.open('greyscale_noise.jpg'))
# print(text)

# help(img.convert())

# Wow, that worked really well! If we look at the help documentation using the help function
# as in help(img.convert) we see that the conversion mechanism is the ITU-R 601-2 luma transform.
# There's more information about this out there, but this method essentially takes a three channel image,
# where there is information for the amount of red, green, and blue (R, G, and B), and reduces it
# to a single channel to represent luminosity. This method actually comes from how standard
# definition television sets encoded color onto black and while images. If you get really interested
# in image manipulation and recognition, learning about color spaces and how we represent color, both
# computationally and through human perception, is really an interesting field.


# Even though we have now the complete text of the image, there are a few other techniques
# we could use to help improve OCR detection in the event that the above two don't help.
# The next approach I would use is called binarization, which means to separate into two
# distinct parts - in this case, black and white. Binarization is enacted through a process
# called thresholding. If a pixel value is greater than a threshold value, it will be converted
# to a black pixel; if it is lower than the threshold it will be converted to a white pixel.
# This process eliminates noise in the OCR process allowing greater image recognition accuracy.
# With Pillow, this process is straightforward.
# Lets open the noisy impage and convert it using binarization
img = Image.open('Noisy_OCR.PNG').convert('1')
# Now lets save and display that image
img.save('black_white_noise.jpg')
# img.show()

# So, that was a bit magical, and really required a fine reading of the docs to figure out
# that the number "1" is a string parameter to the convert function actually does the binarization.
# But you actually have all of the skills you need to write this functionality yourself.
# Lets walk through an example. First, lets define a function called binarize, which takes in
# an image and a threshold value:
def binarize(image_to_transform, threshold):
    # now, lets convert that image to a single greyscale image using convert()
    output_image=image_to_transform.convert("L")
    # the threshold value is usually provided as a number between 0 and 255.
    # the algorithm for the binarization is pretty simple, go through every pixel in the
    # image and, if it's greater than the threshold, turn it all the way up (255), and
    # if it's lower than the threshold, turn it all the way down (0).
    # so lets write this in code. First, we need to iterate over all of the pixels in the
    # image we want to work with
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                # lets set this to zero
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255
                output_image.putpixel( (x,y), 255 )
    #now we just return the new image
    return output_image

# lets test this function over a range of different thresholds. Remember that you can use
# the range() function to generate a list of numbers at different step sizes. range() is called
# with a start, a stop, and a step size. So lets try range(0, 257, 64), which should generate 5
# images of different threshold values
for thresh in range(0,257,64):
    print("Trying with threshold " + str(thresh))
    # Lets display the binarized image inline
    binarized = binarize(Image.open('Noisy_OCR.PNG'), thresh)
    binarized.show()
    # And lets use tesseract on it. It's inefficient to binarize it twice but this is just for
    # a demo
    print(pytesseract.image_to_string(binarize(Image.open('Noisy_OCR.PNG'), thresh)))

# We can see from this that a threshold of 0 essentially turns everything white,
# that the text becomes more bold as we move towards a higher threshold, and that
# the shapes, which have a filled in grey color, become more evident at higher
# thresholds. In the next lecture we'll look a bit more at some of the challenges
# you can expect when doing OCR on real data
