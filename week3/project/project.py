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


def open_zipfile(file):
    with ZipFile(file=file, mode='r') as zf:
        for file_info in zf.infolist():
            print("File:", file_info.filename)
        # zf.printdir()
        with zf.open(file_info.filename) as images:
            img = Image.open(images)
            img.show()

print(open_zipfile("small_img.zip"))