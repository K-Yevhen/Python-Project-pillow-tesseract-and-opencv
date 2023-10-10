from zipfile import ZipFile
from PIL import Image, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# the rest is up to you!

# print(help(zipfile))
# img = Image.open('small_img.zip')

images = {}
name_list = []

def open_zipfile(file):
    with ZipFile(file=file, mode="r") as zf:
        for files in zf.infolist():
            # print("file:", files.filename)
            name_list.append(files.filename)
            images[files.filename] = Image.open(zf.open(files.filename))


if __name__ == '__main__':
    open_zipfile('images.zip')


print(open_zipfile("images.zip"))

