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



