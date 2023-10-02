import kraken
from kraken import binarization, pageseg
from PIL import Image

# print(help(kraken))
# print(help(pageseg))

im = Image.open("two_col.png")
# im.show()

# bounding_boxes = pageseg.segment(im.convert('1'))['boxes']
# print(bounding_boxes)

def show_boxes(img):
    '''Modifies the passed image to show a series of bounding boxes on an image as run by kraken

    :param img: A PIL.Image object
    :return img: The modified PIL.Image object
    '''
    from PIL import ImageDraw
    # And grab a drawing object to annotate that image
    drawing_object = ImageDraw.Draw(img)
    # We can create a set of boxes using pageseg.segment
    bw_im = binarization.nlbin(img)
    bounding_boxes = pageseg.segment(bw_im, black_colseps=True)['boxes']
    # Now lets go through the list of bounding boxes
    for box in bounding_boxes:
        # An just draw a nice rectangle
        drawing_object.rectangle(box, fill=None, outline='red')
    # And to make it easy, lets return the image object
    return img

# print(show_boxes(Image.open('two_col.png')).show())

char_width = 25


def calculate_line_height(img):
    bw_im = binarization.nlbin(img)
    bounding_boxes = pageseg.segment(bw_im)['boxes']
    height_accumulator = 0
    for box in bounding_boxes:
        height_accumulator = height_accumulator + box[3] - box[1]
    return int(height_accumulator / len(bounding_boxes))


line_height = calculate_line_height(Image.open("two_col.png"))
# print(line_height)

gap_box = (0, 0, char_width, line_height*6)
# print(gap_box)


def gap_check(img, location):
    for x in range(location[0], location[0] + gap_box[2]):
        for y in range(location[1], location[1] + gap_box[3]):
            if x < img.width and y < img.height:
                if img.getpixel((x, y)) != 255:
                    return False

    return True


def draw_sep(img, location):
    from PIL import ImageDraw
    drawing_object = ImageDraw.Draw(img)
    x1 = location[0] + int(gap_box[2] / 2)
    x2 = x1
    y1 = location[1]
    y2 = y1 + gap_box[3]
    drawing_object.rectangle((x1, y1, x2, y2), fill='black', outline='black')


def process_image(img):
    for x in range(img.width):
        for y in range(img.height):
            if gap_check(img, (x, y)):
                draw_sep(img, (x, y))
    return img


i = Image.open("two_col.png").convert('L')
i = process_image(i)
# i.show()
show_boxes(i).show()
