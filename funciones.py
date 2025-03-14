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
            unidades = componente["detalles"]["disponibilidad"]["stock"]
            if modelo in tarjetas:
                tarjetas[modelo] += unidades
            else:
                tarjetas[modelo] = unidades

    print("\n--- Tarjetas gráficas ---")
    total = 0
    for modelo, unidades in tarjetas.items():
        print(f"Modelo: {modelo} | Unidades: {unidades}")
        total += unidades
        print(f"Total de tarjetas gráficas: {total}")
        