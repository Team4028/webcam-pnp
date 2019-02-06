import cv2
from datetime import datetime

# These indices correspond to the available cameras on a given computer. It is 
# not known how to request a specific camera by name or other method  besides 
# its index.
CAMERA_DEVICE_INDEX = 1

FRAME_PERIOD_MILLISECONDS = 5000

TIMESTAMP_FORMAT_STRING = '%Y-%m-%d_%H-%M-%S'

videoCapture = cv2.VideoCapture(CAMERA_DEVICE_INDEX)

if not videoCapture.isOpened():
    print('Camera not opened')
    exit()

while(True):
    isFrameRead, img = videoCapture.read()

    if isFrameRead:
        currentTime = datetime.now()
        currentTimeString = currentTime.strftime(TIMESTAMP_FORMAT_STRING)

        cv2.imwrite(currentTimeString + '.png', img)

        cv2.imshow('img', img)

        keyPressed = cv2.waitKey(FRAME_PERIOD_MILLISECONDS)

        isQuitKeyPressed = keyPressed & 0xFF == ord('q')
        if isQuitKeyPressed:
            break
    else:
        print('No frame read')


videoCapture.release()
cv2.destroyAllWindows()
