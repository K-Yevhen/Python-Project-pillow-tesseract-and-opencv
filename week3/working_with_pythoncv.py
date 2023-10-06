import cv2 as cv
import inspect


img = cv.imread("floyd.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(inspect.getmro(type(gray)))
