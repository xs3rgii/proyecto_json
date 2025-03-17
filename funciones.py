import json

# Cargar el json (Abre el json como lectura y lo carga en un diccionario)
def cargar_json():
    with open("hardware.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
# Funcion para listar los procesadores
def listar_procesadores():
    datos = cargar_json()  # Carga los datos desde el archivo JSON
    print("\n--- Lista de procesadores ---\n")
    
    # Itera sobre los componentes del archivo JSON
    for componente in datos["componentes"]:
        if componente["categoria"] == "Procesador":
            modelo = componente["detalles"]["modelo"]
            marca = componente["detalles"]["marca"] 
            precio = componente["detalles"]["precio"] 
            nucleos = componente["detalles"]["especificaciones"]["nucleos"]
            print(f"Modelo: {modelo} | Marca: {marca} | Precio: {precio}€ | Núcleos: {nucleos}")

# Funcion para contar las tarjetas gráficas
def contar_tarjetas_graficas():
    datos = cargar_json()
    tarjetas = {}

    # Itera sobre los componentes del archivo JSON
    for componente in datos["componentes"]:
        if componente["categoria"] == "Tarjeta Gráfica":
            modelo = componente["detalles"]["modelo"]
            marca = componente["detalles"]["marca"]
            unidades = componente["detalles"]["disponibilidad"]["stock"]
            

            if modelo in tarjetas:
                tarjetas[modelo]["unidades"] += unidades
            else:
                tarjetas[modelo] = {"marca": marca, "unidades": unidades}  # Agrega el modelo al diccionario

    # Imprime la información de las tarjetas gráficas
    print("\n--- Tarjetas gráficas ---")
    total = 0
    for modelo, info in tarjetas.items():
        marca = info["marca"]
        unidades = info["unidades"]
        print(f"Marca: {marca} | Modelo: {modelo} | Unidades: {unidades}") 
        total += unidades  # Suma las unidades al total
    print(f"Total de tarjetas gráficas: {total}")

# Función para filtrar almacenamiento por precio
def filtrar_almacenamiento_por_precio(min_precio, max_precio):
    datos = cargar_json()
    almacenamientos = []

    # Itera sobre los componentes del archivo JSON
    for componente in datos["componentes"]:
        if componente["categoria"] == "Almacenamiento": 
            try:
                precio = float(componente["detalles"]["precio"]) 
                if min_precio <= precio <= max_precio:  # Filtra según el rango de precio
                    almacenamientos.append(componente["detalles"])  # Agrega el componente a la lista
            except ValueError:
                print(f"Error: El precio de {componente['detalles']['modelo']} no es válido.")

    # Imprime los componentes de almacenamiento que cumplen con el rango de precio
    if almacenamientos:
        print("\n--- Componentes de almacenamiento en el rango de precios ---")
        for almacenamiento in almacenamientos:
            print(f"Marca: {almacenamiento['marca']} | Modelo: {almacenamiento['modelo']} | Precio: ${almacenamiento['precio']:.2f}")
    else:
        print("No hay componentes de almacenamiento en ese rango de precios.")

# Función para buscar placas base compatibles con un procesador
def buscar_placas_base_compatibles():
    datos = cargar_json()  # Carga los datos desde el archivo JSON
    
    # Mostrar los procesadores disponibles
    print("\n--- Procesadores disponibles ---")
    for componente in datos["componentes"]:
        if componente["categoria"] == "Procesador":
            modelo = componente["detalles"]["modelo"]
            marca = componente["detalles"]["marca"]
            print(f"Modelo: {modelo} | Marca: {marca}")
    
    # Pedir el nombre del procesador
    nombre_procesador = input("\nIntroduce el nombre del procesador: ")

    # Buscar el procesador en los datos
    procesadores_encontrados = []
    for componente in datos["componentes"]:
        if componente["categoria"] == "Procesador" and nombre_procesador.lower() in componente["detalles"]["modelo"].lower():
            procesadores_encontrados.append(componente)
    
    if procesadores_encontrados:
        # Mostrar las compatibilidades de los procesadores encontrados
        for procesador_encontrado in procesadores_encontrados:
            compatibilidades_procesador = procesador_encontrado["detalles"]["compatibilidad"]
            print(f"\n--- Placas base compatibles con {procesador_encontrado['detalles']['modelo']} ---")
            
            # Buscar las placas base compatibles con el procesador
            placas_base_compatibles = []
            for componente in datos["componentes"]:
                if componente["categoria"] == "Placa Base":
                    for compatibilidad in compatibilidades_procesador:
                        if compatibilidad in componente["detalles"]["compatibilidad"]:
                            placas_base_compatibles.append(componente["detalles"]) 
            
            # Imprime las placas base compatibles
            if placas_base_compatibles:
                for placa in placas_base_compatibles:
                    print(f"Marca: {placa['marca']} | Modelo: {placa['modelo']} | Precio: ${placa['precio']:.2f} | Factor de forma: {placa['especificaciones']['factor_forma']}")
            else:
                print("No se encontraron placas base compatibles con este procesador.")
    else:
        print("Procesador no encontrado. Asegúrate de que el nombre esté correctamente escrito.")

# Funcion ejercicio libre
def caja_torre_mas_barata_atx():
    with open('hardware.json', 'r') as f:
        data = json.load(f)
    
    cajas = [comp for comp in data['componentes'] if comp['categoria'] == 'Caja/Torre']
    cajas_atx = [caja for caja in cajas if 'ATX' in caja['detalles']['compatibilidad']]
    
    if cajas_atx:
        caja_barata = min(cajas_atx, key=lambda x: x['detalles']['precio'])
        detalles = caja_barata['detalles']
        print(f"La caja/torre más barata compatible con ATX es {detalles['modelo']} de {detalles['marca']} con un precio de ${detalles['precio']} y {detalles['disponibilidad']['stock']} unidades disponibles.")
    else:
        print("No se encontraron cajas/torres compatibles con ATX.")
