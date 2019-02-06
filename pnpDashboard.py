import cv2
import math
import numpy as np


DASHBOARD_HEIGHT_PX = 325
DASHBOARD_WIDTH_PX  = 825

X_TRANSLATION_MAX_INCHES =  48
Y_TRANSLATION_MAX_INCHES =  48
Z_TRANSLATION_MAX_INCHES = 180

X_ROTATION_MAX_DEGREES = 90
Y_ROTATION_MAX_DEGREES = 90
Z_ROTATION_MAX_DEGREES = 90

XZ_DISTANCE_MAX_INCHES = 180

BLACK_COLOR = (  0,   0,   0)
BLUE_COLOR  = (255, 231,  92)
GRAY_COLOR  = (246, 246, 246)
WHITE_COLOR = (255, 255, 255)

FONT_SCALE = 1

METRIC_BAR_WIDTH_PX  = 200
METRIC_BAR_HEIGHT_PX =  25


def drawBipolarMeter(img, metric, metricLimit, topLeft):
    metricFraction = metric / metricLimit
    meterWidthPx = int(METRIC_BAR_WIDTH_PX / 2 * min(1.0, metricFraction))
    barHalfWidthPx = int(METRIC_BAR_WIDTH_PX / 2)

    barTopCenter    = (topLeft[0] + barHalfWidthPx, topLeft[1])
    barBottomCenter = (topLeft[0] + barHalfWidthPx, topLeft[1] + METRIC_BAR_HEIGHT_PX)
    barBottomRight   = (topLeft[0] + METRIC_BAR_WIDTH_PX, topLeft[1] + METRIC_BAR_HEIGHT_PX)

    meterBottomRight = (barBottomCenter[0] + meterWidthPx, barBottomCenter[1])

    cv2.rectangle(img, topLeft, barBottomRight,   WHITE_COLOR, -1)
    cv2.rectangle(img, barTopCenter, meterBottomRight, BLUE_COLOR,  -1)
    cv2.rectangle(img, topLeft, barBottomRight,   BLACK_COLOR)
    cv2.line(img, barTopCenter, barBottomCenter, BLACK_COLOR)

def drawUnipolarMeter(img, metric, metricLimit, topLeft):
    metricFraction = metric / metricLimit
    meterWidthPx = int(METRIC_BAR_WIDTH_PX * min(1.0, metricFraction))

    meterBottomRight = (topLeft[0] + meterWidthPx, topLeft[1] + METRIC_BAR_HEIGHT_PX)
    barBottomRight   = (topLeft[0] + METRIC_BAR_WIDTH_PX, topLeft[1] + METRIC_BAR_HEIGHT_PX)

    cv2.rectangle(img, topLeft, barBottomRight,   WHITE_COLOR, -1)
    cv2.rectangle(img, topLeft, meterBottomRight, BLUE_COLOR,  -1)
    cv2.rectangle(img, topLeft, barBottomRight,   BLACK_COLOR)

def drawMetricLabel(img, labelString, anchor):
    cv2.putText(img, labelString, anchor, cv2.FONT_HERSHEY_PLAIN, FONT_SCALE, BLACK_COLOR)

def drawAmountLabel(img, metric, anchor, unitString):
    amountString = '{:.2f}{}'.format(metric, unitString)
    cv2.putText(img, amountString, anchor, cv2.FONT_HERSHEY_PLAIN, FONT_SCALE, BLACK_COLOR)


def drawPnpDashboard(translationVector, rotationVector):
    xTranslationInches = translationVector[0]
    yTranslationInches = translationVector[1]
    zTranslationInches = translationVector[2]

    xRotationRadians = rotationVector[0]
    yRotationRadians = rotationVector[1]
    zRotationRadians = rotationVector[2]

    xRotationDegrees = xRotationRadians * 180 / math.pi
    yRotationDegrees = yRotationRadians * 180 / math.pi
    zRotationDegrees = zRotationRadians * 180 / math.pi

    # TODO: calculate the game metrics
    xzDistanceInches = math.sqrt(xTranslationInches**2 + zTranslationInches**2)

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

    secondMetricRowLabelPx     = 167
    secondMetricRowTopPx       = 175

    thirdMetricRowLabelPx      = 237
    thirdMetricRowTopPx        = 250

    firstMetricColumnLeftPx    =  50
    secondMetricColumnLeftPx   = 300
    thirdMetricColumnLeftPx    = 575

    # Draw X translation section
    xTranslationBarTopLeft      = (firstMetricColumnLeftPx,   firstMetricRowTopPx)
    xTranslationLabelTextAnchor = (firstMetricColumnLeftPx,   firstMetricRowLabelPx)
    xTranslationAmountTextAnchor = (175, firstMetricRowLabelPx)

    drawBipolarMeter(img, xTranslationInches, X_TRANSLATION_MAX_INCHES, xTranslationBarTopLeft)
    drawMetricLabel(img, 'X translation:', xTranslationLabelTextAnchor)
    drawAmountLabel(img, xTranslationInches, xTranslationAmountTextAnchor, '"')

    # Draw Y translation section
    yTranslationBarTopLeft     = (firstMetricColumnLeftPx,  secondMetricRowTopPx)
    yTranslationLabelTextAnchor = (firstMetricColumnLeftPx,   secondMetricRowLabelPx)
    yTranslationAmountTextAnchor = (175, secondMetricRowLabelPx)

    drawBipolarMeter(img, yTranslationInches, Y_TRANSLATION_MAX_INCHES, yTranslationBarTopLeft)
    drawMetricLabel(img, 'Y translation:', yTranslationLabelTextAnchor)
    drawAmountLabel(img, yTranslationInches, yTranslationAmountTextAnchor, '"')

    # Draw Z translation section
    zTranslationBarTopLeft     = (firstMetricColumnLeftPx,  thirdMetricRowTopPx)
    zTranslationLabelTextAnchor = (firstMetricColumnLeftPx, thirdMetricRowLabelPx)
    zTranslationAmountTextAnchor = (175, thirdMetricRowLabelPx)

    drawUnipolarMeter(img, zTranslationInches, Z_TRANSLATION_MAX_INCHES, zTranslationBarTopLeft)
    drawMetricLabel(img, 'Z translation:', zTranslationLabelTextAnchor)
    drawAmountLabel(img, zTranslationInches, zTranslationAmountTextAnchor, '"')

    # Draw X rotation section
    xRotationBarTopLeft     = (secondMetricColumnLeftPx,  firstMetricRowTopPx)
    xRotationLabelTextAnchor = (secondMetricColumnLeftPx,   firstMetricRowLabelPx)
    xRotationAmountTextAnchor = (400, firstMetricRowLabelPx)

    drawBipolarMeter(img, xRotationDegrees, X_ROTATION_MAX_DEGREES, xRotationBarTopLeft)
    drawMetricLabel(img, 'X rotation:', xRotationLabelTextAnchor)
    drawAmountLabel(img, xRotationDegrees, xRotationAmountTextAnchor, ' deg')

    # Draw Y rotation section
    yRotationBarTopLeft     = (secondMetricColumnLeftPx,  secondMetricRowTopPx)
    yRotationLabelTextAnchor = (secondMetricColumnLeftPx,   secondMetricRowLabelPx)
    yRotationAmountTextAnchor = (400, secondMetricRowLabelPx)

    drawBipolarMeter(img, yRotationDegrees, Y_ROTATION_MAX_DEGREES, yRotationBarTopLeft)
    drawMetricLabel(img, 'Y rotation:', yRotationLabelTextAnchor)
    drawAmountLabel(img, yRotationDegrees, yRotationAmountTextAnchor, ' deg')

    # Draw Z rotation section
    zRotationBarTopLeft     = (secondMetricColumnLeftPx,  thirdMetricRowTopPx)
    zRotationLabelTextAnchor = (secondMetricColumnLeftPx,   thirdMetricRowLabelPx)
    zRotationAmountTextAnchor = (400, thirdMetricRowLabelPx)

    drawBipolarMeter(img, zRotationDegrees, Z_ROTATION_MAX_DEGREES, zRotationBarTopLeft)
    drawMetricLabel(img, 'Z rotation:', zRotationLabelTextAnchor)
    drawAmountLabel(img, zRotationDegrees, zRotationAmountTextAnchor, ' deg')

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
    xzDistanceLabelTextAnchor = (thirdMetricColumnLeftPx, firstMetricRowLabelPx)
    xzDistanceAmountTextAnchor = (687, firstMetricRowLabelPx)

    drawUnipolarMeter(img, xzDistanceInches, XZ_DISTANCE_MAX_INCHES, xzDistanceBarTopLeft)
    drawMetricLabel(img, 'XZ distance:', xzDistanceLabelTextAnchor)
    drawAmountLabel(img, xzDistanceInches, xzDistanceAmountTextAnchor, '"')

    # Draw angle 1 section
    # angle1BarTopLeft     = (thirdMetricColumnLeftPx,  secondMetricRowTopPx)
    # angle1BarBottomRight = (thirdMetricColumnRightPx, secondMetricRowBottomPx)
    # cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, WHITE_COLOR, -1)
    # cv2.rectangle(img, angle1BarTopLeft, angle1BarBottomRight, BLACK_COLOR)

    # Draw angle 2 section
    # angle2BarTopLeft     = (thirdMetricColumnLeftPx,  thirdMetricRowTopPx)
    # angle2BarBottomRight = (thirdMetricColumnRightPx, thirdMetricRowBottomPx)
    # cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, WHITE_COLOR, -1)
    # cv2.rectangle(img, angle2BarTopLeft, angle2BarBottomRight, BLACK_COLOR)

    cv2.imshow('dashboard', img)

    

if __name__ == '__main__':
    translationVector = [7.8, -4.3, 93.2]
    rotationVector = [-30.2, 5.7, -9.7]

    drawPnpDashboard(translationVector, rotationVector)
    cv2.waitKey(0)
