import funciones

# menu
def main():
    ejecutando = True # Inicializo una variable en true, 
                      # para luego poder usarla como false para salirme del programa

    while ejecutando:
        print("\n--- Menu de opciones ---")
        print("1. Listar informacion")
        print("2. Salir")

        opcion=input("Elige una opcion: ")

        if opcion == "1":
            funciones.listar_procesadores()
        elif opcion == "2":
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opcion no valida, Reintentalo")

if __name__ == "__main__":
    main()