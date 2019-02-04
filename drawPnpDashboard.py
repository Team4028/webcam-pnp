import cv2
import numpy as np

def drawPnpDashboard(translationVector, rotationVector):
    DASHBOARD_HEIGHT_PX = 325
    DASHBOARD_WIDTH_PX  = 825

    BLACK_COLOR = (  0,   0,   0)
    GRAY_COLOR  = (246, 246, 246)
    WHITE_COLOR = (255, 255, 255)

    FONT_SCALE = 1

    # TODO: calculate the game metrics

    dashboardSize = (DASHBOARD_HEIGHT_PX, DASHBOARD_WIDTH_PX, 3)
    img = np.ones(dashboardSize, dtype=np.uint8) * 255

    # PNP metrics area
    pnpAreaTopLeft     = ( 25,  62)
    pnpAreaBottomRight = (525, 300)
    cv2.rectangle(img, pnpAreaTopLeft, pnpAreaBottomRight, GRAY_COLOR, -1)
    cv2.rectangle(img, pnpAreaTopLeft, pnpAreaBottomRight, BLACK_COLOR)

    pnpMetricsLabelBottomLeft = (25, 50)
    cv2.putText(img, 'PNP metrics', pnpMetricsLabelBottomLeft, cv2.FONT_HERSHEY_DUPLEX, \
                FONT_SCALE, BLACK_COLOR)

    firstMetricRowLabelPx      = 87
    firstMetricRowTopPx        = 100
    firstMetricRowBottomPx     = 125

    secondMetricRowLabelPx     = 167
    secondMetricRowTopPx       = 175
    secondMetricRowBottomPx    = 200

    thirdMetricRowLabelPx      = 237
    thirdMetricRowTopPx        = 250
    thirdMetricRowBottomPx     = 275

    firstMetricColumnLeftPx    =  50
    firstMetricColumnCenterPx  = 150
    firstMetricColumnRightPx   = 250

    secondMetricColumnLeftPx   = 300
    secondMetricColumnCenterPx = 400
    secondMetricColumnRightPx  = 500

    thirdMetricColumnLeftPx    = 575
    thirdMetricColumnCenterPx  = 675
    thirdMetricColumnRightPx   = 775

    xTranslationBarTopLeft      = (firstMetricColumnLeftPx,   firstMetricRowTopPx)
    xTranslationBarBottomRight  = (firstMetricColumnRightPx,  firstMetricRowBottomPx)
    xTranslationBarTopCenter    = (firstMetricColumnCenterPx, firstMetricRowTopPx)
    xTranslationBarBottomCenter = (firstMetricColumnCenterPx, firstMetricRowBottomPx)
    xTranslationLabelBottomLeft = (firstMetricColumnLeftPx,   firstMetricRowLabelPx)
    cv2.rectangle(img, xTranslationBarTopLeft, xTranslationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xTranslationBarTopLeft, xTranslationBarBottomRight, BLACK_COLOR)
    cv2.line(img, xTranslationBarTopCenter, xTranslationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'X translation:', xTranslationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    yTranslationBarTopLeft     = (firstMetricColumnLeftPx,  secondMetricRowTopPx)
    yTranslationBarBottomRight = (firstMetricColumnRightPx, secondMetricRowBottomPx)
    yTranslationBarTopCenter    = (firstMetricColumnCenterPx, secondMetricRowTopPx)
    yTranslationBarBottomCenter = (firstMetricColumnCenterPx, secondMetricRowBottomPx)
    yTranslationLabelBottomLeft = (firstMetricColumnLeftPx,   secondMetricRowLabelPx)
    cv2.rectangle(img, yTranslationBarTopLeft, yTranslationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, yTranslationBarTopLeft, yTranslationBarBottomRight, BLACK_COLOR)
    cv2.line(img, yTranslationBarTopCenter, yTranslationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Y translation:', yTranslationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    zTranslationBarTopLeft     = (firstMetricColumnLeftPx,  thirdMetricRowTopPx)
    zTranslationBarBottomRight = (firstMetricColumnRightPx, thirdMetricRowBottomPx)
    zTranslationLabelBottomLeft = (firstMetricColumnLeftPx, thirdMetricRowLabelPx)
    cv2.rectangle(img, zTranslationBarTopLeft, zTranslationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, zTranslationBarTopLeft, zTranslationBarBottomRight, BLACK_COLOR)
    cv2.putText(img, 'Z translation:', zTranslationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    xRotationBarTopLeft     = (secondMetricColumnLeftPx,  firstMetricRowTopPx)
    xRotationBarBottomRight = (secondMetricColumnRightPx, firstMetricRowBottomPx)
    xRotationBarTopCenter    = (secondMetricColumnCenterPx, firstMetricRowTopPx)
    xRotationBarBottomCenter = (secondMetricColumnCenterPx, firstMetricRowBottomPx)
    xRotationLabelBottomLeft = (secondMetricColumnLeftPx,   firstMetricRowLabelPx)
    cv2.rectangle(img, xRotationBarTopLeft, xRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xRotationBarTopLeft, xRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, xRotationBarTopCenter, xRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'X rotation:', xRotationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    yRotationBarTopLeft     = (secondMetricColumnLeftPx,  secondMetricRowTopPx)
    yRotationBarBottomRight = (secondMetricColumnRightPx, secondMetricRowBottomPx)
    yRotationBarTopCenter    = (secondMetricColumnCenterPx, secondMetricRowTopPx)
    yRotationBarBottomCenter = (secondMetricColumnCenterPx, secondMetricRowBottomPx)
    yRotationLabelBottomLeft = (secondMetricColumnLeftPx,   secondMetricRowLabelPx)
    cv2.rectangle(img, yRotationBarTopLeft, yRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, yRotationBarTopLeft, yRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, yRotationBarTopCenter, yRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Y rotation:', yRotationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    zRotationBarTopLeft     = (secondMetricColumnLeftPx,  thirdMetricRowTopPx)
    zRotationBarBottomRight = (secondMetricColumnRightPx, thirdMetricRowBottomPx)
    zRotationBarTopCenter    = (secondMetricColumnCenterPx, thirdMetricRowTopPx)
    zRotationBarBottomCenter = (secondMetricColumnCenterPx, thirdMetricRowBottomPx)
    zRotationLabelBottomLeft = (secondMetricColumnLeftPx,   thirdMetricRowLabelPx)
    cv2.rectangle(img, zRotationBarTopLeft, zRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, zRotationBarTopLeft, zRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, zRotationBarTopCenter, zRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Z rotation:', zRotationLabelBottomLeft, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Game metrics area
    gameAreaTopLeft     = (550,  62)
    gameAreaBottomRight = (800, 300)
    cv2.rectangle(img, gameAreaTopLeft, gameAreaBottomRight, GRAY_COLOR, -1)
    cv2.rectangle(img, gameAreaTopLeft, gameAreaBottomRight, BLACK_COLOR)

    gameMetricsLabelBottomLeft = (550, 50)
    cv2.putText(img, 'Game metrics', gameMetricsLabelBottomLeft, cv2.FONT_HERSHEY_DUPLEX, \
                FONT_SCALE, BLACK_COLOR)

    xzDistanceBarTopLeft     = (thirdMetricColumnLeftPx,  firstMetricRowTopPx)
    xzDistanceBarBottomRight = (thirdMetricColumnRightPx, firstMetricRowBottomPx)
    cv2.rectangle(img, xzDistanceBarTopLeft, xzDistanceBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xzDistanceBarTopLeft, xzDistanceBarBottomRight, BLACK_COLOR)

    angle1BarTopLeft     = (thirdMetricColumnLeftPx,  secondMetricRowTopPx)
    angle1BarBottomRight = (thirdMetricColumnRightPx, secondMetricRowBottomPx)
    cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, BLACK_COLOR)

    angle2BarTopLeft     = (thirdMetricColumnLeftPx,  thirdMetricRowTopPx)
    angle2BarBottomRight = (thirdMetricColumnRightPx, thirdMetricRowBottomPx)
    cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, BLACK_COLOR)



    cv2.imshow('dashboard', img)
    cv2.waitKey(0)

    

if __name__ == '__main__':
    translationVector = [7.8, -4.3, 93.2]
    rotationVector = [-30.2, 5.7, -9.7]

    drawPnpDashboard(translationVector, rotationVector)
