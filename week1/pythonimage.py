import PIL
import inspect
from IPython.display import display

# print(PIL.__version__)

# print(help(PIL))
# print(dir(PIL))


from PIL import Image, ImageFilter

# print(help(Image))
# print(help(ImageFilter))

file = "/Users/yevhenkuts/PycharmProjects/New/Python-Project-pillow-tesseract-and-opencv/week1/msi_recruitment.png"
image = Image.open(file)
# print(image)

# print("The type of the image is {}".format(str(type(image))))

# print(inspect.getmro(type(image)))

# print(help(image.copy))

# print(help(image.save))

# print(inspect.getmro(type(image)))

# print(help(ImageFilter))


image = image.convert('RGB')  # this stands for red, green blue mode
blurred_image = image.filter(ImageFilter.BLUR)
# display(blurred_image)
blurred_image.show()
blurred_image.save("blurred.jpg")
