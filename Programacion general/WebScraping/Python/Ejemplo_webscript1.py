# De la web https://scrapepark.org/spanish/ Sacar las Patinetas que salgan por menos de $68.
import requests
from bs4 import BeautifulSoup


# Realizamos el GET
URL_BASE =  'https://scrapepark.org/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_bruto = pedido_obtenido.text

#print(html_bruto) # Si imprimimos aquí vemos el html de la web

soup = BeautifulSoup(html_bruto, "html.parser")
# Buscamos los div que tengan una clase detail-box
divs = soup.find_all('div', class_='detail-box')

#print(divs) # Si imprimimos vemos los divs que tienen como clase detail-box

productos = []
precios = []

for div in divs:
    # Si el div6 no es nulo Y el texto de div.5 es Patineta Y el precio es menor que 68:
    if (div.h6 is not None) and ('Patineta' in div.h5.text) and (int(div.h6.get_text(strip=True).replace('$','')) < 68):
        producto = div.h5.get_text(strip=True) #Para eliminar espacios
        precio = div.h6.get_text(strip=True).replace('$','') # Eliminamos espacios y ademas remplazamos el simbolo $ por vacio.
        productos.append(producto)
        precios.append(precio)
        #print(f'producto: {producto:<16} | precio: {precio}')

articulos = {producto: precio for producto, precio in zip(productos, precios)} # Agregamos un diccionario con ambas listas
print(articulos)
