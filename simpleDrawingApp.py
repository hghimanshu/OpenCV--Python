import cv2
import numpy as np

canvas = np.ones([640,640,3], 'uint8')*255 # making a white canvas for drawing
color = (0,0,0)
radius = 5
pressed = False

def painter(event, x, y, flags, params):
    global canavs, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x,y), radius, color, -2)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(canvas, (x,y), radius, color, -2)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False
    
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", painter)

while True:
    cv2.imshow("canvas", canvas)
    
    k = cv2.waitKey(1)
    
    if k & 0xff == ord('q'):
        break
    
    if k & 0xff == ord('y'):
        color = (0, 255, 255) # yellow color
    
    if k & 0xff == ord('b'):
        color = (255,0,0) # blue color
    
    if k & 0xff == ord('r'):
        color = (0,0,255) # red color
    
    if k & 0xff == ord('g'):
        color = (0,255,0) # green color
    
    if k & 0xff == ord('c'):
        canvas = np.ones([640,640,3], 'uint8')*255


cv2.destroyAllWindows()