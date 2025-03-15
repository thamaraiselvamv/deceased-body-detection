import cv2

cap = cv2.VideoCapture('http://http://192.168.107.234:8080/video')  # Replace with your IP camera's URL

while True:
    ret, frame = cap.read()
    # Process the frame here
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()