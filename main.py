import funciones

# Menu

def main():
    ejecutando = True  # Variable de control para mantener el programa en ejecución

    while ejecutando:
        print("\n--- Menú de opciones ---")
        print("1. Listar procesadores")
        print("2. Contar tarjetas gráficas")
        print("3. Filtrar almacenamiento por precio")
        print("4. Buscar placas base compatibles con un procesador")
        print("5. Encontrar la caja/torre más barata compatible con ATX")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            funciones.listar_procesadores()
        elif opcion == "2":
            funciones.contar_tarjetas_graficas()
        elif opcion == "3":
            min_precio = float(input("Introduce el precio mínimo: "))
            max_precio = float(input("Introduce el precio máximo: "))
            funciones.filtrar_almacenamiento_por_precio(min_precio, max_precio)
        elif opcion == "4":
            funciones.buscar_placas_base_compatibles()
        elif opcion == "5":
            funciones.caja_torre_mas_barata_atx()
        elif opcion == "6":
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opción no válida, reinténtalo")

if __name__ == "__main__":
    main()
