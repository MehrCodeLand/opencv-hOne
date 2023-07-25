import cv2 as cv

img = cv.imread('image/cat-1.jpeg')

cv.imshow('Cat' , img)

cv.waitKey(0)