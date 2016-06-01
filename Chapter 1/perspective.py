import cv2
import numpy as np
img = cv2.imread('images/input.jpg')
rows, cols = img.shape[:2]

# Set control points
src_points = np.float32([[0, 0], [0, rows-1], [cols/2, 0],	[cols/2, rows-1]])
dst_points = np.float32([[20, 100], [0, rows-101],	[cols/2, 0], [cols/2, rows-1]])

# Get projective matrix from control points
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Transform image using matrix and show it
img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
cv2.imshow('Input', img)
cv2.imshow('Output 1', img_output)
cv2.waitKey()
