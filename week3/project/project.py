from zipfile import ZipFile
from PIL import Image, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
from ipywebrtc import display
import os


# loading the face detection classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# the rest is up to you!

# print(help(zipfile))
# img = Image.open('small_img.zip')


# writing the function to open zip files and appending to the variables
def open_zipfile(file):
    with ZipFile(file=file, mode="r") as zf:
        for files in zf.infolist():
            print("file:", files.filename)
            Image.open(zf.open(files.filename)).show()


# print(open_zipfile("images.zip"))

# os.mkdir('images')
# path_zip = 'images.zip'
# open_zip = ZipFile(path_zip, 'r')
# open_zip.extractall('images')
# open_zip.close()
#
#
# os.mkdir('small_image.png')
# path_zip = 'small_img.zip'
# open_zip = ZipFile(path_zip, 'r')
# open_zip.extractall('small_image.png')
# open_zip.close()

# pages_list = os.listdir('small_image.png')
# global_data_structure = []
# for name_file in pages_list:
#     local_list = []
#     local_list.append(name_file)
#     img = Image.open("small_image.png/"+name_file)
#     local_list.append(pytesseract.image_to_string(img).replace("-\n", ""))
#     global_data_structure.append(local_list)

pages_list = os.listdir('images')
global_data_structure = []
for name_file in pages_list:
    local_list = []
    local_list.append(name_file)
    img = Image.open("images/"+name_file)
    local_list.append(pytesseract.image_to_string(img).replace("-\n", ""))
    global_data_structure.append(local_list)

def finding_name(name, folder):
    for local_list in global_data_structure:
        if name in local_list[1]:
            print("Results found in file", local_list[0])

            try:
                img = Image.open(str(folder+local_list[0]))
                faces = (face_cascade.detectMultiScale(np.array(img), 1.35, 4)).tolist()

                faces_each = []

                for x, y, w, h in faces:
                    faces_each.append(img.crop((x, y, x+w, y+w )))
                    # display((img.crop((x,y,x+w,y+h))).resize((110,110)))
                    img.crop((x, y, x + w, y + h))

                contact_sheet = Image.new(img.mode, (550, 110 * int(np.ceil(len(faces_each)/5))))
                x = 0
                y = 0

                for face in faces_each:
                    face.thumbnail((110, 110))
                    contact_sheet.paste(face, (x, y))

                    if x + 100 == contact_sheet.width:
                        x = 0
                        y = y + 110
                    else:
                        x = x + 110

                contact_sheet.show()
            except:
                print("There weren't find any faces in that file!")


print(finding_name("Mark", "images/"))
