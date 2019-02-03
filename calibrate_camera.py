import cv2
import glob
import numpy as np

NUM_CHESSBOARD_ROW_CORNERS = 5
NUM_CHESSBOARD_COL_CORNERS = 8

numTotalChessboardCorners = NUM_CHESSBOARD_ROW_CORNERS * NUM_CHESSBOARD_COL_CORNERS

chessboardPoints3dList = np.zeros((numTotalChessboardCorners, 3), np.float32)
chessboardPoints3dList[:, :2] = \
    np.mgrid[0 : NUM_CHESSBOARD_COL_CORNERS, 0 : NUM_CHESSBOARD_ROW_CORNERS].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objectPoint3dList = []
imagePoint2dList  = []

imagePathList = glob.glob('calibration_images/*.png')

# Find the image points that correspond to the chessboard in all calibration images
for imagePath in imagePathList:
    bgrImg = cv2.imread(imagePath)

    grayImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2GRAY)

    numChessboardCornersPair = (NUM_CHESSBOARD_COL_CORNERS, NUM_CHESSBOARD_ROW_CORNERS)
    isChessboardFoundInImg, chessboardCorner2dList = \
        cv2.findChessboardCorners(grayImg, numChessboardCornersPair, None)

    assert isChessboardFoundInImg, 'Chessboard not found in image {}'.format(imagePath)

    objectPoint3dList.append(chessboardPoints3dList)
    imagePoint2dList.append(chessboardCorner2dList)

# Calculate the calibrated intrinsic camera parameters
rmsReprojectionError, cameraMatrix, distortionCoefficients, rotationVectors, translationVectors = \
    cv2.calibrateCamera(objectPoint3dList, imagePoint2dList, grayImg.shape[::-1], None, None)

# Save corrected versions of all calibration images
for imagePath in imagePathList:
    bgrImg = cv2.imread(imagePath)
    correctedBgrImg = cv2.undistort(bgrImg, cameraMatrix, distortionCoefficients)

    correctedImagePath = imagePath + '__corrected.png'
    cv2.imwrite(correctedImagePath, correctedBgrImg)

# Save the resulting calibrated intrinsic camera parameters to text files
np.savetxt('cameraMatrix.txt',           cameraMatrix)
np.savetxt('distortionCoefficients.txt', distortionCoefficients)