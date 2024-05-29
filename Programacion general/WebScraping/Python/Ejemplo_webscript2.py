# Traer cualquier texto de la web https://scrapepark.org/spanish/ que tenga la palabra descuento u oferta.

import requests
from bs4 import BeautifulSoup
import re

string_a_buscar = ["descuento", "oferta"]

# Realizamos el GET
URL_BASE =  'https://scrapepark.org/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_bruto = pedido_obtenido.text

soup = BeautifulSoup(html_bruto, "html.parser")

for string in string_a_buscar:
    try:
        resultado = soup.find(string=re.compile(string))
        print(resultado.text)
    except AttributeError:
        print(f"El string '{string}' no fue encontrado")