import PIL
from PIL import Image, ImageEnhance, ImageDraw
from IPython.display import display

# read image and convert to RGB
image = Image.open("msi_recruitment.gif")
image = image.convert('RGB')

# build a list of 9 images which have different color
images = []
for i in range(1, 10):
    images.append(image)

# create a contact sheet from different brightnesses
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x1 = 0
y1 = 0

row1 = []
row2 = []
row3 = []
intensity = .1
width, height = image.size

for img in images[0:3]:
    for y in range(height):
        for x in range(width):
            current_color1 = img.getpixel((x, y))
            r1, g1, b1 = current_color1
            updated = (r1) * intensity
            new_color1 = ((int(updated)), (int(g1)), (int(b1)))
            img.putpixel((x, y), new_color1)
    intensity = intensity + .4
    row1.append(img)

for img in images[3:6]:
    for y in range(height):
        for x in range(width):
            current_color2 = img.getpixel((x, y))
            r2, g2, b2 = current_color2
            new_color2 = ((int(r2)), (int(g2 * intensity)), (int(b2)))
            img.putpixel((x, y), new_color2)
    intensity = intensity + .4
    row2.append(img)

for img in images[6:]:
    for y in range(height):
        for x in range(width):
            current_color3 = img.getpixel((x, y))
            r3, g3, b3 = current_color3
            new_color3 = ((int(r3)), (int(g3)), (int(b3 * intensity)))
            img.putpixel((x, y), new_color3)
    intensity = intensity + .4
    row3.append(img)

finallist = row1 + row2 + row3

for img in finallist:
    contact_sheet.paste(img, (x1, y1))
    if x1 + first_image.width == contact_sheet.width:
        x1 = 0
        y1 = y1 + first_image.height
    else:
        x1 = x1 + first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
contact_sheet.show()

