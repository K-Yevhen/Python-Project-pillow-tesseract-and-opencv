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
contact_sheet = Image.new(first_image.mode, (first_image.width, 10*first_image.height))

current_location = 0
for img in images:
    contact_sheet.paste(img, (0, current_location))
    current_location = current_location + 450

contact_sheet = contact_sheet.resize((160, 900))
# contact_sheet.show()

contact_sheet_new = Image.new(first_image.mode, (first_image.width*3, first_image.height*3))
x = 0
y = 0

for img in images[1:]:
    contact_sheet_new.paste(img, (x, y))
    if x + first_image.width == contact_sheet_new.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

contact_sheet_new = contact_sheet_new.resize((int(contact_sheet_new.width/2), int(contact_sheet_new.height/2)))
contact_sheet_new.show()