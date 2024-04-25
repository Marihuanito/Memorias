#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import time
import datetime
import os

import speech_recognition as sr

with sr.Microphone() as source:
    os.system('mpg123 -q Hola.mp3')
    print ("Di tu nombre y apellidos...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    text1 = text.replace(' ','_')
    print("tú dijiste: {}".format(text))
    print("tú dijiste: {}".format(text1)
    a = open('cuarentena.txt','a')
    outfile.write(text1+'.jpg\n')
    fecha = str(time.time())
    print('fecha: ',fecha)
    print(time.asctime(time.localtime(time.time())))
    outfile.write(fecha+'n')
    outfile.close()
except:
    print("Lo siento!... no te pude entender")
