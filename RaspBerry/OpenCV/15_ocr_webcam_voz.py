#!usr/bin/python3
# -*- coding: utf-8 -*-
'''
En esta página se explica como instalar "festival"
https://www.raspberrypi.org/forums/viewtopic.php?t=123283
'''
import os, sys
import subprocess
from gtts import gTTS

import cv2
from pytesseract import *

capture = cv2.VideoCapture(0)  
IMAGE_FILE = 'luis_ocr.jpg'
 
val,frame=capture.read()
capture.release()
cv2.destroyAllWindows()

cv2.imwrite(IMAGE_FILE, frame)

# load image
im = cv2.imread(('luis_ocr.jpg'))

texto = pytesseract.image_to_string(im)
print('texto leido: ',texto)

tts = gTTS(texto)
tts.save('saludo.mp3')

os.system('mpg123 -q saludo.mp3')
'''
luis=subprocess.getoutput('echo '+'"'+ texto +'"'+' | festival --language spanish --tts')

if texto == 'Mr Puce':
    print('Reconocimiemnto correcto')
    luis=subprocess.getoutput('echo '+'"'+ texto +'"'+' | festival --language spanish --tts')
'''

