import cv2

cap = cv2.VideoCapture(0)

color = (255,0,0)
thickness = 3
radius = 15
point = (10,10)

def cursor_locator(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_MOUSEMOVE:
        print("Coordinates",x,y)
        point = (x,y)
    
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", cursor_locator)

while(True):
    ret, frame = cap.read()
    
    cv2.circle(frame, point, radius, color, thickness)
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
