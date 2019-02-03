import cv2
import numpy as np


NUM_CHESSBOARD_ROW_CORNERS = 5
NUM_CHESSBOARD_COL_CORNERS = 8

# These indices correspond to the available cameras on a given computer. It is 
# not known how to request a specific camera by name or other method  besides 
# its index.
CAMERA_DEVICE_INDEX = 1

videoCapture = cv2.VideoCapture(CAMERA_DEVICE_INDEX)

if not videoCapture.isOpened():
    print('Camera not opened')
    exit()

while(True):
    isFrameRead, img = videoCapture.read()

    if isFrameRead:
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        numChessboardCornersPair = (NUM_CHESSBOARD_ROW_CORNERS, NUM_CHESSBOARD_COL_CORNERS)
        isChessboardFoundInImg, corners = \
            cv2.findChessboardCorners(grayImg, numChessboardCornersPair, \
                                      None, cv2.CALIB_CB_FAST_CHECK)

        cv2.drawChessboardCorners(img, numChessboardCornersPair, corners, isChessboardFoundInImg)
        cv2.imshow('img', img)

        keyPressed = cv2.waitKey(1)

        isQuitKeyPressed = keyPressed & 0xFF == ord('q')
        if isQuitKeyPressed:
            break
    else:
        print('No frame read')


videoCapture.release()
cv2.destroyAllWindows()
