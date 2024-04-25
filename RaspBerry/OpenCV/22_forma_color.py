#Práctica 4 Luis
import cv2
import numpy as np

try:  
  while(1):
    #-------------------------------------------------------------------------------------------------------------
    #Capturamos frame 
    #-------------------------------------------------------------------------------------------------------------
    capture = cv2.VideoCapture(0)  
    IMAGE_FILE = 'luis_ocr.png'
     
    val,frame=capture.read()
    capture.release()
    cv2.destroyAllWindows()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #-------------------------------------------------------------------------------------------------------------
    #Seleccionamos color a detectar
    #-------------------------------------------------------------------------------------------------------------
    '''
    #ROJO
    lower_color = np.array([0, 50, 50])
    upper_color =  np.array([15, 255, 255])
    '''
    
    #VERDE
    lower_color = np.array([60, 100, 20])
    upper_color =  np.array([100, 255, 255])
    
    '''
    #AZUL
    lower_color = np.array([85, 50, 50])
    upper_color =  np.array([145, 255, 255])
    '''
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Color', res)
    #-------------------------------------------------------------------------------------------------------------
    #Escribimos la imagen con el color detectado en el fichero para poder ser tratado posteriormente
    #-------------------------------------------------------------------------------------------------------------
    cv2.imwrite(IMAGE_FILE, res)
    #-------------------------------------------------------------------------------------------------------------
    #Leemos la imagen, seleccionamos un marco a tratar (supuestamente, donde se encuentra el objeto)
    #Lo pasamos a escala de grises, 
    #-------------------------------------------------------------------------------------------------------------
    image = cv2.imread(('luis_ocr.png'))
    image=image[170:350, 250:500]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #-------------------------------------------------------------------------------------------------------------
    #Eliminamos ruido de la imagen con un kernel de 3
    #-------------------------------------------------------------------------------------------------------------
    blur=cv2.medianBlur(gray,3)
    cv2.imshow('blur',blur)
    #-------------------------------------------------------------------------------------------------------------
    #filtramos con canny
    #-------------------------------------------------------------------------------------------------------------
    canny = cv2.Canny(blur, 10, 150)
    canny = cv2.dilate(canny, None, iterations=1)
    canny = cv2.erode(canny, None, iterations=1)
    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
    print(len(cnts))
    #-------------------------------------------------------------------------------------------------------------
    #Buscamos la forma de la figura
    #-------------------------------------------------------------------------------------------------------------
    for c in cnts:
      #-------------------------------------------------------------------------------------------------------------
      #El epsilon hay que cambiarlo dependiendo de la figura a tratar...
      #Triángulo --> 0.1
      #Cualquier otro polígono --> 0.01
      #-------------------------------------------------------------------------------------------------------------
      epsilon = 0.01*cv2.arcLength(c,True)
      approx = cv2.approxPolyDP(c,epsilon,True)
      x,y,w,h = cv2.boundingRect(approx)

      if len(approx)==3:
        cv2.putText(image,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)

      if len(approx)==4:
        aspect_ratio = float(w)/h
        print('aspect_ratio= ', aspect_ratio)
        if aspect_ratio == 1:
          cv2.putText(image,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        else:
          cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)

      if len(approx)==5:
        cv2.putText(image,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)

      if len(approx)==6:
        cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)

      if len(approx)>10:
        cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)

      cv2.drawContours(image, [approx], 0, (0,255,0),2)
      cv2.imshow('image',image)
      cv2.waitKey(0)
      
except KeyboardInterrupt:   #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    print('Salida por "finally"')

