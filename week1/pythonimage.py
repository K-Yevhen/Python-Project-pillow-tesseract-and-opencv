import PIL

# print(PIL.__version__)

# print(help(PIL))
# print(dir(PIL))

from PIL import Image
# print(help(Image))


file = "/Users/yevhenkuts/PycharmProjects/New/Python-Project-pillow-tesseract-and-opencv/reandonly/msi_recruitment.gif"
image = Image.open(file)
print(image)
