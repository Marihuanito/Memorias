'''
Saca texto de una imagen
Lo primero es instalar la librería:
sudo apt-get install tesseract-ocr
si no funciona utiliza la siguiente orden
sudo pip3 install pytesseract

Podemos utilizar Pillow o openCV
'''
#from PIL import Image
# Importamos la libreria OpenCv
import cv2

# Importamos Pytesseract
import pytesseract 

# Abrimos la imagen
'''
im1 = cv2.imread("example_01.png")
im2 = cv2.imread("example_02.png")
im3 = cv2.imread("example_03.png")
'''
im = cv2.imread(('prueba_ocr.jpg'))

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
'''
texto1 = pytesseract.image_to_string(im1)
texto2 = pytesseract.image_to_string(im2)
texto3 = pytesseract.image_to_string(im3)
'''
texto = pytesseract.image_to_string(im)

# Mostramos el resultado
'''
print('texto1: ',texto1)
print()
print('texto12: ',texto2)
print()
print('texto3: ',texto3)
print()
'''
print('texto: ',texto)
