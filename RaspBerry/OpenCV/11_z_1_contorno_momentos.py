import cv2

img = cv2.imread('binario_cuadrado.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

#imagen, contornos, jerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contornos, jerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print('#############################################################################')
print('contorno_SIMPLE',contornos)
print('#############################################################################')

cnt = contornos[0]  #si pongo un nº>0 da error de index
M = cv2.moments(cnt)
print('Todos los momentos: ',M)        #M contiene todos los momentos
print('#############################################################################')

#El área de contorno viene dada por la función cv2.contourArea() o por el momento M [‘m00’]
area = cv2.contourArea(cnt)
print('area: ',area)        #creo que la unidad son pixeles
print('#############################################################################')

perimetro = cv2.arcLength(cnt,True)
print('Perímetro: ', perimetro) #creo que la unidad son pixeles
print('#############################################################################')

img_1 = cv2.drawContours(img, contornos, -1, (0,255,0), 5)
cv2.imshow('contorno',img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
