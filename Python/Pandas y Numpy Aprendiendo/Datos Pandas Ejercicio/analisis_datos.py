"""
Enunciado:

Crea un programa en Python que realice un análisis básico de datos utilizando la biblioteca pandas. 
El programa debe permitir al usuario cargar un archivo CSV y realizar operaciones como mostrar estadísticas descriptivas, 
filtrar datos y generar gráficos simples.

Requisitos:
Bibliotecas Requeridas: Utiliza las bibliotecas pandas y matplotlib.

Paso 1: Carga de Datos:

Permite al usuario especificar la ruta de un archivo CSV.
Carga los datos del archivo CSV en un DataFrame de pandas.
Paso 2: Estadísticas Descriptivas:

Muestra estadísticas descriptivas básicas del DataFrame, como media, mediana, desviación estándar, y conteo de valores únicos por columna.
Paso 3: Filtrado de Datos:

Permite al usuario filtrar los datos por una columna especificada y un valor dado.
Paso 4: Generación de Gráficos:

Genera gráficos simples como histogramas y gráficos de barras para columnas numéricas o categóricas del DataFrame.
Paso 5: Menú Principal:

Implementa un menú principal con las opciones:
1. Cargar Datos
2. Mostrar Estadísticas Descriptivas
3. Filtrar Datos
4. Generar Gráficos
5. Salir
"""

import pandas as pd
import matplotlib.pyplot as plt

class AnalisisDatos:
    def __init__(self):
        # Constructor
        self.archivo_csv = 'datos_ejemplo.csv'

        '''
        Me está dando problemas al leer las líneas del CSV que tienen tildes. Esto en teoría se debe a la codificación.
        Para solucionarlo se pone la codificación ISO-8858-1 que es general en europa. Si siguiese dando problemas, otra forma de
        resolver el problema es instalando la librería chardet, ella nos puede indicar con que codificación está escrito el csv
        y sabiendo esto, lo podemos leer poniendo esa misma codificación.

        '''
        self.datos = pd.read_csv(self.archivo_csv, encoding='ISO-8859-1')

    def cargar_datos(self):
        # Cargar datos del archivo CSV
        print(self.datos.head()) # Muestra solo las 5 primeras filas del CSV
        #print(datos) # Muestra todo el CSV

    def mostrar_estadisticas(self):
        # Mostrar estadísticas descriptivas
        '''
        El metodo describe proporciona de forma automática varias estadísticas con las columnas numéricas (con include=all utiliza todas las columnas)
        como mediana, media, desviación estandar...etc..
        '''
        print(self.datos.describe())

    def filtrar_datos(self, columna, valor):
        # Filtrar datos por una columna y un valor
        if columna not in self.datos.columns:
            raise ValueError(f"la columna {columna} no existe en los datos.")
        
        tipo_columna = self.datos[columna].dtype

        #Filtramos dependiendo del tipo de columna.
        if pd.api.types.is_numeric_dtype(tipo_columna):
            filtro_columna = f"{columna} {valor}"
        elif pd.api.types.is_datetime64_any_dtype(tipo_columna):
            #Primero nos aseguramos de que el formato fecha es correcto
            '''
            errors='coerce' es un parámetro que indica qué hacer si encuentra un valor que no puede convertir a datetime. 
            Con 'coerce', cualquier valor que no pueda ser convertido se reemplazará con NaT (Not a Time), que es el 
            equivalente a NaN (Not a Number) para objetos datetime.

            '''
            self.datos[columna] = pd.to_datetime(self.datos[columna], errors='coerce')
            filtro_columna = f"{columna} {valor}"
        elif pd.api.types.is_string_dtype(tipo_columna):
            filtro_columna = f"{columna}.str.contains('{valor}', na=False)"
        else:
            raise ValueError("Tipo de columna no soportado.")
        
        resultado = self.datos.query(filtro_columna)
        return(resultado)

    def generar_graficos(self):
        # Generar gráficos simples
        self.datos.plot.scatter(x='Edad',y='Salario') #Gráfico de dispersión
        plt.title('Relación entre Edad y Salario')
        plt.xlabel('Edad')
        plt.ylabel('Salario')
        plt.show()

        serie = self.datos.Departamento.value_counts() #Gráfico circular
        serie.plot.pie(autopct= '%1.1f%%',title='Distribución por Departamento')

        plt.show()

        # Gráfico de barras ordenado por Edad
        # Primero, ordenamos el DataFrame por 'Edad' para luego graficarlo
        df_ordenado = self.datos.sort_values(by='Edad')
        df_ordenado.plot.bar(x='Edad', y='Salario', title='Salario por Edad (ordenado)')
        plt.xlabel('Edad')
        plt.ylabel('Salario')
        plt.show()

def main():
     
     Datos_padre = AnalisisDatos()
     while True:
        print("Análisis de Datos\n 1. Cargar Datos\n 2. Mostrar Estadísticas Descriptivas\n 3. Filtrar Datos\n 4. Generar Gráficos\n 5. Salir")
        seleccion = input("Elige una opción (1-5): ")

        if seleccion == '1':
            # Cargar datos
            Datos_padre.cargar_datos()

        elif seleccion == '2':
            # Mostrar estadísticas descriptivas
            Datos_padre.mostrar_estadisticas()

        elif seleccion == '3':
            # Filtrar datos. 
            print("Introduce la columna por la que deseas filtrar (o 'salir' para terminar): ")
            columna = input()
            if columna.lower() == 'salir':
                break

            print("Introduce la condición para el filtro (por ejemplo, '> 30', 'Ventas', '> \"2022-02-01\"'): ")
            condicion = input()
            try:
                resultado = Datos_padre.filtrar_datos(columna, condicion)
                print(resultado)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif seleccion == '4':
            # Generar gráficos
            Datos_padre.generar_graficos()
            print("4")
        elif seleccion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.\n")


if __name__ == "__main__":
    main()