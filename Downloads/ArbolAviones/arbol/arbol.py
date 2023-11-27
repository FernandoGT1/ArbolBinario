# arbol.py

class NodoAvion:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad
        self.izquierda = None
        self.derecha = None

class ArbolAviones:
    def __init__(self):
        self.raiz = None

    # Funciones privadas

    def _insertar_nodo(self, nodo, nuevo_nodo):
        # Implementación del método de inserción
        if nodo is None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.modelo < nodo.modelo:
            if nodo.izquierda is None:
                nodo.izquierda = nuevo_nodo
            else:
                self._insertar_nodo(nodo.izquierda, nuevo_nodo)
        elif nuevo_nodo.modelo > nodo.modelo:
            if nodo.derecha is None:
                nodo.derecha = nuevo_nodo
            else:
                self._insertar_nodo(nodo.derecha, nuevo_nodo)

    def _recorrido_inorden(self, nodo, aviones):
        # Implementación del recorrido inorden
        if nodo:
            self._recorrido_inorden(nodo.izquierda, aviones)
            aviones.append({"Modelo": nodo.modelo, "Capacidad": nodo.capacidad})
            self._recorrido_inorden(nodo.derecha, aviones)

    def _recorrido_preorden(self, nodo):
        # Implementación del recorrido preorden
        if nodo:
            print(nodo.modelo, end=", ")
            self._recorrido_preorden(nodo.izquierda)
            self._recorrido_preorden(nodo.derecha)

    def _recorrido_postorden(self, nodo):
        # Implementación del recorrido postorden
        if nodo:
            self._recorrido_postorden(nodo.izquierda)
            self._recorrido_postorden(nodo.derecha)
            print(nodo.modelo, end=", ")

    def _buscar_nodo(self, nodo, modelo):
        # Implementación del método de búsqueda
        if nodo is None or nodo.modelo == modelo:
            return nodo
        if modelo < nodo.modelo:
            return self._buscar_nodo(nodo.izquierda, modelo)
        return self._buscar_nodo(nodo.derecha, modelo)

    def _eliminar_nodo(self, nodo, modelo):
        # Implementación del método de eliminación
        if nodo is None:
            return None

        if modelo < nodo.modelo:
            nodo.izquierda = self._eliminar_nodo(nodo.izquierda, modelo)
        elif modelo > nodo.modelo:
            nodo.derecha = self._eliminar_nodo(nodo.derecha, modelo)
        else:
            # Caso 1: Sin hijos o solo uno
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 2: Dos hijos
            sucesor = self._encontrar_sucesor(nodo.derecha)
            nodo.modelo = sucesor.modelo
            nodo.capacidad = sucesor.capacidad
            nodo.derecha = self._eliminar_nodo(nodo.derecha, sucesor.modelo)

        return nodo

    # Funciones adicionales para casos específicos de eliminación
    def _buscar_nodo_a_eliminar(self, nodo, modelo):
        if nodo is None:
            return None
        if modelo < nodo.modelo:
            return self._buscar_nodo_a_eliminar(nodo.izquierda, modelo)
        elif modelo > nodo.modelo:
            return self._buscar_nodo_a_eliminar(nodo.derecha, modelo)
        else:
            return nodo

    def _encontrar_padre(self, nodo, modelo):
        if nodo:
            if nodo.izquierda and nodo.izquierda.modelo == modelo:
                return nodo
            elif nodo.derecha and nodo.derecha.modelo == modelo:
                return nodo
            elif modelo < nodo.modelo:
                return self._encontrar_padre(nodo.izquierda, modelo)
            else:
                return self._encontrar_padre(nodo.derecha, modelo)
        return None

    def _eliminar_caso_1_o_2(self, nodo, padre, es_hijo_izquierdo):
        if nodo.izquierda is None and nodo.derecha is None:
            if es_hijo_izquierdo:
                padre.izquierda = None
            else:
                padre.derecha = None
        elif nodo.izquierda is None:
            if es_hijo_izquierdo:
                padre.izquierda = nodo.derecha
            else:
                padre.derecha = nodo.derecha
        else:
            if es_hijo_izquierdo:
                padre.izquierda = nodo.izquierda
            else:
                padre.derecha = nodo.izquierda

    def _eliminar_caso_3(self, nodo, padre, es_hijo_izquierdo):
        sucesor = self._encontrar_sucesor(nodo.derecha)
        self._eliminar_nodo(sucesor, sucesor.modelo)
        nodo.modelo = sucesor.modelo
        nodo.capacidad = sucesor.capacidad

    def _encontrar_sucesor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def obtener_lista_aviones(self):
        aviones = []
        self._recorrido_inorden(self.raiz, aviones)
        return aviones

    def mostrar_arbol(self):
        self._mostrar_arbol(self.raiz, 0)

    def _mostrar_arbol(self, nodo, nivel):
        if nodo:
            self._mostrar_arbol(nodo.derecha, nivel + 1)
            print("  " * nivel + f"{nodo.modelo} - {nodo.capacidad}")
            self._mostrar_arbol(nodo.izquierda, nivel + 1)
