#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:                                              Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: CAMBIAR NOMBRE Y FORMATO A UNA IMAGEN                    VERSIÓN: 1.0     
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
            Abrimos una imagen JPG y la cambiamos a formato PNG
////////////////////////////////////////////////////////////////////////////////////
"""

#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2

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
    while True:      #iniciamos un loop infinito
        #Load
        '''
        Leer una imagen
        Utiliza la función cv2.imread() para leer una imagen.
        La imagen debe estar en el directorio de trabajo o se ha de señalar
        una ruta absoluta a la imagen.

        El segundo argumento es un indicador (o bandera) que especifica la forma
        en que se debe leer la imagen.
        ◾cv2.IMREAD_COLOR: carga una imagen de color.
            Cualquier transparencia de la imagen será ignorada.
            Es el indicador (o bandera) predeterminado.
        ◾cv2.IMREAD_GRAYSCALE: carga la imagen en modo de escala de grises
        ◾cv2.IMREAD_UNCHANGED: carga la imagen como sin alteraciones incluyendo el canal alfa

        Nota.-En lugar de estos tres indicadores (o banderas), simplemente puedes pasar números enteros,
        específicamente 1, 0 o -1, respectivamente. 
        '''
        image_path='caras.jpg'
        image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

        #Save copy as png
        image_copy_path='caras_copy.png'
        cv2.imwrite(image_copy_path, image)

        #Load copy
        image_copy=cv2.imread(image_copy_path)

        #Show
        cv2.imshow('Original',image)
        cv2.imshow('Copy',image_copy)
        '''
        cv2.waitKey () es una función de enlace con el teclado.
        Su argumento es tiempo en milisegundos. La función espera durante milisegundos
        especificados que suceda cualquier evento de teclado. Si presionas cualquier
        tecla en ese momento, el programa continúa. Si se pasa el valor 0, la espera
        del evento es indefinida hasta que se presione una tecla. 
        También se puede configurar para detectar pulsaciones de teclas específicas.
        '''
        cv2.waitKey(3000)
        break       #Salimos del While y pasamos por "finally"
     

except KeyboardInterrupt:   #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    '''
    cv2.destroyAllWindows() Esta función destruye todas las ventanas que hemos creado.
    Si deseas destruir una ventana específica, utiliza la función de cv2.destroyWindow ()
    donde se pasa el nombre de la ventana a eliminar como argumento.
    '''    
    cv2.destroyAllWindows()

