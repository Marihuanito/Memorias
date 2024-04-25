#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR: CIFPN1                                             Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: MANEJAR PIXEL                         VERSIÓN: 1.0      
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   Versión Python:   3.5.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 3 B+                   
////////////////////////////////////////////////////////////////////////////////////
                               Aprendiendo a manejar píxeles
////////////////////////////////////////////////////////////////////////////////////
"""
#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2
import numpy as np

img = cv2.imread('colores.png') # Creamos el objeto 'img'
                                # Imagen de 264px horizontales 182px verticales 

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
    '''La coordenada del pixel es [y,x]'''
    px = img[50,50]       #pixel azul. Como OpenCV lo da en BGR, la lista que nos 
    print ('azul: ',px)   #devuelve, será mayoritariamente azul [255,0,0]-->realmente[204,72,63]

    px = img[50,150]      #pixel rojo. Como OpenCV lo da en BGR, la lista que nos 
    print ('rojo: ',px)   #devuelve, será mayoritariamente rojo [0,0,255]-->realmente[36,28,237]

    px = img[150,50]      #pixel blanco. Como OpenCV lo da en BGR, la lista que nos 
    print ('blanco: ',px) #devuelve, será mayoritariamente blanco [255,255,255]

    px = img[150,150]     #pixel verde. Como OpenCV lo da en BGR, la lista que nos 
    print ('verde: ',px)  #devuelve, será mayoritariamente verde [0,255,0]-->realmente[76,177,34]
    '''############################################################################'''

    # accediendo solamente al valor Blue de un pixel del cuadro azul
    blue = img[50,50,0]   #si seleccionamos un pixel dentro del cuadro azul
    print (blue)          #al poner 0, en la lista,nos devuelve el nivel de Blue del formato BGR
                          #siendo la lista --> [204  72  63]print(blue) imprime -->204
    print(img.item(50,50,0)) #otra forma de acceder al rango BGR del pixel, en este caso a Blue

    # accediendo solamente al valor Green de un pixel del cuadro rojo
    green = img[50,150,1] #si seleccionamos un pixel dentro del cuadro rojo
    print (green)         #al poner 1, en la lista,nos devuelve el nivel de Green del formato BGR
                          #siendo la lista --> [ 36  28 237] print(green) imprime -->28
    print(img.item(50,150,1)) #otra forma de acceder al rango BGR del pixel, en este caso a Green

    # accediendo solamente al valor Red de un pixel del cuadro verde
    red = img[150,150,2]  #si seleccionamos un pixel dentro del cuadro verde
    print (red)           #al poner 0, en la lista,nos devuelve el nivel de Red del formato BGR
                          #siendo la lista --> [ 76 177  34]print(red) imprime -->34
    print(img.item(150,150,2)) #otra forma de acceder al rango BGR del pixel, en este caso a Red
    '''############################################################################'''

    #aquí, modificamos el pixel [150,200], de color verde, con un color blanco -->[255,255,255]
    img[150,200] = [255,255,255]
    print  ('pixel verde modificado',img[150,200]) #escribirá la lista BGR del color blanco-->[255,255,255]
    print  ('pixel verde sin modificar',img[155,200]) #escribirá la lista BGR del color verde-->[76,177,34]

    print ('shape: ',img.shape) #devuelve filas, columnas y canales -->[182,264,3]
    print ('size: ',img.size) #devuelve el tamaño--> 182 x 264 x 3 = 144144
    print ('type: ',img.dtype) #devuelve el tipo de datos de la imagen --> uint8

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")

except:
    print("error inesperado")

finally:
    print("Fin de programa")
