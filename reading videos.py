import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')

# You can pass as an arguments in VideoCapture and integer( 0 for your webcam ) or a path to the video file

while True:  # We are losing a While Loop to read the video frame by frame

    is_true, frame = capture.read()
    # Reads the video frame by frame and return the frame and a boolean which says whether the frame was read or not

    cv.imshow('Video', frame)  # Displays the frame

    if cv.waitKey(20) and 0xFF == ord('d'):  # If the letter d is pressed break out of this loop and stop the video
        break

capture.release()
cv.destroyAllWindows()