import funciones

# menu
def main():
    ejecutando = True # Inicializo una variable en true, 
                      # para luego poder usarla como false para salirme del programa

    while ejecutando:
        print("\n--- Menu de opciones ---")
        print("1. Listar informacion")
        print("2. Contar informacion")
        print("3. Filtrar informacion")
        print("4. Salir")

        opcion=input("Elige una opcion: ")

        if opcion == "1":
            funciones.listar_procesadores()
        elif opcion == "2":
            funciones.contar_tarjetas_graficas()
        elif opcion == "3":
            min_precio = float(input("Introduce el precio mínimo: "))
            max_precio = float(input("Introduce el precio máximo: "))
            funciones.filtrar_almacenamiento_por_precio(min_precio, max_precio)

        elif opcion == "4":
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opcion no válida, reinténtalo")

if __name__ == "__main__":
    main()