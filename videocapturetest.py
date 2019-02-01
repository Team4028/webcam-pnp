import cv2
import numpy as np

videoCapture = cv2.VideoCapture(0)

if not videoCapture.isOpened():
    print('Camera not opened')
    exit()

while(True):
    isFrameRead, frame = videoCapture.read()

    if isFrameRead:
        cv2.imshow('test', frame)

        keyPressed = cv2.waitKey(1)

        isQuitKeyPressed = keyPressed & 0xFF == ord('q')
        if isQuitKeyPressed:
            break
    else:
        print('No frame read')


videoCapture.release()
cv2.destroyAllWindows()
