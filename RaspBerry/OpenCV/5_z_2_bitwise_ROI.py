import cv2
# cargamos 2 imagenes, la segunda hace de máscara
img1 = cv2.imread('nadal.jpg')
cv2.imshow('origen',img1)
cv2.waitKey(0)
'''======================================================================================'''
''' cambia de imagen para probar'''
img2 = cv2.imread('circulos.jpg')
#img2 = cv2.imread('rectangulo.jpg')
cv2.imshow('fuente_mask ',img2)
cv2.waitKey(0)
'''======================================================================================'''

#############################################################################################
# Yo quiero poner el logo en el corner izquierdo y por eso creo un ROI con el tamaño de img2
#############################################################################################
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
cv2.imshow('roi',roi )
cv2.waitKey(0)
#cv2.destroyAllWindows()
#############################################################################################

#############################################################################################
# Ahora creo una máscara de logotipo y hago su máscara inversa también
#############################################################################################
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# El threshold necesita un rango... en este caso elegimos entre 250 y 255, que es el blanco
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
cv2.imshow('1',mask)
cv2.waitKey(0)
#############################################################################################

#############################################################################################
# Invertimos la máscara
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('2',mask_inv)
cv2.waitKey(0)
#############################################################################################

#############################################################################################
# Ahora pongo oscura el área de logotipo en ROI
#############################################################################################
'''======================================================================================'''
''' cambia de instrucción para probar'''
#img1_bg = cv2.bitwise_and(roi,roi,mask = mask)    # oculta el área de los círculos 
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv) # muestra el área de los círculos
cv2.imshow('3',img1_bg )
cv2.waitKey(0)
#cv2.destroyAllWindows()
'''======================================================================================'''
#############################################################################################

#############################################################################################
# Tomo solamente la región del logotipo de la imagen del logotipo
#############################################################################################
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('4',img2_fg )
cv2.waitKey(0)
#cv2.destroyAllWindows()
#############################################################################################

#############################################################################################
# Pongo el logotipo en ROI y modifico la imagen principal
#############################################################################################
''' cambia de instrucción para probar'''
#dst = cv2.add(img1_bg,img2_fg)
#img1[0:rows, 0:cols ] = dst
#img1[50:50+rows, 50:50+cols] = img1_bg #Lo muevo donde quiero
img1[0:rows, 0:cols] = img1_bg #Añadimos la imagen generada con la máscara a la original
cv2.imshow('5',img1)
cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow('6',roi )
cv2.waitKey(0)
#############################################################################################
cv2.destroyAllWindows()
