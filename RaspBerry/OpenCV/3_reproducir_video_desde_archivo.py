#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:  CIFPN1                                            Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:  REPRODUCIR VIDEO DESDE ARCHIVO                        VERSIÓN:1.0      
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
Reproducción de un fichero mp4 hasta su final
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
    '''
    A veces, el objeto VideoCapture puede no haber logrado la inicialización
    de la captura correctamente.
    Por ello, es mejor comprobar si se ha inicializado, o no,
    a través del método cap.isOpened().
    Si el resultado es True es que sí se ha podido abrir la captura.
    '''
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        '''
        El método cap.read() devuelve un valor booleano (True/False).
        Si el frame se leyó correctamente, devolverá True.
        De esta forma, se puede comprobar cuándo se ha llegado
        al final de la lectura del vídeo comprobando este parámetro.
        '''
        if ret == True:
            # Operations on the frame
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Muestra el vídeo en blanco y negro
            gray = cv2.cvtColor(frame,0) #Muestra el vídeo en color

            # Display the resulting frame
            cv2.imshow('frame', gray)
        
            # Exit? Espera que presionemos la tecla 'q' para terminar el while
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break     

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    cap.release()
    cv2.destroyAllWindows()
