# In the previous example, we were using a clear, unambiguous image for conversion. Sometimes there will
# be noise in images you want to OCR, making it difficult to extract the text. Luckily, there are
# techniques we can use to increase the efficacy of OCR with pytesseract and Pillow.
#
# Let's use a different image this time, with the same text as before but with added noise in the picture.
# We can view this image using the following code.
from PIL import Image
import PIL
import pytesseract

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

img = img.convert('L')
img.save('greyscale_noise.jpg')
# And run OCR on the greyscale image
text = pytesseract.image_to_string(Image.open('greyscale_noise.jpg'))
# print(text)

help(img.convert())