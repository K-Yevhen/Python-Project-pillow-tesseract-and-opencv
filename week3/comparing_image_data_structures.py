import cv2 as cv
import inspect
from PIL import Image
import numpy as np


#  variable to read the image with opencv
img = cv.imread("floyd.jpg")

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# checking return of the object
# print(inspect.getmro(type(gray)))

# looking of the consisting of gray color - bites, arrays and etc
# print(gray)

image = Image.fromarray(gray, "L")
# image.show()

single_din = np.array([25, 50, 25, 10, 10])
double_din = np.array([single_din])
# print(double_din)

# Image.fromarray(double_din, "L").show()

# print(double_din.shape)
# print(img.shape)

first_pixel = img[0][0]
# print(first_pixel)

# print("Original Image")
# print(gray)
#
# print("New Image")
# image1d = np.reshape(gray, (1, gray.shape[0] * gray.shape[1]))
#
# print(image1d)

new_img = cv.imread("two_col.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# print(gray[2:4, 1:3])
# print(np.count_nonzero(gray[2:4, 1:3]))

white_metrics = np.full((12, 12), 255, dtype=np.uint8)
# Image.fromarray(white_metrics, "L").show()
# print(white_metrics)

# white_metrics[:, 6] = np.full((1, 12), 0, dtype=np.uint8)
# Image.fromarray(white_metrics, "L").show()
# print(white_metrics)

