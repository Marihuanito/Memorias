#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR: CIFPN1                                             Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:  MOSTRAR FPS DE UN VIDEO                        VERSIÓN: 1.0      
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
Muestra en pantalla los frames por segundo del video ejecutado 
////////////////////////////////////////////////////////////////////////////////////
"""

#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2

video_file = 'conejo.mp4'
cap = cv2.VideoCapture(video_file)

#////////////////////////////////////////////////////////////////////////////////////
# VARIABLES GLOBALES
#////////////////////////////////////////////////////////////////////////////////////
# Properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255,255,255)
thickness = 1

#////////////////////////////////////////////////////////////////////////////////////
# FUNCIONES
#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
# CONFIGURACIÓN PUERTOS GPIO Y RECURSOS A UTILIZAR
#////////////////////////////////////////////////////////////////////////////////////
if cv2.__version__.startswith('2.4'):
    height_prop = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT 
else:
    height_prop = cv2.CAP_PROP_FRAME_HEIGHT

if cv2.__version__.startswith('2.4'):
    fps_prop = cv2.cv.CV_CAP_PROP_FPS
else:
    fps_prop = cv2.CAP_PROP_FPS

#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:                 
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Text position
            height = int(cap.get(height_prop))
            position = (50, height - 50)
            
            # Frames per second
            fps = "{0:.2f}".format(cap.get(fps_prop))
            text = "FPS: " + fps
            
            # Put text
            cv2.putText(frame, text, position, font, font_scale, color, thickness)

            # Display
            cv2.imshow("Video", frame)
            
            # Exit?
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")
    cap.release()
    cv2.destroyAllWindows()
except:
    print("error inesperado")
    cap.release()
    cv2.destroyAllWindows()
finally:
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()
