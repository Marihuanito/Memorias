import cv2

# Load image, ESTE NO LE HIZO MUCHO CASO EN CLASE, NO SE DIO.
image_path = 'nadal.jpg'
image = cv2.imread(image_path)
'''
El filtro de la media es el más simple,
intuitivo y fácil de implementar para suavizar imágenes.
Esta operación se realiza mediante la convolución de la imagen
con un filtro normalizado. Simplemente, calcula la media de los píxeles
que están bajo el área del kernel y reemplaza el valor del elemento central
'''
# Blur
k = 3 #tamaño del kernel
blur = cv2.blur(image, (k, k))

# Show
cv2.imshow('Original', image)
cv2.imshow('Filtered', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
