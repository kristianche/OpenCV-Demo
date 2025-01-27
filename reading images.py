import cv2 as cv

img = cv.imread('Photos/cat_large.jpg') #reading the image

cv.imshow('Cat', img) #displays the img in a new window with a certain name

cv.waitKey(0)