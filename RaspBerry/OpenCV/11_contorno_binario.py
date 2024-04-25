#import numpy as np
import cv2

#img = cv2.imread('binario.png')
#img_s = cv2.imread('binario_cuadrado.png')
img = cv2.imread('colores.png')
img_s = cv2.imread('cruz.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grises',imgray)
print(imgray)
imgray_s = cv2.cvtColor(img_s,cv2.COLOR_BGR2GRAY)
cv2.imshow('grises_2',imgray_s)
print(imgray_s)
'''
The cv2.threshold Function
Comencemos por echar un vistazo a la firma de la función cv2.threshold:
(T, threshImage) = cv2.threshold(src, thresh, maxval, type)
El primer parámetro es nuestra imagen de origen, o la imagen en la que queremos realizar el umbral. Esta imagen debe ser en escala de grises.
El segundo parámetro, thresh , es el valor umbral que se utiliza para clasificar las intensidades de píxeles en la imagen en escala de grises.
El tercer parámetro, maxval , es el valor de píxel utilizado si un píxel en la imagen pasa el umbral.
Finalmente, el cuarto parámetro es el método de umbral que se utilizará. El   valor de tipo puede ser cualquiera de:

cv2 . THRESH_BINARY
cv2 . THRESH_BINARY_INV
cv2 . THRESH_TRUNC
cv2 . THRESH_TOZERO
cv2 . THRESH_TOZERO_INV
'''

ret,thresh = cv2.threshold(imgray,184,255,0)    #Todo lo que esté en el rango (thresh-maxval), se convierte en blanco
ret,thresh_s = cv2.threshold(imgray_s,200,250,0) #El '0' equivale a THRESH_BINARY
cv2.imshow('thresh',thresh)
cv2.imshow('thresh_s',thresh_s)

'''
cv2.CHAIN_APPROX_SIMPLE, genera los puntos imprescindibles para generar el contorno.
En el caso del círculo son muchos
En el caso del cuadrado le basta con 4
'''
#imagen, contornos, jerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contornos, jerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#imagen_s, contornos_s, jerarquia_s = cv2.findContours(thresh_s,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contornos_s, jerarquia_s = cv2.findContours(thresh_s,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
#imagen_s1, contornos_s1, jerarquia_s1 = cv2.findContours(thresh_s,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #Esto genera todos los puntos
contornos_s1, jerarquia_s1 = cv2.findContours(thresh_s,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #
'''
print('contorno',contornos)
print('contorno_SIMPLE',contornos_s)
print('contorno_NONE',contornos_s1)
'''
#El contorno se pintará alrededor de los pixeles blancos. Por eso en la cruz también se pinta el cuadrado exterior
img = cv2.drawContours(img, contornos, 0, (0,255,0), 10)
img_s = cv2.drawContours(img_s, contornos_s, -1, (0,255,0), 3)
img_s1 = cv2.drawContours(img_s, contornos_s, -1, (0,255,0), 3)

constant= cv2.copyMakeBorder(img_s,40,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,255])

cv2.imshow('contorno',img)
cv2.imshow('contorno_s',img_s)
cv2.imshow('contorno_s1',img_s1)
cv2.imshow('borde',constant)

cv2.waitKey(0)
cv2.destroyAllWindows()
