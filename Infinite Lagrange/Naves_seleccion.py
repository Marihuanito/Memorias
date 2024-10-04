import random

# Datos base para las naves
naves = {
    "Empresas Encargadas": {
        "Antonios": {
            "Transportistas": ["Mariscal Crux"],
            "Naves Auxiliares": [],
            "Barcos de batalla": ["Constantino", "Ranger"],
            "Cruceros": ["Jaeger", "Depredador"],
            "Destructores": ["Guardian", "Husar Alado"],
            "Fragatas": ["Reliat", "Carilion"],
            "Corbetas": ["Vacío Mágico", "Buscanebulosas", "Defensora Celular"],
            "Cazas": ["Mistral", "Vitas-B", "Vitas-A", "Anderson"]
        },
        "Jupiter": {
            "Transportistas": ["Cielo Eterno"],
            "Barcos de batalla": ["Tormenta Eterna"],
            "Cruceros": ["Conamara", "Calisto", "IO"],
            "Destructores": ["Quaoar", "Ceres", "Eris I"],
            "Fragatas": ["Mare Imbrium", "Mare Serenitatus", "Mare Nubium", "Mare Tranquilitatis"],
            "Corbetas": ["Hale-Bopp", "S-Levy9"],
            "Cazas": ["Janbiya", "Raya", "Espora", "Terranova"]
        },
        "NOMA": {
            "Transportistas": ["Ballena Solar"],
            "Naves Auxiliares": ["Ediacaran"],
            "Barcos de batalla": ["Lanza de Urano"],
            "Cruceros": ["Quimera", "Cono de luz", "Aldabra"],
            "Destructores": ["Tundra", "Taurus"],
            "Fragatas": ["Noma M470", "Rubí", "XenoStinger"],
            "Corbetas": ["Bestia Roja", "Asesina Silenciosa"],
            "Cazas": ["Strix", "Rana", "Sandrake"]
        },
        "Pacto del Alba": {
            "Transportistas": ["CV3000"],
            "Naves Auxiliares": ["FSV830"],
            "Barcos de batalla": ["ST59"],
            "Cruceros": ["CAS066", "KCCPV"],
            "Destructores": ["AC721"],
            "Fragatas": ["FG-300"],
            "Corbetas": ["CV-T800", "CV-M011", "CV-11003"],
            "Cazas": ["BR050", "AT021", "SC002"]
        }
    },
    "Desempeño Estratégico": {
        "Fuego Excepcional": {
            "Transportistas": ["Cielo Eterno", "Mariscal Crux"],
            "Naves Auxiliares": ["Ediacaran"],
            "Barcos de batalla": ["Thunderbolt", "Lanza de Urano", "Constantino", "Tormenta Eterna", "Ranger"],
            "Cruceros": ["Conamara", "Quimera", "Cono de luz", "Calisto", "IO", "CAS066", "KCCPV"],
            "Destructores": ["Aldabra", "Quaoar", "Guardian", "Husar Alado", "Taurus", "Eris I"],
            "Fragatas": ["Reliat", "Mare Imbrium", "Mare Serenitatus", "Noma M470", "Rubí", "Xeno", "Mare Nubium"],
            "Corbetas": ["S-Levy9", "CV-T800", "CV-M011", "Vacío Mágico", "Buscanebulosas", "Defensora Celular"],
            "Cazas": ["BR050", "AT021", "Raya", "Vitas-B", "Vitas-A", "Leal", "Rana"]
        },
        "Combate Sostenido": {
            "Transportistas": [],
            "Naves Auxiliares": ["FSV830"],
            "Barcos de batalla": ["ST59", "Lanza de Urano"],
            "Cruceros": ["Quimera", "IO", "CAS066"],
            "Destructores": ["Aldabra", "Guardian", "Husar Alado", "Taurus", "Eris I"],
            "Fragatas": ["Reliat", "Mare Serenitatus", "Carilion", "Rubí", "FG-300"],
            "Corbetas": ["S-Levy9", "CV-M011", "Vacío Mágico", "Bestia Roja"],
            "Cazas": ["BR050", "AT021", "SC002", "Raya", "Vitas-B", "Anderson", "Leal"]
        },
        "Estrategia y Apoyo": {
        "Transportistas": ['Cielo Eterno', 'Mariscal Crux', 'CV3000', 'Ballena Solar'],
        "Naves Auxiliares": ['Ediacaran', 'FSV830'],
        "Barcos de batalla": ['Thunderbolt', 'ST59'],
        "Cruceros": ['CAS066', 'Conamara', 'Jaeger', 'Depredador', 'Cono de Luz', 'KCCPV'],
        "Destructores": ['Guardián', 'Húsar Alado', 'Taurus', 'Ceres', 'AC721'],
        "Fragatas": ['Mare Tranquilitatis', 'Carilion', 'Xeno', 'FG-300', 'Noma M470'],
        "Corbetas": ['Hale-Bopp', 'CV-M011', 'Bestia Roja', 'CV-11003'],
        "Cazas": ['AT021', 'Janbiya', 'Espora', 'Terranova', 'Sandrake', 'SC002']
        },
        "cazas_y_corbetas": {
        "Transportistas": [],
        "Naves Auxiliares": [],
        "Barcos de batalla": [],
        "Cruceros": [],
        "Destructores": [],
        "Fragatas": [],
        "Corbetas": [
        'Hale-Bopp', 'S-Levy9', 'CV-T800', 'CV-M011', 'Vacío Mágico',
        'Bestia Roja', 'Buscanebulosas', 'Defensora Celular', 'CV-11003', 'Asesina Silenciosa'
        ],
        "Cazas": [
        'BR050', 'AT021', 'SC002', 'Raya', 'Vitas-B', 'Anderson', 'Leal',
        'Mistral', 'Janbiya', 'Espora', 'Terranova', 'Vitas-A', 'Strix', 'Rana', 'Sandrake'
        ]
        }
    },
    "Desempeño Táctico": {
        "Armas de Proyectil": {
            "Transportistas": [],
            "Naves Auxiliares": [],
            "Barcos de batalla": [],
            "Cruceros": ["Cono de Luz", "Calisto", "CAS066", "KCCPV"],
            "Destructores": ["Guardian", "Quaoar", "Husar Alado", "AC721"],
            "Fragatas": ["Reliat", "Mare Serenitatis", "Mare Tranquilitatis", "Rubí"],
            "Corbetas": ["S-Levy9", "CV-M011", "Vacío Mágico", "Bestia Roja", "Defensora Celular"],
            "Cazas": ["BR050", "AT021", "Janbiya", "Raya", "Vitas-A", "Rana"]
        },
        "Armas de Fuego Directo": {
            "Transportistas": ["Mariscal Crux"],
            "Naves Auxiliares": [],
            "Barcos de batalla": ["Thunderbolt", "Lanza de Urano", "Constantino", "ST59", "Tormenta Eterna", "Ranger"],
            "Cruceros": ["Conamara", "Jaeger", "Quimera", "IO", "CAS066", "KCCPV"],
            "Destructores": ["Aldabra", "Guardian", "Taurus", "Eris I", "Quaoar", "AC721"],
            "Fragatas": ["Mare Imbrium", "Mare Tranquilitatis", "Carilion", "Rubí", "FG-300"],
            "Corbetas": ["CV-T800", "CV-M011", "Buscanebulosas", "Asesina Silenciosa"],
            "Cazas": ["AT021", "SC002", "Mistral", "Vitas-B", "Anderson", "Leal", "Espora", "Terranova", "Strix", "Sandrake"]
        }
    }
}
# Función que va filtrando naves en bucle
def obtener_naves_filtradas(faccion, desempeno_estrategico, desempeno_tactico):
    # Inicializar el diccionario para almacenar las naves filtradas.
    naves_filtradas = {
        "Transportistas": set(),
        "Naves Auxiliares": set(),
        "Barcos de batalla": set(),
        "Cruceros": set(),
        "Destructores": set(),
        "Fragatas": set(),
        "Corbetas": set(),
        "Cazas": set()
    }
    
    ##------FASE 1: Filtrar por facción--------##
    for tipo in naves["Empresas Encargadas"][faccion].keys():
        naves_filtradas[tipo].update(naves["Empresas Encargadas"][faccion][tipo])

    ##------FASE 2: Filtrar por desempeño estratégico--------##
    for tipo in naves_filtradas.keys():
        naves_filtradas[tipo] &= set(naves["Desempeño Estratégico"][desempeno_estrategico][tipo])

    ##------FASE 3: Filtrar por desempeño táctico--------##
    for tipo in naves_filtradas.keys():
        naves_filtradas[tipo] &= set(naves["Desempeño Táctico"][desempeno_tactico][tipo])
    
    return naves_filtradas
# 
def obtener_mejor_opcion_nave(nave_especifica):
    mejor_probabilidad = 0
    mejores_opciones = []

    for faccion in naves["Empresas Encargadas"].keys():
        for desempeno_estrategico in naves["Desempeño Estratégico"].keys():
            for desempeno_tactico in naves["Desempeño Táctico"].keys():
                naves_filtradas = obtener_naves_filtradas(faccion, desempeno_estrategico, desempeno_tactico)
                probabilidad = calcular_probabilidad_nave_especifica(naves_filtradas, nave_especifica)

                if probabilidad > mejor_probabilidad:
                    mejores_opciones = [(faccion, desempeno_estrategico, desempeno_tactico)]
                    mejor_probabilidad = probabilidad
                elif probabilidad == mejor_probabilidad:
                    mejores_opciones.append((faccion, desempeno_estrategico, desempeno_tactico))

    return mejores_opciones, mejor_probabilidad
# Función para calcular probabilidad de obtener una nave específica
def calcular_probabilidad_nave_especifica(naves_filtradas, nave_especifica):
    todas_naves = sum(len(naves_filtradas[tipo]) for tipo in naves_filtradas)
    for tipo, lista_naves in naves_filtradas.items():
        if nave_especifica in lista_naves:
            return (1 / todas_naves) * 100 if todas_naves > 0 else 0
    return 0

def calcular_probabilidad(naves_filtradas, tipo_nave):
    # Con la función for vamos a recorrer el diccionario naves filtrada según el tipo, el tipo se añadirá a len(naves_filtradas[tipo])
    # y len contará las naves que hay en el diccionario de ese tipo y se irán sumando en cada iteración con sum.
    todas_naves = sum(len(naves_filtradas[tipo]) for tipo in naves_filtradas)
    naves_tipo = len(naves_filtradas.get(tipo_nave, [])) # .get nos permite obtener las naves que hay según el tipo que le pasemos.
    # en caso de no encontrar nada devolverá un conjunto vacío []. Por último len nos cuenta cuantas naves hay de ese tipo.
    
    if todas_naves == 0:
        return 0
    
    probabilidad = (naves_tipo / todas_naves) * 100
    return probabilidad
# Funciona para calcular las mejores opciones según el tipo.
def obtener_mejor_opcion_tipo(tipo_objetivo):
    mejor_probabilidad = 0
    mejores_opciones = []

    for faccion in naves["Empresas Encargadas"].keys():
        for desempeno_estrategico in naves["Desempeño Estratégico"].keys():
            for desempeno_tactico in naves["Desempeño Táctico"].keys():
                #Hasta aquí simplemente vamos obteniendo las naves que quedarían después de cada 3 fases.
                naves_filtradas = obtener_naves_filtradas(faccion, desempeno_estrategico, desempeno_tactico)
                #Aquí ahora vamos a ver la probabilidad.
                probabilidad = calcular_probabilidad(naves_filtradas, tipo_objetivo)
                
                if probabilidad > mejor_probabilidad:
                    mejores_opciones = [(faccion, desempeno_estrategico, desempeno_tactico)]
                    mejor_probabilidad = probabilidad
                elif probabilidad == mejor_probabilidad:
                    mejores_opciones.append((faccion, desempeno_estrategico, desempeno_tactico))

    return mejores_opciones, mejor_probabilidad
# Función para la primera opción.
def fase_por_fase():

    ## Código para que el usuario nos indique por pantalla las fases.
    print("\nSelecciona la facción:")
    facciones = list(naves["Empresas Encargadas"].keys())
    for i, faccion in enumerate(facciones):
        print(f"{i}. {faccion}")
    eleccion_faccion = int(input("Elige el número de la facción: "))
    
    print("\nSelecciona el Desempeño Estratégico:")
    desempenos_estrategicos = list(naves["Desempeño Estratégico"].keys())
    for i, desempeno in enumerate(desempenos_estrategicos):
        print(f"{i}. {desempeno}")
    eleccion_estrategico = int(input("Elige el número del Desempeño Estratégico: "))

    print("\nSelecciona el Desempeño Táctico:")
    desempenos_tacticos = list(naves["Desempeño Táctico"].keys())
    for i, desempeno in enumerate(desempenos_tacticos):
        print(f"{i}. {desempeno}")
    eleccion_tactico = int(input("Elige el número del Desempeño Táctico: "))
    # Aquí podemos ir imprimiendo los valores para ver si son correctos.
    faccion_elegida = facciones[eleccion_faccion]
    desempeno_estrategico_elegido = desempenos_estrategicos[eleccion_estrategico]
    desempeno_tactico_elegido = desempenos_tacticos[eleccion_tactico]

    naves_filtradas = obtener_naves_filtradas(faccion_elegida, desempeno_estrategico_elegido, desempeno_tactico_elegido)
    return naves_filtradas
# Función para listar todas las naves.
def listar_todas_las_naves():
    naves_totales = []
    for faccion in naves["Empresas Encargadas"]:
        for tipo_nave in naves["Empresas Encargadas"][faccion]:
            naves_totales.extend(naves["Empresas Encargadas"][faccion][tipo_nave])
    return naves_totales
# Funciona para calcular las mejores opciones según una nave específica.
def obtener_mejor_opcion_nave_especifica():
    # Listar todas las naves para que el usuario elija
    print("\nLista de todas las naves disponibles:")
    todas_las_naves = listar_todas_las_naves()
    
    for i, nave in enumerate(todas_las_naves):
        print(f"{i + 1}. {nave}")
    
    # Elegir nave
    eleccion_nave = int(input("Elige el número de la nave que quieres consultar: "))
    nave_elegida = todas_las_naves[eleccion_nave - 1]

    # Obtener la mejor combinación de fases para obtener la nave seleccionada
    opciones, probabilidad = obtener_mejor_opcion_nave(nave_elegida)
    
    # Mostrar los resultados
    print(f"\nLas mejores combinaciones para obtener la nave '{nave_elegida}' son:")
    for opcion in opciones:
        print(f"Facción: {opcion[0]}, Desempeño Estratégico: {opcion[1]}, Desempeño Táctico: {opcion[2]}")
    print(f"Probabilidad: {probabilidad:.2f}%")

if __name__ == "__main__":
    print("Bienvenido al juego de desbloqueo de naves.")
    
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Jugar (Ir fase por fase y desbloquear naves)")
        print("2. Consultar mejor probabilidad para obtener una nave según su tipo")
        print("3. Consultar mejor probabilidad para obtener una nave en concreto")
        print("5. Salir")

        opcion = int(input("\nElige una opción (número): "))

        if opcion == 1:
            naves_finales = fase_por_fase()
            print("\nNaves finales:")
            for tipo, lista_naves in naves_finales.items():
                print(f"{tipo}: {lista_naves}")

            # Desbloquear nave aleatoria
            todas_naves = []
            for lista_naves in naves_finales.values():
                todas_naves.extend(lista_naves)
            if todas_naves:
                nave_desbloqueada = random.choice(todas_naves)
                print(f"\n¡Has desbloqueado la nave: {nave_desbloqueada}!")
            else:
                print("\nNo hay naves disponibles para desbloquear.")

        elif opcion == 2:
            while True:
                print("1. Transportistas")
                print("2. Naves Auxiliares")
                print("3. Barcos de batalla")
                print("4. Cruceros")
                print("5. Destructores")
                print("6. Fragatas")
                print("7. Corbetas")
                print("8. Cazas")
                opcion_tipo = int(input("Elige una de las opciones:"))
                if opcion_tipo == 1:
                    tipo_nave = "Transportistas"
                    break
                elif opcion_tipo == 2: 
                    tipo_nave = "Naves Auxiliares"
                    break
                elif opcion_tipo == 3: 
                    tipo_nave = "Barcos de batalla"
                    break
                elif opcion_tipo == 4: 
                    tipo_nave = "Cruceros"
                    break
                elif opcion_tipo == 5: 
                    tipo_nave = "Destructores"
                    break
                elif opcion_tipo == 6: 
                    tipo_nave = "Fragatas"
                    break
                elif opcion_tipo == 7: 
                    tipo_nave = "Corbetas"
                    break
                elif opcion_tipo == 8: 
                    tipo_nave = "Cazas" 
                    break 
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
   
            opciones, probabilidad = obtener_mejor_opcion_tipo(tipo_nave)
            print(f"\nLas mejores combinaciones para obtener {tipo_nave} son:")
            for opcion in opciones:
                print(opcion)
            print(f"Probabilidad: {probabilidad:.2f}%")

        elif opcion == 3:
            obtener_mejor_opcion_nave_especifica()  # Llamada a la nueva función para mostrar todas las naves


        elif opcion == 5:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
