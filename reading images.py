import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')  # Reading the image

cv.imshow('Cat', img)  # Displays the img in a new window with a certain name

cv.waitKey(0)