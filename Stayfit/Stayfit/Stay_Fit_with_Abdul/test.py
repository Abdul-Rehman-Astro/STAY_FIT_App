

import cv2

camera_index = 0  # Replace with the correct camera index from the output of the above script
cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Test Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to grab frame")
cap.release()
cv2.destroyAllWindows()