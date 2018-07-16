import cv2

img = cv2.imread('images/candy.jpg')
cv2.imshow("Original", img)
cv2.waitKey(0)
# converting into gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
# converting into HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
# converting into RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()