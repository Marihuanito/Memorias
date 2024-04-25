#Hace alguna cosa con máscaras y el filtro canny
import cv2
#import numpy as np

webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

# Cany edge detector thresholds
threshold_one = 50
threshold_two = 150
aperture_size = 3
try:
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Operations on the frame
            edges = cv2.Canny(frame, threshold_one, threshold_two, aperture_size)
            
            # Display
            cv2.imshow("Original", frame)
            cv2.imshow("Canny edge detection", edges)

            px = edges[100, 100]
            #Leo el valor del Rojo
            px2=frame[100, 100,2]
            print("original rojo",px2)
            print('pixel leido',px)

            if px2 > 100:
                print ("Rojo detectado")
            if px > 200:
                print (px)
                print ('alarma')
            
            # Exit?
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    #Libera todo si la tarea ha terminado
    cap.release()
    cv2.destroyAllWindows()
