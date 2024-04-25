import cv2

cap = cv2.VideoCapture(1)
#set the width and height, and UNSUCCESSFULLY set the exposure time
#1920x1080 / 1280x720 / 640x480
cap.set(3,640)
cap.set(4,480)
cap.set(15, 0.1)

fps_prop = cv2.CAP_PROP_FPS



while True:
    ret, img = cap.read()

    fps = "{0:.2f}".format(cap.get(fps_prop))
    text = "FPS: " + fps
    
    text_color = (255,0,0)
    cv2.putText(img,text, (10,30), cv2.FONT_HERSHEY_PLAIN, 2.0, text_color, thickness=2)
    cv2.imshow('luis',img)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows()
cv2.VideoCapture(1).release()
