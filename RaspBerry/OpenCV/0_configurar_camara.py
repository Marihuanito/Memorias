import cv2 
'''
Como referencia, el primer argumento en el cap.set()
comando se refiere a la enumeración de las propiedades de la cámara,
se enumeran a continuación:

0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds. 
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next. 
3. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file 
4. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream. 
5. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream. 
6. CV_CAP_PROP_FPS Frame rate. 
7. CV_CAP_PROP_FOURCC 4-character code of codec. 
8. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file. 
9. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() . 
10. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode. 
11. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras). 
12. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras). 
13. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras). 
14. CV_CAP_PROP_HUE Hue of the image (only for cameras). 
15. CV_CAP_PROP_GAIN Gain of the image (only for cameras). 
16. CV_CAP_PROP_EXPOSURE Exposure (only for cameras). 
17. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB. 
18. CV_CAP_PROP_WHITE_BALANCE Currently unsupported 
19. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras
(note: only supported by DC1394 v 2.x backend currently) 
'''

#capture from camera at location 0 
cap = cv2.VideoCapture(0) 
#set the width and height, and UNSUCCESSFULLY set the exposure time 
cap.set(3,1000) 
cap.set(4,1024)
#cap.set(5,1000)
cap.set(15, 0.1) 

while True: 
    ret, img = cap.read() 
    cv2.imshow("input", img) 

    key = cv2.waitKey(3) 
    if key == 27: 
     break 


cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
