import cv2
import numpy as np


NUM_CHESSBOARD_ROW_CORNERS = 5
NUM_CHESSBOARD_COL_CORNERS = 8

# These indices correspond to the available cameras on a given computer. It is 
# not known how to request a specific camera by name or other method  besides 
# its index.
CAMERA_DEVICE_INDEX = 1

CAMERA_CALIBRATION_DIRECTORY = 'logitech-quickcam-pro-9000-calibration'

cameraMatrix           = np.loadtxt(CAMERA_CALIBRATION_DIRECTORY + '/cameraMatrix.txt')
distortionCoefficients = np.loadtxt(CAMERA_CALIBRATION_DIRECTORY + '/distortionCoefficients.txt')

numTotalChessboardCorners = NUM_CHESSBOARD_ROW_CORNERS * NUM_CHESSBOARD_COL_CORNERS

chessboardPoints3dList = np.zeros((numTotalChessboardCorners, 3), np.float32)
chessboardPoints3dList[:, :2] = \
    np.mgrid[0 : NUM_CHESSBOARD_COL_CORNERS, 0 : NUM_CHESSBOARD_ROW_CORNERS].T.reshape(-1,2)

videoCapture = cv2.VideoCapture(CAMERA_DEVICE_INDEX)

if not videoCapture.isOpened():
    print('Camera not opened')
    exit()

while(True):
    isFrameRead, bgrImg = videoCapture.read()

    if isFrameRead:
        grayImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2GRAY)

        numChessboardCornersPair = (NUM_CHESSBOARD_COL_CORNERS, NUM_CHESSBOARD_ROW_CORNERS)
        isChessboardFoundInImg, chessboardCorner2dList = \
            cv2.findChessboardCorners(grayImg, numChessboardCornersPair, None, cv2.CALIB_CB_FAST_CHECK)

        if isChessboardFoundInImg:
            idkSomeReturnValue, rotationVector, translationVector = \
                cv2.solvePnP(chessboardPoints3dList, chessboardCorner2dList, cameraMatrix, distortionCoefficients)
    
            assert idkSomeReturnValue

            # See opencv docs for Rodrigues for formatting of rotation matrix
            rotationMatrix, _ = cv2.Rodrigues(rotationVector)
            xRotation = rotationMatrix[2, 1]
            yRotation = rotationMatrix[0, 2]
            zRotation = rotationMatrix[1, 0]
            xyzRotationVector = [xRotation, yRotation, zRotation]
    
            print('Rotation vector: {}\nTranslation vector: {}'.format(xyzRotationVector, translationVector.T))

        cv2.drawChessboardCorners(bgrImg, numChessboardCornersPair, chessboardCorner2dList, isChessboardFoundInImg)
        cv2.imshow('img', cv2.resize(bgrImg, None, fx = 0.5, fy = 0.5))

        keyPressed = cv2.waitKey(1)

        isQuitKeyPressed = keyPressed & 0xFF == ord('q')
        if isQuitKeyPressed:
            break
    else:
        print('No frame read')


videoCapture.release()
cv2.destroyAllWindows()
