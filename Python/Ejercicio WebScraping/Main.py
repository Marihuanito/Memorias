'''
Crea un programa en Python que realice un web scraping a una página web de noticias y almacene los titulares y sus URLs
en una base de datos SQLite.

Requisitos:
Bibliotecas Requeridas: Utiliza las bibliotecas requests, BeautifulSoup, y sqlite3.

Paso 1: Scraping:

Especifica una URL de una página web de noticias (por ejemplo, BBC News, CNN, etc.).
Realiza una solicitud HTTP GET a la página especificada.
Analiza el contenido HTML de la página para extraer los titulares de las noticias y sus URLs correspondientes.

Paso 2: Almacenamiento en la Base de Datos:

Crea una base de datos SQLite llamada noticias.db.
Crea una tabla llamada titulares con las columnas id (entero, clave primaria, autoincremental), titular (texto) y url (texto).
Inserta los titulares y sus URLs en la tabla titulares.

Paso 3: Mostrar los Datos:

Crea una función que muestre todos los titulares almacenados en la base de datos.

Paso 4: Menú Principal:

Implementa un menú principal con las opciones:
1. Realizar Scraping y Almacenar Noticias
2. Mostrar Noticias Almacenadas
3. Salir

https://www.eldiariomontanes.es/santander/burger-king-abrira-local-santander-primero-mayo-20240219172540-nt.html?ref=https%3A%2F%2Fwww.eldiariomontanes.es%2Fsantander%2Fburger-king-abrira-local-santander-primero-mayo-20240219172540-nt.html
https://www.eldiariomontanes.es/
https://eldiariocantabria.publico.es/

'''

import requests
from bs4 import BeautifulSoup
import sqlite3

class NoticiasBD:

    def __init__(self) -> None:
        #Constructor
        self.conn = sqlite3.connect("noticias.db")
        self.cursor = self.conn.cursor()
    
    def crear_tabla(self):
        # Crear tabla
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS titulares (
                                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titular TEXT,
                                url TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear tabla: {e}")

    def insertar_titular(self, articulos):
        # Insertar titular en la base de datos
        for key in articulos:
            try:
                self.cursor.execute("INSERT INTO titulares (titular, url) VALUES (?, ?)",(key, articulos[key]))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"error al agregar artículo {e}")
                
        print(f"se han almacenado {len[articulos]} artículos en la base de datos.")
            #print(key, articulos[key])

    def mostrar_titulares(self):
        # Mostrar todos los titulares
        try:
            self.cursor.execute("SELECT * FROM titulares")
            # el método fechall es un metodo de cursor que realiza la consulta y devuelve en una tupla todos los resultados
            filas = self.cursor.fetchall()
            for fila in filas:
                id, titular, url = fila
                print(f"Titular: {titular}\nURL: {url}\n")
        except sqlite3.Error as e:
            print(f"Error al mostrar titulares: {e}")
        
    def cerrar_conexion(self):
        # Cerrar conexión
        self.cursor.close()
        self.conn.close()
        

def realizar_scraping():
    # URL de la página de noticias
    # Realizar solicitud HTTP GET
    URL_Base = 'https://eldiariocantabria.publico.es'
    try:
        request = requests.get(URL_Base)
        URL_obtenido = request.text
    except requests.exceptions.RequestException as e:
        print(f"error al realizar la solicitud: {e} \n")

    
    # Analizar contenido HTML con BeautifulSoup
    soup = BeautifulSoup(URL_obtenido, "html.parser")
    enlaces = []
    titulo_textos = []
    # Buscamos los títulos con la clase title
    titulos_h2 = soup.find_all('h2', class_= "title")
    # Extraer titulares y URLs
    for titulo in titulos_h2:
        enlace = titulo.find('a')['href'] # Nos busca en la etiqueta a con el atributo href.
        enlace = URL_Base + enlace
        #Guardamos en listas.
        titulo_textos.append(titulo.get_text(strip=True))
        enlaces.append(enlace)
    #Creamos un diccionario con las dos listas y retornamos el diccionario.
    articulos = {titulo: enlace for titulo, enlace in zip(titulo_textos, enlaces)}

    return articulos

    
def main():
    #Menú principal del programa

    noticias = NoticiasBD()

    while True:
        print("Gestión de Noticias\n 1. Realizar Scraping y Almacenar Noticias\n 2. Mostrar Noticias Almacenadas\n 3. Salir")
        seleccion = input("Elige una opción (1-3): ")

        if seleccion == '1':
            articulos = realizar_scraping()
            noticias.insertar_titular(articulos)
        elif seleccion == '2':
            noticias.mostrar_titulares()
        elif seleccion == '3':
            noticias.cerrar_conexion()
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.\n")

if __name__ == "__main__":
    main()

    #031026