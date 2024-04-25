import cv2
import numpy as np

'''
Para HSV, el rango de tonos es [0,179],
el rango de saturación es [0,255]
y el rango de valor es [0,255].
Los distintos programas usan distintas escalas.
Así que, si estás comparando los valores de OpenCV con ellos,
necesitas normalizar estos rangos.
'''
# Webcam
webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

while True:
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''
    La búsqueda del color en HSV, tendrá que ser empírica
    '''
    # Define range in HSV
    #AZUL
    #lower_color = np.array([85, 50, 50])
    #upper_color =  np.array([145, 255, 255])
    #AMARILLO
    #lower_color = np.array([25, 50, 50])
    #upper_color =  np.array([60, 255, 255])
    #ROJO
    lower_color = np.array([0, 50, 50])
    upper_color =  np.array([15, 255, 255])

    # Mask: threshold the HSV image to get only defined colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    px = res[100, 100]
    print ('intensidad', px)
    # Show
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Color', res)

    # Exit?
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
