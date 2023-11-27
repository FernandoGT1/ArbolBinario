# main.py

from arbol.arbol import ArbolAviones, NodoAvion
from funciones_publicas.funciones_publicas import insertar_avion, buscar_avion, eliminar_avion, mostrar_inorden, mostrar_aviones, mostrar_preorden, mostrar_postorden

def main():
    arbol_aviones = ArbolAviones()

    while True:
        print("\n1. Insertar Avión")
        print("2. Buscar Avión")
        print("3. Eliminar Avión")
        print("4. Mostrar Recorrido Inorden")
        print("5. Mostrar Aviones en el Árbol")
        print("6. Mostrar Recorrido Preorden")
        print("7. Mostrar Recorrido Postorden")
        print("8. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            modelo = input("Ingrese el modelo del avión: ")
            capacidad = int(input("Ingrese el numero de pasajeros  : "))
            insertar_avion(arbol_aviones, modelo, capacidad)
        elif opcion == 2:
            modelo = input("Ingrese el modelo del avión a buscar: ")
            resultado = buscar_avion(arbol_aviones, modelo)
            if resultado:
                print(f"Avión encontrado: Modelo - {resultado[0]}, Capacidad - {resultado[1]}")
            else:
                print("Avión no encontrado.")
        elif opcion == 3:
            modelo = input("Ingrese el modelo del avión a eliminar: ")
            eliminar_avion(arbol_aviones, modelo)
            print(f"Avión con modelo {modelo} eliminado.")
            continue
        elif opcion == 4:
            mostrar_inorden(arbol_aviones)
        elif opcion == 5:
             arbol_aviones.mostrar_arbol()
        elif opcion == 6:
            mostrar_preorden(arbol_aviones)
        elif opcion == 7:
            mostrar_postorden(arbol_aviones)
        elif opcion == 8:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
