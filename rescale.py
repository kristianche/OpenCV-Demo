import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)


def rescale_frame(frame, scale=.2):  # A function to rescale Images, Video and LiveVideo
    width = int(frame.shape[1] * scale)  # Decreasing the width of your frame (shape[1] - width): integer
    height = int(frame.shape[0] * scale)  # Decreasing the height of your frame (shape[0] - height): integer

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # Resizes the frame to a particular dimension


def change_res(width, height):  # Another method for Resizing which works ONLY for LiveVideo(your webcam)
    capture.set(3, width)  # 3 is for the width(integer)
    capture.set(4, height)  # 4 is for the height(integer)

    # 10 is for Brightness


resized_image = rescale_frame(img)  # Resizing an large image
cv.imshow('Resized Image', resized_image)  # Displaying the Resized image

capture = cv.VideoCapture('Videos/dog.mp4')

while True:

    is_true, frame = capture.read()

    frame_resized = rescale_frame(frame)  # Resizing the frame

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)  # Displaying the Resized Video

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()