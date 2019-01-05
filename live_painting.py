import cv2
import numpy as np

def color_changer(color, x,y):
    if x in range(520, 640):
        if y in range(10, 100):
            color = (0, 0, 255)
        elif y in range(110, 200):
            color = (255, 0, 0)
        elif y in range(210, 300):
            color = (0, 255, 0)
        elif y in range(310, 400):
            color = (0, 255, 255)
        elif y in range(410, 500):
            color = (255,0,255)

    return color

def trace_color(prev_color, x,y):
    if x in range(520, 640):
        new_color = prev_color
        if y in range(10, 100):
            new_color = (0, 0, 255)
        elif y in range(110, 200):
            new_color = (255, 0, 0)
        elif y in range(210, 300):
            new_color = (0, 255, 0)
        elif y in range(310, 400):
            new_color = (0, 255, 255)
        elif y in range(410, 500):
            new_color = (255,0,255)
    else:
        new_color = prev_color
    return new_color

        

low_red = np.array([31, 49, 191])
up_red = np.array([58, 255, 255])
cap = cv2.VideoCapture(0)
points = []
radius = 0
ret, frame = cap.read()
ht, wd = frame.shape[:2]
frame_count = 0
color = (0,0,0)
canvas = np.ones([480,640,3], dtype='uint8')*255

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ht, wd = frame.shape[:2]
    
    cv2.rectangle(frame, (520, 10), (640, 100), (0,0,255), 3)
    cv2.rectangle(frame, (520, 110), (640, 200), (255,0,0), 3)
    cv2.rectangle(frame, (520, 210), (640, 300), (0,255,0), 3)
    cv2.rectangle(frame, (520, 310), (640, 400), (0,255,255), 3)
    cv2.rectangle(frame, (520, 410), (640, 500), (255,0,255), 3)
#    
    
    mask = cv2.inRange(hsv, low_red, up_red)
    _, contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    center = int(ht/2), int(wd/2)
    
    if len(contours) > 0:
        c = max(contours, key =cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        radius = int(radius)
        M = cv2.moments(c)
        try:
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/ M["m00"]))
            x, y = center
        except:
            center = int(ht/2), int(wd/2)
        if radius > 25:
            cv2.circle(frame, (int(x), int(y)), radius, (88, 50, 255), 5)
            color = color_changer(color, x,y)
            cv2.circle(frame, center, 5, color, -3)
    points.append(center)
    if radius > 25:
        for i in range(1, len(points)):
            try:
                x, y = points[i]
                prev_color = color
                new_color = trace_color(prev_color, x,y)
                print(x, y)
                cv2.line(canvas, points[i-1], points[i], new_color, 6)
            except:
                pass
            
        frame_count = 0
    else:
        frame_count += 1
        
        if frame_count == 10:
            points = []
            canvas = np.ones([480,640,3], dtype='uint8')*255 
            frame_count = 0
    canvas = cv2.flip(canvas, 1)
    frame = cv2.flip(frame, 1)
    cv2.imshow("Canvas", canvas)
    cv2.imshow("Last", frame)
    
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()