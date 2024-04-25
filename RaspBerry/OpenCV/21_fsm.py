#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR:   CIFPN1                                                  Noviembre/2020
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: FSM                                   VERSIÓN: 1.0      
//   DISPOSITIVO: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC                              
//   S.O.: Buster 							                Versión Python:   3.7.3                             
//   TARJETA DE APLICACIÓN: Raspberry Pi 4 B                   
////////////////////////////////////////////////////////////////////////////////////
                                  MÁQUINA DE ESTADOS FINITA
////////////////////////////////////////////////////////////////////////////////////
"""
#////////////////////////////////////////////////////////////////////////////////////
# IMPORTAR LIBRERÍAS E INSTANCIAR CLASES
#////////////////////////////////////////////////////////////////////////////////////
import cv2
import time
from fysom import Fysom  #Libreria o Módulo que contiene las funciones de la FSM
import RPi.GPIO as GPIO
import estados_fsm #Librería con todos los estados de la FSM

#-----------------------------------------------------------------------------------
#Importamos las librerías para el manejo de la pantalla OLED
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#////////////////////////////////////////////////////////////////////////////////////
# VARIABLES GLOBALES
#////////////////////////////////////////////////////////////////////////////////////
#------------------------------------------------------------------------------------
#Variables para la pantalla OLED
#------------------------------------------------------------------------------------
RST = None #numero de pin donde esta conectado el pin RESET de la pantalla oled 
DC = 23 #numero de pin donde esta conectado el pin DC de la pantalla oled
SPI_PORT = 0 #puerto SPI
SPI_DEVICE = 0 #dispositivo SPI

#------------------------------------------------------------------------------------
salida = False    #variable de salida de las funciónes que contendrá lo que ha sucedido

#////////////////////////////////////////////////////////////////////////////////////
# CONFIGURACIÓN PUERTOS GPIO Y RECURSOS A UTILIZAR
#////////////////////////////////////////////////////////////////////////////////////
GPIO.setmode(GPIO.BCM) #Establecemos el sistema de numeracion de pines BCM
GPIO.setup(16, GPIO.OUT, initial=0) ## GPIO 16 como salida
GPIO.setup(20, GPIO.OUT, initial=0) ## GPIO 20 como salida
GPIO.setup(21, GPIO.OUT, initial=0) ## GPIO 21 como salida

#------------------------------------------------------------------------------------
#MÁQUINA DE ESTADOS FINITA (FSM)
#------------------------------------------------------------------------------------
'''
ESTADOS         FUNCIONES                                  
UNO             uno_dos()  TRANSICIONA DEL ESTADO UNO-->DOS    
DOS             dos_tres() TRANSICIONA DEL ESTADO DOS-->TRES    
TRES            tres_uno() TRANSICIONA DEL ESTADO TRES-->UNO   

'''
covid19 = Fysom({ 'initial': 'UNO',     # Estado inicial de la máquina.
        	      'events': [          # Lista de transiciones (eventos) de la máquina
                {'name': 'UNO_DOS', 'src': 'UNO', 'dst': 'DOS'}, 
                {'name': 'DOS_TRES', 'src': 'DOS', 'dst': 'TRES'},
                {'name': 'TRES_UNO', 'src': 'TRES', 'dst': 'UNO'},] })
#------------------------------------------------------------------------------------
# Pantalla OLED
#------------------------------------------------------------------------------------
#creamos el objeto controlador
oled=Adafruit_SSD1306.SSD1306_128_64(rst=RST)
#definimos altura y anchura de la pantalla
anchura = oled.width
altura = oled.height
#creamos tantos objetos imagen sobre los cuales vamos a dibujar usando PIL, 
#como mensajes distintos queramos visualizar
#---------------------------------------
# "Estado UNO"
#---------------------------------------
image = Image.new('1', (anchura,altura)) #El '1' significa monocromo
draw = ImageDraw.Draw(image)
#---------------------------------------
# "Estado DOS"
#---------------------------------------
image1 = Image.new('1', (anchura,altura))
draw1 = ImageDraw.Draw(image1)
#---------------------------------------
# "Estado TRES"
#---------------------------------------
image2 = Image.new('1', (anchura,altura))
draw2 = ImageDraw.Draw(image2)

#inicializamos la pantalla
oled.begin()
#limpiamos la pantalla
oled.clear()
#.display es la funcion que mostrara los cambios a la pantalla
oled.display()
#escogemos una fuente, en este caso la predefinida
#font = ImageFont.load_default()
#Podemos poner la ruta completa de una fuente y configurar tamaño
#font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 28)
font = ImageFont.truetype('/usr/share/fonts/truetype/crosextra/Carlito-BoldItalic.ttf',28)
#------------------------------------------------------------------------------------                  

#////////////////////////////////////////////////////////////////////////////////////
# FUNCIONES
#////////////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////////////
# ANTES DEL PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////


#-------------------------------------------------------------------------------- 

#////////////////////////////////////////////////////////////////////////////////////
# PROGRAMA PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
try:                 
    while True:      #iniciamos un loop infinito
        #****************************************************************************
        # Estado UNO
        #****************************************************************************
        if covid19.current == "UNO":
            print('Estado: ',covid19.current)

            # Escribimos "1º state"
            draw.text((0,0),'     1º',font=font,fill=255)
            draw.text((0,30),'  state',font=font,fill=255)
            #mostramos la pantalla con ambos comandos
            oled.image(image)
            oled.display()
            
            # Llamamos a la función "uno_dos()"
            tiempo_inicial = time.perf_counter()
            print('inicial "UNO": ',tiempo_inicial)
            salida=estados_fsm.uno_dos(tiempo_inicial)
            print('salida "UNO": ',salida)
            print('=========================================')

            if salida == True:
                print('Transicionamos al estado DOS...')
                time.sleep(3)
                covid19.UNO_DOS()     # Transicionamos al estado DOS
            else:                   
                print('Algo salió mal en el estado UNO...')
        #****************************************************************************
        # Estado DOS
        #****************************************************************************
        if covid19.current == "DOS":
            print('Estado: ',covid19.current)

            # Escribimos "2º state"
            draw1.text((0,0),'     2º',font=font,fill=255)
            draw1.text((0,30),'  state',font=font,fill=255)
            #mostramos la pantalla con ambos comandos
            oled.image(image1)
            oled.display()
            
            # Llamamos a la función "uno_dos()"
            tiempo_inicial = time.perf_counter()
            print('inicial "DOS": ',tiempo_inicial)
            salida=estados_fsm.dos_tres(tiempo_inicial)
            print('salida "DOS": ',salida)
            print('=========================================')

            if salida == True:
                print('Transicionamos al estado TRES...')
                time.sleep(3)
                covid19.DOS_TRES()     # Transicionamos al estado TRES
            else:                   
                print('Algo salió mal en el estado DOS...')
        #****************************************************************************
        # Estado TRES
        #****************************************************************************
        if covid19.current == "TRES":
            print('Estado: ',covid19.current)

            # Escribimos "3º state"
            draw2.text((0,0),'     3º',font=font,fill=255)
            draw2.text((0,30),'  state',font=font,fill=255)
            #mostramos la pantalla con ambos comandos
            oled.image(image2)
            oled.display()
            
            # Llamamos a la función "uno_dos()"
            tiempo_inicial = time.perf_counter()
            print('inicial "TRES": ',tiempo_inicial)
            salida=estados_fsm.tres_uno(tiempo_inicial)
            print('salida "TRES": ',salida)
            print('=========================================')

            if salida == True:
                print('Transicionamos al estado UNO...')
                time.sleep(3)
                covid19.TRES_UNO()     # Transicionamos al estado UNO
            else:                   
                print('Algo salió mal en el estado TRES...')
        #----------------------------------------------------------------------------                       

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print("El usuario ha pulsado Ctrl+C...")
except:
    print("error inesperado")
finally:
    print('Salimos por finally...')
    GPIO.cleanup() ## Hago una limpieza de los GPIO
    oled.clear()
    oled.display()
    cv2.destroyAllWindows()

