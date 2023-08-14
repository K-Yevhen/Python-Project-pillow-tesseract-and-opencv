from PIL import Image, ImageEnhance
from IPython.display import display

file = "msi_recruitment.gif"
image = Image.open(file).convert('RGB')

# display(image.show())
enhanced = ImageEnhance.Brightness(image)
images = []
for i in range(0, 10):
    images.append(enhanced.enhance(i/10))

# print(images)

first_image = images[0]
