# webcam-pnp

This project demonstrates the Perspective-n-Point (PnP) algorithm for finding a target's position and rotation in 3D space. Currently, it looks for a chessboard pattern, which is easily supported in OpenCV. This project could be extended to a game target instead to find the robot's pose (XYZ coordinates and rotation).

For more information on PnP:
https://en.wikipedia.org/wiki/Perspective-n-Point

This project also contains calibration data for the Logitech Quickcam Pro 9000. Using this calibration with other cameras is likely to result in unreliable measurements.
