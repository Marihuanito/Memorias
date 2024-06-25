'''
Crea un programa que se conecte a una base de datos SQLite y permita realizar operaciones CRUD 
(Crear, Leer, Actualizar, Eliminar) en una tabla de empleados. Debe incluir funciones para agregar 
nuevos empleados, mostrar todos los empleados, actualizar la información de un empleado y eliminar empleados.

'''

import sqlite3

class BaseDatos:
    def __init__(self) -> None:
        # Constructor
        self.conn = sqlite3.connect('empresa.db')
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        #Funcion para crear tabla.
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                apellido TEXT,
                                edad INTEGER,
                                departamento TEXT,
                                salario REAL)''')
        self.conn.commit()
    
    def agregar_empleado(self, nombre, apellido, edad, departamento, salario):
        # Código para agregar un empleado a la base de datos
        try:            
            self.cursor.execute("INSERT INTO empleados (Nombre, apellido, edad, departamento, salario) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, edad, departamento, salario)) # Consulta para insertar
            self.conn.commit() # Realiza la inserción.
        except sqlite3.Error as e:
            print(f"Error al agregar empleado: {e}")

    def mostrar_empleados(self):
        # Código para mostrar todos los empleados
        try:
            self.cursor.execute("SELECT * FROM empleados")
            # el método fechall es un metodo de cursor que realiza la consulta y devuelve en una tupla todos los resultados
            filas = self.cursor.fetchall()
            for fila in filas:
                print(fila)
        except sqlite3.Error as e:
            print(f"Error al mostrar empleado: {e}")
        

    def actualizar_empleado(self, id, nombre, apellido, edad, departamento, salario):
        # Código para actualizar un empleado en la base de datos
        try:
            self.cursor.execute("UPDATE empleados SET nombre = ?, apellido = ?, edad = ?, departamento = ?, salario = ? WHERE Id = ?", (nombre, apellido, edad, departamento, salario, id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar empleado: {e}")

    def eliminar_empleado(self, id):
        # Código para eliminar un empleado de la base de datos
        try:
            self.cursor.execute("Delete FROM empleados WHERE Id = ?", (id,)) # La coma es necesaria para que se interprete como una tupla.
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar empleado: {e}")
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

#Función para reducir código y no repetir todas las solicitudes de edad, salario e Id.
def solicitar_numero(prompt, tipo=int):
    # prompt le pasamos el texto que se enseñará al usuario.
    # tipo=int eso no significa el tipo de entrada sea int si o si. Se espara un int, pero puede ser otro tipo de número.
    # si no se especifica otra cosa, el convierte a int.
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print(f"Ingrese un {tipo.__name__} válido.") 


def main():
    # Menú principal del programa
    bd = BaseDatos()
        
    while True:
        print("Gestión de Empleados\n 1. Agregar Empleado \n 2. Mostrar Empleados \n 3. Actualizar Empleado \n 4. Eliminar Empleado \n 5. Salir")
        seleccion = input("Elige una opción (1-5): ")

        if seleccion == '1':
            nombre = input("Introduzca nombre del nuevo empleado: ")
            apellido = input("Apellido: ")
            edad = solicitar_numero("Edad: ")
            departamento = input("Departamento: ")
            salario = solicitar_numero("Salario: ", float)
            bd.agregar_empleado(nombre, apellido, edad, departamento, salario)
        elif seleccion == '2':
            bd.mostrar_empleados()
        elif seleccion == '3':
            id = solicitar_numero("Introduzca el Id del usuario a modificar: ")
            nombre = input("Introduzca nombre del empleado: ")
            apellido = input("Apellido: ")
            edad = solicitar_numero("Edad: ")
            departamento = input("Departamento: ")
            salario = solicitar_numero("Salario: ", float)
            bd.actualizar_empleado(id, nombre, apellido, edad, departamento, salario)
        elif seleccion == '4':
            id = solicitar_numero("Introduzca el Id del usuario a eliminar: ")
            bd.eliminar_empleado(id)
        elif seleccion == '5':
            print("Saliendo...")
            bd.cerrar_conexion()
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.\n")

if __name__ == "__main__": #Patron que asegura que ciertas partes del código se ejecutan cuando el SCRIPT se ejecuta directamente. y no se usan cuando se importa como un módulo de otro SCRIPT.
    main()


