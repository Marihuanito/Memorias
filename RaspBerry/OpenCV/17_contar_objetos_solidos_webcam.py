import cv2
import numpy as np
'''
Para este ejercicio utilizaremos el plafón de luz y unas monedas encima
'''
webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

# Cany edge detector thresholds
threshold_one = 50
threshold_two = 150
aperture_size = 3

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Operations on the frame
        edges = cv2.Canny(frame, threshold_one, threshold_two, aperture_size)
        
        # Display
        cv2.imshow("Original", frame)
        cv2.imshow("Canny edge detection", edges)
        
        #############################################################################################
        # Convertimos a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        # Aplicar suavizado Gaussiano
        gauss = cv2.GaussianBlur(gris, (5,5), 0)
         
        cv2.imshow("suavizado", gauss)

        # Detectamos los bordes con Canny
        canny = cv2.Canny(gauss, 50, 150)
         
        cv2.imshow("canny", canny)

        # Buscamos los contornos
        (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Mostramos el número de monedas por consola
        print("He encontrado {} objetos".format(len(contornos)))
        #############################################################################################

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
