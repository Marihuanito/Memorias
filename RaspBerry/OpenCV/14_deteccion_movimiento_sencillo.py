import cv2
import numpy as np  #Sirve para trabajar con matrices, vectores, etc...
                    #y asignamos un alias 'np'
    
webcam_id = 0       #Seleccionamos el id de la cámara
cap = cv2.VideoCapture(webcam_id) #creamos el objeto 'cap'
cap.set(3,520) #pixeles en horizontal de la ventana
cap.set(4,240) #pixeles en vertical

ret,prev=cap.read()

while(cap.isOpened()):
    # Capture frame-by-frame
    ret,next = cap.read() #si se estan recibiendo imagenes 'ret'=True.
    if ret == True:
        #restamos las imágenes como tipo float, tomamos el valor absoluto de la resta
        #y lo ponemos tipo entero 8 bits para poder visualizarlo
        #Esto se hace así para que la resta sea correcta... queda explicado aquí:
        #https://www.youtube.com/watch?v=5ryjqXUeipg
        flow=np.array(abs(np.array(next,np.float32)-np.array(prev,np.float32)),np.uint8)

        #mostramos la imagen
        cv2.imshow('flow',flow)

        prev=next

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
