import cv2
import numpy as np

img = cv2.imread('images/house.jpg')
cv2.imshow("Original", img)
cv2.waitKey()
############################################
## code for translation
height, width = img.shape[:2]

tx, ty = 45,45

# visulaizing our translation matrix
#T = |1  0   tx|
#    |0  1   ty|

T = np.float32([[1, 0, tx], [0, 1, ty]])

transl = cv2.warpAffine(img, T, (height, width))
cv2.imshow("Translation", transl)
cv2.waitKey()

#############################################
## code for scaling

scaling = cv2.resize(img,None,fx=1.5, fy=1.5)
cv2.imshow("Scaling", scaling)
cv2.waitKey()

############################################
## code for rotation

M = cv2.getRotationMatrix2D((height/3,width/4),45,1)
rot = cv2.warpAffine(img,M,(height,width))
cv2.imshow("Rotation", rot)

cv2.waitKey()
cv2.destroyAllWindows()