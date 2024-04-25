import cv2
import numpy as np
from matplotlib import pyplot as plt

title = 'Money' 
img_rgb = cv2.imread('mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('moneda.jpg',0)
w, h = template.shape[::-1] #El -1 hace que se devuelva los valores invertidos
#w, h = template.shape[:-1] #Así, sólo devuelve un valor
#w, h = template.shape
print('w: ',w)
print('h: ',h)

count=0

#Generamos una matriz 'res' con los puntos de coincidencia
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
print('res: ',res)
'''
el umbral 0.8 significa que la coincidencia debe ser al menos el 80% de
la imagen de la plantilla y la Región de interés de origen. así, si es
mayor que 805 es una moneda. Si reduce el umbral, los resultados falsos
positivos aumentarían incluso si no es una moneda.
'''
umbral = 0.8
'''
np.where() --> devuelve los índices de elementos en una matriz de entrada
donde se cumple la condición dada.
'''
loc = np.where( res >= umbral)
print('loc: ',loc)
'''
para pt en Zip (* loc [:: - 1]): este comando es para los puntos que tienen
valores mayores que el umbral. zip es el contenedor de todos esos puntos e
iterará a todos esos puntos y dibujará un rectángulo alrededor de esta
entidad cerrada, es decir, monedas aquí.
'''
for pt in zip(*loc[::-1]):
    count += 1
    print(count,end="-")
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
 
cv2.imwrite('out_monedas.png',img_rgb)
cv2.imshow(title, img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows() 
