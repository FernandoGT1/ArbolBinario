# funciones_publicas.py

from arbol.arbol import ArbolAviones, NodoAvion

def insertar_avion(arbol, modelo, capacidad):
    # Llamada al método de inserción pública de la clase ArbolAviones
    arbol._insertar_nodo(arbol.raiz, NodoAvion(modelo, capacidad))

def buscar_avion(arbol, modelo):
    # Llamada a la función privada de búsqueda del árbol
    nodo_encontrado = arbol._buscar_nodo(arbol.raiz, modelo)
    if nodo_encontrado:
        return nodo_encontrado.modelo, nodo_encontrado.capacidad
    else:
        return None

def eliminar_avion(arbol, modelo):
    # Llamada a la función privada de eliminación del árbol
    arbol._eliminar_nodo(arbol.raiz, modelo)

def mostrar_inorden(arbol):
    # Llamada al método privado de recorrido inorden del árbol
    arbol._recorrido_inorden(arbol.raiz)
    print()

def mostrar_aviones(arbol_aviones):
    aviones = arbol_aviones.obtener_lista_aviones()
    print("Aviones en el árbol:", ", ".join(aviones))

def mostrar_inorden(arbol):
    # Llamada al método privado de recorrido inorden del árbol
    aviones = arbol.obtener_lista_aviones()
    print("Inorden:")
    for avion in aviones:
        print(f"Modelo - {avion['Modelo']}, Capacidad - {avion['Capacidad']}", end=", ")
    print()
    
def mostrar_aviones(arbol_aviones):
    aviones = arbol_aviones.obtener_lista_aviones()
    print("Aviones en el árbol:")
    for avion in aviones:
        print(f"{avion.modelo}, {avion.capacidad}")

def mostrar_preorden(arbol):
    print("Preorden:")
    arbol._recorrido_preorden(arbol.raiz)
    print()

def mostrar_postorden(arbol):
    print("Postorden:")
    arbol._recorrido_postorden(arbol.raiz)
    print()
    

# Puedes agregar más funciones públicas según tus necesidades
