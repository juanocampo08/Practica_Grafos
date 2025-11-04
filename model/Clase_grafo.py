
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.sedes = []
        self.costo_por_km = 950 

    def agregar_sede(self, nombre_sede):
        """Agrega una sede al grafo."""
        if nombre_sede not in self.grafo:
            self.grafo[nombre_sede] = []
            self.sedes.append(nombre_sede)


    def agregar_ruta(self, sede_1, sede_2, distancia_km):
        """Agrega una ruta bireccional entre dos sedes.
        
        sede_1 y sede_2: nombres de las sedes.
        distancia_km: distancia en kilómetros entre las sedes.
        """
        

grafo_prueba = Grafo()
grafo_prueba.agregar_sede("Sede a")
grafo_prueba.agregar_sede("Sede B")
print(grafo_prueba.grafo)


    