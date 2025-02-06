import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # Creates a blank image (width, height, color)
cv.imshow('Blank', blank)

blank[:] = 0, 225, 0  # Paints the image a certain color
cv.imshow('Green', blank)

blank[200:300, 300:400] = 0, 187, 187  # Paints a only a small part of the area
cv.imshow('Blank2', blank)

cv.rectangle(blank, (0, 0), (250, 250), (225, 0, 0), thickness=0)  # Makes a rectangle out of the whole area
cv.imshow('Rectangle', blank)

cv.circle(blank, (250, 250), 40, (0, 0, 225), thickness=-1)  # Making a filled circle with radius 40
cv.imshow('Circle', blank)

cv.line(blank, (0, 0), (250, 250), (0, 0, 0), thickness=3)  # Drawing a line
cv.imshow('Line', blank)

cv.waitKey(0)