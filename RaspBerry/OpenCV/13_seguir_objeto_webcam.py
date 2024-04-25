import cv2
import numpy as np  #Sirve para trabajar con matrices, vectores, etc...
                    #y asignamos un alias 'np'
    
webcam_id = 0       #Seleccionamos el id de la cámara
cap = cv2.VideoCapture(webcam_id) #creamos el objeto 'cap'
kernel=np.ones((5,5),np.uint8)  #esta matriz sirve para convolucionar una imagen,
                                #es decir, para filtrar.
                                #la creamos de 5x5 y un rango de valores de 8 bits
'''
TRANSFORMACIONES MORFOLÓGICAS
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

Las transformaciones morfológicas son algunas operaciones simples basadas en la forma de la imagen. 
Normalmente se realiza en imágenes binarias. Necesita dos entradas, una es nuestra imagen original, 
la segunda se llama elemento estructurante o núcleo (kernel) que decide la naturaleza de la operación.

Erosión: --> erosion = cv2.erode(img,kernel,iterations = 1)
Elimina pequeños ruidos blancos alrededor de la imagen y la adelgaza.

Dilatación: --> dilation = cv2.dilate(img,kernel,iterations = 1)
Normalmente va seguida de la erosión que reduce el objeto, y ahora que ya no tiene ruido lo dilatamos.

Opening: --> opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
Su acción es de erosión seguido de dilatación. Elimina ruido exterior

Closing: --> closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
Su acción es la dilatación seguido de erosión.Elimina el ruido interior. 
Es útil para cerrar pequeños agujeros dentro de los objetos en primer plano, 
o pequeños puntos negros en el objeto.
'''
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read() #si se estan recibiendo imagenes 'ret'=True.
                            #'frame' son las imagenes leidas en ms
    if ret == True:
        #Configuramos el rango de valores BGR para detectar un objeto, en este caso verde
        #rangomax=np.array([50,255,50])
        #rangomin=np.array([0,51,0])
        #Configuramos el rango de valores BGR para detectar un objeto, en este caso rojo
        rangomax=np.array([15,255,255])
        rangomin=np.array([0,50,50])
        #Creamos la máscara. Esto quiere decir que, cuando el pixel se encuentre dentro del
        #rango será un punto blanco y cuando esté fuera será un punto negro
        mascara=cv2.inRange(frame,rangomin,rangomax)
        #eliminamos el ruido
        opening=cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)
        #obtenemos los valores inicial y final del rectángulo...inicial (x,y) y final (w,h)
        #seguidamente dibujamos el rectángulo:punto de inicio (x,y) punto final (x+w,y+h)
        #color verde y grosor 3
        x,y,w,h=cv2.boundingRect(opening)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        #dibujamos un punto Rojo en el centro del rectángulo de grosor 5
        #y '-1' para que sea un círculo en lugar de una circunferencia
        cv2.circle(frame,(int(x+w/2),int(y+h/2)),10,(0,0,255),-1)
        #mostramos la imagen
        cv2.imshow('camara',frame)

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
