# In the previous example, we were using a clear, unambiguous image for conversion. Sometimes there will
# be noise in images you want to OCR, making it difficult to extract the text. Luckily, there are
# techniques we can use to increase the efficacy of OCR with pytesseract and Pillow.
#
# Let's use a different image this time, with the same text as before but with added noise in the picture.
# We can view this image using the following code.
from PIL import Image
img = Image.open("Noisy_OCR.PNG")
img.show()

