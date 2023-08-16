import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from IPython.display import display

# read image and convert to RGB
image = Image.open("msi_recruitment.gif")
image = image.convert('RGB')

# build a list of 9 images which have different color
# for i in range(1, 10):
#     images.append(image)

images = []
labels = []
for segami in range(3):
    for intensity in (0.1, 0.5, 0.9):
        splited_image = image.split()
        mid = splited_image[segami].point(lambda x: x*intensity)
        splited_image[segami].paste(mid)
        im = Image.merge(image.mode, splited_image)
        labels.append('channel {} intensity {}'.format(segami, intensity))
        images.append(im)
font = ImageFont.truetype("fanwood-webfont.ttf", 75)


# create a contact sheet from different brightnesses
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x = 0
y = 0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x = 0
        y = y+first_image.height
    else:
        x = x+first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
contact_sheet.show()

