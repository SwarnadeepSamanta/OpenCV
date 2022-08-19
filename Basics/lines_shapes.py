import cv2
import numpy as np

# creating canvas of 500X500 (Three Channels)
canvas = np.zeros((500, 500, 3))

# Drawing a line
cv2.line(canvas, (0, 0), (100, 100), (0, 255, 0), 2, cv2.LINE_4)
cv2.line(canvas, (0, 40), (140, 140), (0, 255, 0), 2, cv2.LINE_AA)

# line_4 and line_8 -> bresenham algorithm
# line _AA ->Gaussian filtering

# Drawing a rectangle
cv2.rectangle(canvas, (200, 200), (250, 270), (200, 100, 95), -1)

# Drawing a circle
cv2.circle(canvas, (350, 350), 10, (255, 0, 1), 3)

# Drawing arrowed line
cv2.arrowedLine(canvas, (400, 400), (400, 450), (255, 255, 255), tipLength=0.5)
# showing the canvas
cv2.imshow('canvas', canvas)
cv2.waitKey()
