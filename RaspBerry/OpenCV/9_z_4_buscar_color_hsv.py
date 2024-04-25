'''
Extrapolar entre BGR y HSV
Es muy simple y puedes usar la misma función, cv2.cvtColor().
En lugar de pasar una imagen, sólo pasas los valores RGB que deseas.
Por ejemplo, para encontrar el valor HSV para el verde:
'''
import cv2
import numpy as np
rosa1 = np.array([[[237,103,216 ]]],np.uint8) 
rosa = np.uint8([[[237,103,216 ]]]) 
green = np.uint8([[[0,255,0 ]]]) 
blue = np.uint8([[[255,0,0 ]]])
red = np.uint8([[[0,0,255 ]]])

hsv_rosa1 = cv2.cvtColor(rosa1,cv2.COLOR_BGR2HSV) 
print ('HSV rosa1: ',hsv_rosa1) #[[[ ]]]

hsv_rosa = cv2.cvtColor(rosa,cv2.COLOR_BGR2HSV) 
print ('HSV rosa: ',hsv_rosa) #[[[ ]]]

hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV) 
print ('HSV verde: ',hsv_green) #[[[ 60 255 255]]]

hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV) 
print ('HSV azul: ',hsv_blue ) #[[[120 255 255]]]

hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV) 
print ('HSV rojo: ',hsv_red) #[[[  0 255 255]]]
