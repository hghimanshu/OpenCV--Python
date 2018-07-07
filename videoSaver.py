import cv2

cap = cv2.VideoCapture(0)
name = 'output.avi'
fps = 25.0
frameSize = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(name,fourcc, fps, frameSize)

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()