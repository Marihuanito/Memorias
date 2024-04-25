import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_eye.xml')

#img = cv2.imread('face_eye.png')
img = cv2.imread('caras.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) 
'''
1.- image: Matriz del tipo CV_8U que contiene una imagen donde se detectan objetos.
2.- scaleFactor: Parámetro que especifica cuánto se reduce el tamaño de la imagen en cada escala de imagen.
    Este factor de escala se usa para crear una pirámide de escala como se muestra en la imagen.
    Supongamos que el factor de escala es 1.03, significa que estamos usando un pequeño
    paso para cambiar el tamaño, es decir, reducir el tamaño en un 3%, aumentamos las posibilidades
    de que coincida el tamaño con el modelo de detección, mientras que es caro.
3.- minNeighbors: Parámetro que especifica cuántos vecinos debe tener cada rectángulo candidato para conservarlo.
    Este parámetro afectará la calidad de las caras detectadas: un valor más alto da como resultado menos detecciones 
    pero con mayor calidad. Estamos usando 5 en el código.
4.- flags: Parámetro con el mismo significado para una cascada antigua que en la función cvHaarDetectObjects.
    No se usa para una nueva cascada.
5.- minSize: tamaño mínimo posible del objeto. Los objetos más pequeños que eso se ignoran.
6.- maxSize: tamaño de objeto máximo posible. Los objetos más grandes que eso son ignorados

Si se encuentra la cara o los ojos, la función devuelve (x,y,w,h)
'''
faces = face_cascade.detectMultiScale(gray, 1.2, 2) #cambiando el factor de escala se puede encontrar, o no, los ojos
print('caras: ',faces)
'''
caras:  [[260  53 142 142]
 [480  54 141 141]
 [ 39  55 149 149]
 [ 37 268 147 147]
 [478 271 145 145]
 [254 279 149 149]]
 Son los datos de las 6 caras --> [x,y,w,h]
'''
for (x,y,w,h) in faces:
  print('x:',x)
  print('y:',y)
  print('w:',w)
  print('h:',h)
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,100,100),2)
  roi_gray = gray[y:y+h, x:x+w]     #Este roi coincide en tamaño y localización con la 'img' de la línea anterior
  #print('roi_gray:',roi_gray)
  roi_color = img[y:y+h, x:x+w]     #Este roi coincide en tamaño y localización con el 'roi_gray'
									#Y se utilizará para dibujar el rectángulo de los ojos en la imagen original
  #print('roi_color:',roi_color)
  #roi_gray = gray[x:x+w, y:y+h] #depende de como creemos el ROI (xy) o (yx), también afecta a la búsqueda de ojos
  #roi_color = img[x:x+w, y:y+h]
  eyes = eye_cascade.detectMultiScale(roi_gray) #Detectamos los ojos dentro del roi que contiene la cara
  print('ojos: ',eyes)
  '''
  Por ejemplo, los ojos de la cara [260  53 142 142] son:
      [[24 39 34 34]
      [79 38 36 36]]
  Estas dos listas, ojo izd. y ojod dch., tienen el siguiente formato --> [x,y,w,h]
  Siendo las coordenas x,y relativas respecto a las de la cara, es decir, si la cara tiene x=260, la coordenada
  absoluta del ojo izd. es 260+24 y la del derecho 260+79    
  '''  
  for (ex,ey,ew,eh) in eyes:        #'ejes' contiene dos listas, una por ojo, por lo que el for devuelve dos listas
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(40,55,200),2)

cv2.imshow('img',img)
cv2.imwrite('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
