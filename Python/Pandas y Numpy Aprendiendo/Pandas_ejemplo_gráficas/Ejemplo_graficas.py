import pandas as pd
import matplotlib.pyplot as plt

documento = pd.read_csv("listaclase.csv")

#print(documento.sample(10)) # 10 muestras aleatorias

#print(documento.describe()) # estadísitca básica 

""" Si ejecutamos describe podemos ver:
    - número de registros
    - media
    - desviacion estándar
    - mínimo
    - cuartiles
    - maximo
"""

documento.plot.scatter(x="Peso",y="Altura") # Con este ejemplo veriamos como contra mas altura mayor peso. Gráffico de dispersión.

plt.show()

serie = documento.Genero.value_counts()
serie.plot.pie(autopct= '%1.1f%%') #gráfico circular. con autopct ponemos porcentajes.

plt.show()

serie = documento.Edad.value_counts()
#serie.plot.bar() # Gráfico barras.
#serie.plot.barh() # Gráfico barras cambiando X por Y
serie = serie.sort_values(ascending=True) # Ordenamos los resultados
serie.plot.barh() 
plt.show()

documento.Altura.plot.hist(bins=5)
plt.show()

#documento.Altura.plot.density() # Gráfico de densidad. No fula bien XD pero al del video si que le va.
#plt.show()

documento.Altura.plot.box()
plt.show()

""" 
    Según el chico del video, esto solo es una muestra, pero el NO utilizaría estas gráficas para clientes ni para el.
    Hay una bliblioteca llamada plotly que tiene unas gráficas mucho mas profesiones.
    Fuente: https://www.youtube.com/watch?v=JUPi6Oo8stQ
    Librría Plotly: https://plotly.com/python/
"""