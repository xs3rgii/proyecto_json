import json

#Cargar el json (Abre el json como lectura y lo carga en un diccionario)
def cargar_json():
    with open("hardware.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
# Funcion para listar los procesadores
def listar_procesadores():
    datos = cargar_json() # carga el json
    print("\n--- Lista de procesadores ---\n")
    for componente in datos["componentes"]:
        if componente["categoria"] == "Procesador":
            modelo = componente["detalles"]["modelo"]
            marca = componente ["detalles"]["marca"]
            precio = componente["detalles"]["precio"]
            nucleos= componente["detalles"]["especificaciones"]["nucleos"]
            print(f"Modelo: {modelo} | Marca: {marca} | Precio: {precio}€ | Núcleos: {nucleos}")

# Funcion para contar las tarjetas graficas
def contar_tarjetas_graficas():
    datos = cargar_json()
    tarjetas = {}

    for componente in datos["componentes"]:
        if componente["categoria"] == "Tarjeta Gráfica":
            modelo = componente["detalles"]["modelo"]
            marca = componente["detalles"]["marca"]
            unidades = componente["detalles"]["disponibilidad"]["stock"]
            if modelo in tarjetas:
                tarjetas[modelo]["unidades"] += unidades
            else:
                tarjetas[modelo] = {"marca": marca, "unidades": unidades}

    print("\n--- Tarjetas gráficas ---")
    total = 0
    for modelo, info in tarjetas.items():
        marca = info["marca"]
        unidades = info["unidades"]
        print(f"Marca: {marca} | Modelo: {modelo} | Unidades: {unidades}")
        total += unidades
    print(f"Total de tarjetas gráficas: {total}")

# funcion para filtrar precio almacenamiento
def filtrar_almacenamiento_por_precio(min_precio, max_precio):
    datos = cargar_json()
    almacenamientos = []

    for componente in datos["componentes"]:
        if componente["categoria"] == "Almacenamiento":
            try:
                precio = float(componente["detalles"]["precio"])
                if min_precio <= precio <= max_precio:
                    almacenamientos.append(componente["detalles"])
            except ValueError:
                print(f"Error: El precio de {componente['detalles']['modelo']} no es válido.")

    if almacenamientos:
        print("\n--- Componentes de almacenamiento en el rango de precios ---")
        for almacenamiento in almacenamientos:
            print(f"Marca: {almacenamiento['marca']} | Modelo: {almacenamiento['modelo']} | Precio: ${almacenamiento['precio']:.2f}")
    else:
        print("No hay componentes de almacenamiento en ese rango de precios.")
