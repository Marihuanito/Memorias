#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este no lo hemos estudiado en clase.
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR: CIFPN1                                             Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: ESTUDIO BORDES                          VERSIÓN: 1.0       
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
                      Estudio de los bordes
Sintaxis: cv2.copyMakeBorder (src, top, bottom, left, right, borderType, value)

Parámetros:
src: es la imagen de origen.
arriba: es el ancho del borde en número de píxeles en la dirección superior.
bottom: es el ancho del borde en número de píxeles en la dirección inferior.
left: es el ancho del borde en número de píxeles en la dirección izquierda.
derecha: es el ancho del borde en número de píxeles en la dirección correcta.
borderType: representa qué tipo de borde se agregará. Está definido por banderas como
           cv2.BORDER_CONSTANT , cv2.BORDER_REFLECT , etc.
Valor: es un parámetro opcional que representa el color del borde
       si el tipo de borde es cv2.BORDER_CONSTANT .
       
cv2.BORDER_CONSTANT: Agrega un borde de color constante.
                     El valor debe darse como siguiente argumento.
cv2.BORDER_REFLECT: El borde será un reflejo espejo de los elementos del borde.
                    Supongamos que si la imagen contiene letras " abcdefg ", 
                    la salida será " gfedcba | abcdefg | gfedcba ".
cv2.BORDER_REFLECT_101 o cv2.BORDER_DEFAULT: hace el mismo trabajo que cv2.BORDER_REFLECT
                    pero con un ligero cambio. Supongamos que si la imagen contiene letras
                    " abcdefgh ", la salida será " gfedcb | abcdefgh | gfedcba ".
cv2.BORDER_REPLICATE: replica el último elemento.
                    Supongamos que si la imagen contiene letras " abcdefgh"
                    Entonces la salida será" aaaaa | abcdefgh | hhhhh ".
////////////////////////////////////////////////////////////////////////////////////
"""
#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2
import numpy as np
from matplotlib import pyplot as plt #Aquí importamos y creamos el objeto 'plt'

#////////////////////////////////////////////////////////////////////////////////////
# VARIABLES GLOBALES
#////////////////////////////////////////////////////////////////////////////////////
BLUE = [0,0,255]

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
    img1 = cv2.imread('mario.jpg')
    replicate = cv2.copyMakeBorder(img1,40,40,10,10,cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1,10,40,40,10,cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1,40,10,10,40,cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1,40,40,40,40,cv2.BORDER_WRAP)
    constant= cv2.copyMakeBorder(img1,40,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
    
    #si mostramos la imagen con cv2 el color que muestra el borde es rojo.
    #cv2 utiliza BGR y la variable BLUE vale-->[0,0,255]
    cv2.imshow('1_borde',img1)
    cv2.imshow('2_borde',replicate)
    cv2.imshow('3_borde',reflect)
    cv2.imshow('4_borde',reflect101)
    cv2.imshow('5_borde',wrap)
    cv2.imshow('6_borde',constant)

    '''    
    #si mostramos la imagen con plt el color que muestra el borde es azul.
    #matplotlib utiliza RGB y la variable BLUE vale-->[0,0,255]

    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
    plt.show()
    '''     
    cv2.waitKey(0)

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    cv2.destroyAllWindows()
