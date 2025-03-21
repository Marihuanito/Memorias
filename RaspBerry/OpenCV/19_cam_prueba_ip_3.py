import cv2, platform
#import numpy as np

#cam = "http://usuario:usuario@172.100.7.232:88/cam2"
cam = "http://luis:dani30@192.168.1.121:8080/videofeed"
#cam = 0 # Use  local webcam.

cap = cv2.VideoCapture(cam)
if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

while(True):
    # Capture frame-by-frame
    ret, current_frame = cap.read()
    if type(current_frame) == type(None):
        print("!!! Couldn't read frame!")
        break

    # Display the resulting frame
    cv2.imshow('frame',current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()
