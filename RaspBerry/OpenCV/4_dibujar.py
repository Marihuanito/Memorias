#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:   CIFPN1                                           Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:   DIBUJAR                       VERSIÓN: 1.0      
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
Programa para aprender a dibujar con instrucciones de opencv
////////////////////////////////////////////////////////////////////////////////////
"""

#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2
import numpy as np

img = np.zeros((600, 800, 3), np.uint8) #Creamos el objeto 'img'

#////////////////////////////////////////////////////////////////////////////////////
# VARIABLES GLOBALES
#////////////////////////////////////////////////////////////////////////////////////
title = 'Drawing'

#////////////////////////////////////////////////////////////////////////////////////
# FUNCIONES
#////////////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////////////
# CONFIGURACIÓN PUERTOS GPIO Y RECURSOS A UTILIZAR
#////////////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:            
    #línea blanca en el centro de la imagen
    #(0,255) --> punto de inicio (x,y)
    #(511,255) --> punto final (x,y)
    #(255,255,255) --> Color (B, G, R)
    #(10) --> grosor
    cv2.line(img,(0,255),(511,255),(255,255,255),10)

    #rectángulo azul en la parte inferior de la imagen
    cv2.rectangle(img,(210,360),(300,500),(255,0,0),3)

    #círculo rojo en el centro de la imagen
    #(255,255) --> centro del círculo (x,y)
    # 100 --> radio
    #(0,0,255) --> Color (B, G, R)
    #(-1) --> grosor, en este caso lleno   
    cv2.circle(img,(255,255), 100, (0,0,255), 10)

    #media elipse en el centro superior de la imagen
    cv2.ellipse(img,(255,105),(100,50),0,0,180,255,-1)
    cv2.ellipse(img, (400, 360), (100, 50), 0, 45, 360, (255, 0, 255), -1, cv2.LINE_AA)
    
    #polígono, triángulo amarillo
    pts = np.array([[180,120],[330,120],[255,140]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(0,255,255),3)

    #texto
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, 'OpenCV Python', (5, 560), font, 3, (255,255,255), 1, cv2.LINE_AA)

    #polígono, estrella de david amarilla
    pts = np.array([[403, 75], [587, 312], [216, 150], [588, 155], [215, 313]], np.int32)
    cv2.polylines(img, [pts], True, (0, 255, 255), 5, cv2.LINE_AA)
    
    cv2.imshow(title, img)
    cv2.waitKey(0)

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    cv2.destroyAllWindows()
