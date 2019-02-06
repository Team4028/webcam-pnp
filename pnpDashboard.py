import cv2
import numpy as np


DASHBOARD_HEIGHT_PX = 325
DASHBOARD_WIDTH_PX  = 825

Z_TRANSLATION_MAX_INCHES = 180

BLACK_COLOR = (  0,   0,   0)
BLUE_COLOR  = (255, 231,  92)
GRAY_COLOR  = (246, 246, 246)
WHITE_COLOR = (255, 255, 255)

FONT_SCALE = 1

METRIC_BAR_WIDTH_PX  = 200
METRIC_BAR_HEIGHT_PX =  25


def drawUnipolarMeter(img, metric, metricLimit, topLeft):
    metricFraction = metric / metricLimit
    meterWidthPx = int(METRIC_BAR_WIDTH_PX * min(1.0, metricFraction))

    meterBottomRight = (topLeft[0] + meterWidthPx, topLeft[1] + METRIC_BAR_HEIGHT_PX)
    barBottomRight   = (topLeft[0] + METRIC_BAR_WIDTH_PX, topLeft[1] + METRIC_BAR_HEIGHT_PX)

    cv2.rectangle(img, topLeft, barBottomRight,   WHITE_COLOR, -1)
    cv2.rectangle(img, topLeft, meterBottomRight, BLUE_COLOR,  -1)
    cv2.rectangle(img, topLeft, barBottomRight,   BLACK_COLOR)


def drawPnpDashboard(translationVector, rotationVector):
    # TODO: calculate the game metrics

    dashboardSize = (DASHBOARD_HEIGHT_PX, DASHBOARD_WIDTH_PX, 3)
    img = np.ones(dashboardSize, dtype=np.uint8) * 255

    # PNP metrics area
    pnpAreaTopLeft     = ( 25,  62)
    pnpAreaBottomRight = (525, 300)
    cv2.rectangle(img, pnpAreaTopLeft, pnpAreaBottomRight, GRAY_COLOR, -1)
    cv2.rectangle(img, pnpAreaTopLeft, pnpAreaBottomRight, BLACK_COLOR)

    pnpMetricsLabelTextAnchor = (25, 50)
    cv2.putText(img, 'PNP metrics', pnpMetricsLabelTextAnchor, cv2.FONT_HERSHEY_DUPLEX, \
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

    # Draw X translation section
    xTranslationBarTopLeft      = (firstMetricColumnLeftPx,   firstMetricRowTopPx)
    xTranslationBarBottomRight  = (firstMetricColumnRightPx,  firstMetricRowBottomPx)
    xTranslationBarTopCenter    = (firstMetricColumnCenterPx, firstMetricRowTopPx)
    xTranslationBarBottomCenter = (firstMetricColumnCenterPx, firstMetricRowBottomPx)
    xTranslationLabelTextAnchor = (firstMetricColumnLeftPx,   firstMetricRowLabelPx)
    cv2.rectangle(img, xTranslationBarTopLeft, xTranslationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xTranslationBarTopLeft, xTranslationBarBottomRight, BLACK_COLOR)
    cv2.line(img, xTranslationBarTopCenter, xTranslationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'X translation:', xTranslationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Draw Y translation section
    yTranslationBarTopLeft     = (firstMetricColumnLeftPx,  secondMetricRowTopPx)
    yTranslationBarBottomRight = (firstMetricColumnRightPx, secondMetricRowBottomPx)
    yTranslationBarTopCenter    = (firstMetricColumnCenterPx, secondMetricRowTopPx)
    yTranslationBarBottomCenter = (firstMetricColumnCenterPx, secondMetricRowBottomPx)
    yTranslationLabelTextAnchor = (firstMetricColumnLeftPx,   secondMetricRowLabelPx)
    cv2.rectangle(img, yTranslationBarTopLeft, yTranslationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, yTranslationBarTopLeft, yTranslationBarBottomRight, BLACK_COLOR)
    cv2.line(img, yTranslationBarTopCenter, yTranslationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Y translation:', yTranslationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Draw Z translation section
    zTranslationBarTopLeft     = (firstMetricColumnLeftPx,  thirdMetricRowTopPx)
    zTranslationLabelTextAnchor = (firstMetricColumnLeftPx, thirdMetricRowLabelPx)
    zTranslationInches = translationVector[2]

    drawUnipolarMeter(img, zTranslationInches, Z_TRANSLATION_MAX_INCHES, zTranslationBarTopLeft)

    zTranslationAmountString = '{:.2f}"'.format(zTranslationInches)
    zTranslationAmountTextAnchor = (175, thirdMetricRowLabelPx)

    cv2.putText(img, 'Z translation:', zTranslationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)
    cv2.putText(img, zTranslationAmountString, zTranslationAmountTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Draw X rotation section
    xRotationBarTopLeft     = (secondMetricColumnLeftPx,  firstMetricRowTopPx)
    xRotationBarBottomRight = (secondMetricColumnRightPx, firstMetricRowBottomPx)
    xRotationBarTopCenter    = (secondMetricColumnCenterPx, firstMetricRowTopPx)
    xRotationBarBottomCenter = (secondMetricColumnCenterPx, firstMetricRowBottomPx)
    xRotationLabelTextAnchor = (secondMetricColumnLeftPx,   firstMetricRowLabelPx)
    cv2.rectangle(img, xRotationBarTopLeft, xRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xRotationBarTopLeft, xRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, xRotationBarTopCenter, xRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'X rotation:', xRotationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Draw Y rotation section
    yRotationBarTopLeft     = (secondMetricColumnLeftPx,  secondMetricRowTopPx)
    yRotationBarBottomRight = (secondMetricColumnRightPx, secondMetricRowBottomPx)
    yRotationBarTopCenter    = (secondMetricColumnCenterPx, secondMetricRowTopPx)
    yRotationBarBottomCenter = (secondMetricColumnCenterPx, secondMetricRowBottomPx)
    yRotationLabelTextAnchor = (secondMetricColumnLeftPx,   secondMetricRowLabelPx)
    cv2.rectangle(img, yRotationBarTopLeft, yRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, yRotationBarTopLeft, yRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, yRotationBarTopCenter, yRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Y rotation:', yRotationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Draw Z rotation section
    zRotationBarTopLeft     = (secondMetricColumnLeftPx,  thirdMetricRowTopPx)
    zRotationBarBottomRight = (secondMetricColumnRightPx, thirdMetricRowBottomPx)
    zRotationBarTopCenter    = (secondMetricColumnCenterPx, thirdMetricRowTopPx)
    zRotationBarBottomCenter = (secondMetricColumnCenterPx, thirdMetricRowBottomPx)
    zRotationLabelTextAnchor = (secondMetricColumnLeftPx,   thirdMetricRowLabelPx)
    cv2.rectangle(img, zRotationBarTopLeft, zRotationBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, zRotationBarTopLeft, zRotationBarBottomRight, BLACK_COLOR)
    cv2.line(img, zRotationBarTopCenter, zRotationBarBottomCenter, BLACK_COLOR)
    cv2.putText(img, 'Z rotation:', zRotationLabelTextAnchor, cv2.FONT_HERSHEY_PLAIN, \
                FONT_SCALE, BLACK_COLOR)

    # Game metrics area
    gameAreaTopLeft     = (550,  62)
    gameAreaBottomRight = (800, 300)
    cv2.rectangle(img, gameAreaTopLeft, gameAreaBottomRight, GRAY_COLOR, -1)
    cv2.rectangle(img, gameAreaTopLeft, gameAreaBottomRight, BLACK_COLOR)

    gameMetricsLabelTextAnchor = (550, 50)
    cv2.putText(img, 'Game metrics', gameMetricsLabelTextAnchor, cv2.FONT_HERSHEY_DUPLEX, \
                FONT_SCALE, BLACK_COLOR)

    # Draw XZ distance section
    xzDistanceBarTopLeft     = (thirdMetricColumnLeftPx,  firstMetricRowTopPx)
    xzDistanceBarBottomRight = (thirdMetricColumnRightPx, firstMetricRowBottomPx)
    cv2.rectangle(img, xzDistanceBarTopLeft, xzDistanceBarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, xzDistanceBarTopLeft, xzDistanceBarBottomRight, BLACK_COLOR)

    # Draw angle 1 section
    angle1BarTopLeft     = (thirdMetricColumnLeftPx,  secondMetricRowTopPx)
    angle1BarBottomRight = (thirdMetricColumnRightPx, secondMetricRowBottomPx)
    cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, BLACK_COLOR)

    # Draw angle 2 section
    angle2BarTopLeft     = (thirdMetricColumnLeftPx,  thirdMetricRowTopPx)
    angle2BarBottomRight = (thirdMetricColumnRightPx, thirdMetricRowBottomPx)
    cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, WHITE_COLOR, -1)
    cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, BLACK_COLOR)

    cv2.imshow('dashboard', img)

    

if __name__ == '__main__':
    translationVector = [7.8, -4.3, 93.2]
    rotationVector = [-30.2, 5.7, -9.7]

    drawPnpDashboard(translationVector, rotationVector)
    cv2.waitKey(0)
