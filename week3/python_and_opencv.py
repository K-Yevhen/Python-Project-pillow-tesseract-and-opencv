import cv2 as cv
from PIL import Image, ImageDraw

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")

img = cv.imread('floyd.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

# print(faces)
# print(faces.tolist()[0])

pil_img = Image.fromarray(gray, mode="L")
drawing = ImageDraw.Draw(pil_img)

rec = faces.tolist()[0]
drawing.rectangle(rec, outline="white")
# pil_img.show()

drawing.rectangle((rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3]), outline="white")
# pil_img.show()

new_img = cv.imread("msi_recruitment.gif")
# Image.fromarray(new_img)

pil_img = Image.open("msi_recruitment.gif")
open_cv_version = pil_img.convert("L")
# open_cv_version.save("msi_recruitment.png")
#
cv_img = cv.imread("msi_recruitment.png")
faces = face_cascade.detectMultiScale(cv_img)

# pil_img = Image.open("msi_recruitment.gif")
# pil_img = pil_img.convert("RGB")
# drawing = ImageDraw.Draw(pil_img)

for x, y, w, h in faces:
    drawing.rectangle((x, y, x+w, y+h), outline="white")
# pil_img.show()

# print(pil_img.mode)


def show_rects(faces):
    pil_img = Image.open("msi_recruitment.gif").convert("RGB")
    drawing = ImageDraw.Draw(pil_img)
    for x, y, w, h in faces:
        drawing.rectangle((x, y, x + w, y + h), outline="white")
    pil_img.show()


cv_img_bin = cv.threshold(img, 120, 255, cv.THRESH_BINARY)[1]
# faces = face_cascade.detectMultiScale(cv_img_bin)
faces = face_cascade.detectMultiScale(cv_img_bin, 1.05)
show_rects(faces)
faces = face_cascade.detectMultiScale(cv_img_bin, 1.15)
show_rects(faces)
faces = face_cascade.detectMultiScale(cv_img_bin, 1.25)
show_rects(faces)
