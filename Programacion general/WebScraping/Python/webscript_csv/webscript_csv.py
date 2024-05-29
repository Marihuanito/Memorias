# Generar un archivo .csv con dos columnas: Una conteniendo el nombre del cliente y otra su testimonio.

import requests
from bs4 import BeautifulSoup
import csv


URL_BASE = 'https://scrapepark.org/spanish/'
solicitud = requests.get(URL_BASE)
html_bruto = solicitud.text

soup = BeautifulSoup(html_bruto, "html.parser")

datos_h5 = soup.find_all('h5', class_='customer-name')

Clientes = []
Comentarios = []

for dato in datos_h5:
    if(dato is not None):
        comentario = dato.parent
        comentario = comentario.find('p')
        Clientes.append(dato.get_text(strip=True))
        Comentarios.append(comentario.text)

Testimonios = {cliente: comentario for cliente, comentario in zip(Clientes, Comentarios)}

with open('datos.csv','w') as f:
    w = csv.writer(f)
    w.writerows(Testimonios.items())
